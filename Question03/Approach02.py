# cryptography through

import itertools

message = " Encrypt me!!"

def encrypt(message, password): 
    matrix = [[] for i in range(password)]
    counter =0
    encrypted_message = ""
    for i in range(0, len(message)):
        if counter < password:
            matrix[counter].append(message[i])
            counter += 1
            
        else:
            counter = 0
            matrix[counter].append(message[i])
            counter += 1
    encrypted_message= ''.join(itertools.chain(*matrix))
    return encrypted_message


def decrypt(encrypted, password):
    counter = 0
    decrypted_message = ''
    group_length =int(len(encrypted) / password)
    
    
    # check if length matches encrypted
    if isinstance(int, type(group_length)) == True:
        for z in encrypted:
            if counter < password:
                decrypted_message += encrypted[counter:(counter +password)]
            else: 
                first = encrypted[:(password + 1)]
                
                

ency = encrypt("Encrypr me!!", 2)
ency1= encrypt("Encrypr me!!", 3)

decry = decrypt("View Me!!", 3)

print(ency1)
print(decry)