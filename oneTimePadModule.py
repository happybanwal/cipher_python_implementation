import onetimepad

message = "NO ATTACK"
cipher = "DO ATTACK"

print("original Text :" + message)

encrypt = onetimepad.encrypt(message, cipher)
print("encrypt message:" + encrypt)

decrypt = onetimepad.decrypt(encrypt, cipher)
print("decrypt message:" + decrypt)
