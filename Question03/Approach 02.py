# Author : Zubeir Msemo

# Encryption and decryption algorithms


def encrypt(key, message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) + key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result

def decrypt(key, message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) - key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result

def main():
    print("")
    print("====================================")
    word = input("Enter message: ")
    print("====================================")
    key_value = input("Enter key(2 or 3): ")
    if key_value == "2":
        #encrypt
        print("====================================") 
        encrypted = encrypt(2,word)
        print ("The encrypted message is:", encrypted)
        print("")
        print("====================================")
        
        val = input("Press Yes to decrypt : ") 
        print("====================================")
        if val == "Yes":
            decrypted = decrypt(2,encrypted)
            print("The decrypted message is:", decrypted)
        else:
            print("Sorry !! Wrong Inputs , Goodbye")
    else:
        #encrypt
        print("====================================") 
        encrypted = encrypt(3,word)
        print ("The encrypted message is:", encrypted)
        print("")
        print("====================================")
        
        val = input("Press Yes to decrypt: ") 
        print("====================================")
        if val == "Yes":
            decrypted = decrypt(3,encrypted)
            print("The decrypted message is:", decrypted)
        else:
            print("Sorry !! Wrong Inputs , Goodbye")
        

if __name__ == "__main__":
    main()