import cv2
import os
import string

img = cv2.imread("mypic.jpg")  # Replace with the correct image path

msg = input("Enter secret message:")
password = input("Enter a passcode:")

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

m = 0
n = 0
z = 0

for i in range(len(msg)):
    img[m, n, z] = d[msg[i]]
    m = m + 1
    n = n + 1
    z = (z + 1) % 3

cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Use 'start' to open the image on Windows

message = ""
m = 0
n = 0
z = 0

pas = input("Enter passcode for Decryption")
if password == pas:
    for i in range(len(msg)):
        message = message + c[img[m, n, z]]
        m = m + 1
        n = n + 1
        z = (z + 1) % 3
    print("Decryption message:", message)
