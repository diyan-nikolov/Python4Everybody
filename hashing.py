import hashlib

#the string we input must be passed as a bytestring (use .encode() method to convert it to bytestring format)
def encrypt_stringMD5(hash_string):
    hash_signature = hashlib.md5(hash_string.encode()).hexdigest()
    return hash_signature
def encrypt_stringSHA1(hash_string):
    hash_signature = hashlib.sha1(hash_string.encode()).hexdigest()
    return hash_signature
def encrypt_stringSHA256(hash_string):
    hash_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return hash_signature

selection = input("Which hashing type would you like to use? Type 1 for MD5, 2 for SHA-1 and 3 for SHA-256: ")

if int(selection) == 1:
    hash_string = input("Input information you would like hashed: ")
    hash_signature = encrypt_stringMD5(hash_string)
    print("Your hashed string is: ", hash_signature)
elif int(selection) == 2:
    hash_string = input("Input information you would like hashed: ")
    hash_signature = encrypt_stringSHA1(hash_string)
    print("Your hashed string is: ", hash_signature)
elif int(selection) == 3:
    hash_string = input("Input information you would like hashed: ")
    hash_signature = encrypt_stringSHA256(hash_string)
    print("Your hashed string is: ", hash_signature)
    









