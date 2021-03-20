
from cryptography.fernet import Fernet

messages = ['hi', 'hello', 'greetings']
key = Fernet.generate_key()
print("=====Key======")
print(key)
print("===========")
fernet = Fernet(key)
encrypted_message = [fernet.encrypt(each_message.encode())
                     for each_message in messages]

print("Original String Value: ", messages)
print("Encrypted String Value: ", encrypted_message)
decrypted_message = [fernet.decrypt(each_message).decode()
                     for each_message in encrypted_message]
print("decrypted string: ", decrypted_message)

with open('test2.txt', 'wb') as file:
    file.writelines(encrypted_message)
