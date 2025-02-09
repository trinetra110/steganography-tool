from encrypt import encrypt
from decrypt import decrypt

password = input("Enter your passcode: ")

(c, msg, img) = encrypt()
decrypt(password, c, msg, img)
