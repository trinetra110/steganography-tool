
def decrypt(password, c, msg, img):
    
    message = ""
    n = 0
    m = 0
    z = 0

    pas = input("Enter passcode for Decryption: ")
    if password == pas:
        for i in range(len(msg)):
            message = message + c[img[n, m, z]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3
        print("Decryption message: ", message)
    else:
        print("You are not autorised to access the secret data.")
