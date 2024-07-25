from PIL import Image

# Path to the encoded image
img_path = "C:\\Users\\karth\\OneDrive\\Desktop\\Intern\\a2.png"

# Open the encoded image
img = Image.open(img_path, 'r')

# Get image dimensions
w, h = img.size

# Prompt for the passcode
try:
    passcode = int(input("Enter the passcode used for encoding: "))  # Example: 88
except ValueError:
    print("Invalid passcode. Please enter a number.")
    exit()

# Initialize binary message
bin_msg = ""

for y in range(h - 1, -1, -1):
    for x in range(w - 1, -1, -1):
        # Get pixel value
        r, g, b = img.getpixel((x, y))

        # Extract LSBs
        bin_msg += str(r & 1)
        bin_msg += str(b & 1)

# Decrypt binary message
dec_msg = ''.join(format((int(bit) + passcode) % 2, 'b') for bit in bin_msg)

# Convert binary to string
msg = ""
for i in range(0, len(dec_msg), 8):
    byte = dec_msg[i:i+8]
    if byte == '00000000':  
        break
    msg += chr(int(byte, 2))

print("Decoded message:", msg)
