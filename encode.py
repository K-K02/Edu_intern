from PIL import Image

# Path to the image
img_path = "C:\\Users\\karth\\OneDrive\\Desktop\\Intern\\a1.jpeg"

# Open the image
img = Image.open(img_path, 'r')
new_img = img.copy()

# Get image dimensions
w, h = img.size

# Prompt for the secret numerical message
msg = input("Enter a secret numerical message (0-9 only): ")

# Validate that the message contains only numbers
if not msg.isdigit():
    print("Invalid message. Please enter only numbers.")
    exit()

# Convert the message to a binary string
bin_msg = ''.join(format(ord(char), '08b') for char in msg)

# Append null character to the message to indicate end
bin_msg += '00000000'

# Prompt for the passcode
try:
    passcode = int(input("Enter a passcode: "))
except ValueError:
    print("Invalid passcode. Please enter a number.")
    exit()

# Encrypt the binary message with the passcode
enc_msg = ''.join(format((int(bit) + passcode) % 2, 'b') for bit in bin_msg)

msg_idx = 0
for y in range(h - 1, -1, -1):
    for x in range(w - 1, -1, -1):
        if msg_idx < len(enc_msg):
            # Get current pixel value
            r, g, b = img.getpixel((x, y))

            # Encode the bit into the LSB of the red channel
            new_r = (r & ~1) | int(enc_msg[msg_idx])
            msg_idx += 1

            # If there are still bits left, encode the next bit into the blue channel
            if msg_idx < len(enc_msg):
                new_b = (b & ~1) | int(enc_msg[msg_idx])
                msg_idx += 1
            else:
                new_b = b

            # Update the pixel value in the new image
            new_img.putpixel((x, y), (new_r, g, new_b))
        else:
            break
    if msg_idx >= len(enc_msg):
        break

# Save the modified image to a new file
new_img_path = "C:\\Users\\karth\\OneDrive\\Desktop\\Intern\\a2.png"
new_img.save(new_img_path, "PNG")

print("Image created.")
