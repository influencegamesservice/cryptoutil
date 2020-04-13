import cryptography
from cryptography.fernet import Fernet
import os

class Encryption:
    def __init__(self):
        pass

    def __create_key(self):
        return Fernet.generate_key()
    
    def __save_key(self, key, file_path):
        with open(file_path, 'wb') as f:
            f.write(key)
    
    def __load_key(self, file_path):
        with open(file_path, 'rb') as f:
            return f.read()

    def __load_plainstring_to_binary(self, plainstring):
        return plainstring.encode()
    
    def __load_encryption(self, en_file):
        with open(en_file, 'rb') as f:
            return f.read()
    
    def __plaintext2encryption(self, plaintext, key):
        return Fernet(key).encrypt(plaintext)
    
    def __encryption2plaintext(self, encryption, key):
        return Fernet(key).decrypt(encryption)
    
    def __save_encryption(self, encryption, path):
        with open(path, 'wb') as f:
            f.write(encryption)
    
    def create_encryptionAndkey(self, plainstring, key_save_path, encryption_save_path):
        key = self.__create_key()
        self.__save_key(key, key_save_path)
        bplaintext = self.__load_plainstring_to_binary(plainstring)
        encryption = self.__plaintext2encryption(bplaintext, key)
        self.__save_encryption(encryption, encryption_save_path)
    
    def load_encryption2plaintext(self, key_load_path, encryption_load_path, return_plain_text_decode=True):
        bencryption = self.__load_encryption(encryption_load_path)
        key = self.__load_key(key_load_path)

        if return_plain_text_decode:
            return self.__encryption2plaintext(bencryption, key).decode()
        else:
            return self.__encryption2plaintext(bencryption, key)
