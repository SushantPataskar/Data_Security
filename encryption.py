from cryptography.fernet import Fernet

def gen_key():
    key = Fernet.generate_key()
    fernet = Fernet(key)
    return fernet

def encrypt_data(data,fernet):
    encMessage = fernet.encrypt(data.encode())
    return encMessage

def decrypt_data(data,fernet):
    decMessage = fernet.decrypt(data).decode()
    return decMessage

fernet=gen_key()
encrypted_data=encrypt_data("PII Data",fernet)
decrypted_data=decrypt_data(encrypted_data,fernet)
print("encrypted_data "+encrypted_data.decode())
print("encrypted_data ",encrypted_data)
print("decrypted_data "+decrypted_data)