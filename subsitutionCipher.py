import random


def generate_key():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_012356789 "
    cletters = list(letters)
    key = {}
    for c in letters:
        key[c] = cletters.pop(random.randint(0, len(cletters) - 1))
    return key


def encrypt(key, message):
    cipher = ""
    for i in range(0, len(message)):
        # print(message[i])
        cipher = key[message[i]] + cipher
    return cipher


def decryption_key(key):
    dkey = {}

    for k in key:
        dkey[key[k]] = k
    return dkey


def decrypt(d_key, message):
    cipher = ""
    for i in range(0, len(message)):
        print(message[i])
        cipher = d_key[message[i]] + cipher
    # return cipher
    print(cipher)


# original message
message = "i am HAPPY 0123"
print("original msg :" + message)

# encryption key
key = generate_key()
print("encryption key\n" + str(key))

# encrpyted message
encrypted_msg = encrypt(key, message)
print("encrypted msg :" + encrypted_msg)

# decryption key
d_key = decryption_key(key)
print("decryption key\n" + str(d_key))

k = encrypt(d_key, encrypted_msg)
print("decrypted msg :" + k)
