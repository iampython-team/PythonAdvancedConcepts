import rsa
from rsa.key import PrivateKey, PublicKey

message = 'hello iampython'

publicKey, privateKey = rsa.newkeys(512)
print(publicKey, privateKey)

encrption_message = rsa.encrypt(message.encode(), publicKey)
print(encrption_message)


decrpt_message = rsa.decrypt(encrption_message, privateKey).decode()
print(decrpt_message)
