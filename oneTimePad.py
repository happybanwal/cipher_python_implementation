# encode convert text into bytes
# decode vice versa 
# bytes is a built-in data type that represents a sequence of bytes, which are integer values between 0 and 255. Bytes are commonly used to represent raw binary data, such as images, audio files, and network packets.
message = "NO ATTACK"
cipher = "DO ATTACK"
message = message.encode()
cipher = cipher.encode()


def xor_bytes(key_stream, message):
    length = min(len(key_stream), len(message))
    return bytes([key_stream[i] ^ message[i] for i in range(length)])


print("original text :" ,message.decode())
key_stream = xor_bytes(message, cipher)

print("cipher text :" ,key_stream)
dKey = xor_bytes(key_stream, cipher)

dKey = dKey.decode()
print("decipher text :" ,dKey)

