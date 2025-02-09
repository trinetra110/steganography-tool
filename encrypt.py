import cv2
import os

def encrypt():
    
    f = input("Enter the path of the image: ")
    img = cv2.imread(f)

    msg = input("Enter secret message: ")

    d = {}
    c = {}

    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)

    m = 0
    n = 0
    z = 0

    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    cv2.imwrite("stego_test.jpg", img)
    os.system("start stego_test.jpg")
    
    return c, msg, img
