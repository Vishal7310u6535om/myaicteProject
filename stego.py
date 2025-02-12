import cv2
import os
import string

# Load the image (replace with the correct image path)
img = cv2.imread(r"C:\Users\user\OneDrive\Desktop\Stenography-main\vishal.jpg")
if img is None:
    print("Image not found. Please check the path.")
    exit()

# Encrypt the message
cv2.imwrite(r"C:\Users\user\OneDrive\Desktop\Stenography-main\vishal.jpg", img)

msg = input("Enter secret message:")
password = input("Enter a passcode:")

# Create dictionaries for encoding and decoding
d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

m = 0
n = 0
z = 0

# Loop to encode the message into the image
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Open the image on Windows

# Decryption process
message = ""
n = 0
m = 0
z = 0

# Ask for passcode for decryption
pas = input("Enter passcode for Decryption: ")
if password == pas:
    # Decrypt the message from the image
    for i in range(len(msg)):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decrypted message:", message)
else:
    print("YOU ARE NOT AUTHORIZED")
