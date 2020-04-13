import cryptography
from cryptography.fernet import Fernet
import os

class Encryption:
    def __init__(self):
        pass

    @staticmethod
    def __create_key():
        return Fernet.generate_key()
    
    @staticmethod
    def __save_key(key, file_path):
        with open(file_path, 'wb') as f:
            f.write(key)
    
    @staticmethod
    def __load_key(file_path):
        with open(file_path, 'rb') as f:
            return f.read()

    @staticmethod
    def __load_plainstring_to_binary(plainstring):
        return plainstring.encode()
    
    @staticmethod
    def __load_encryption(en_file):
        with open(en_file, 'rb') as f:
            return f.read()
    
    @staticmethod
    def __plaintext2encryption(plaintext, key):
        return Fernet(key).encrypt(plaintext)
    
    @staticmethod
    def __encryption2plaintext(encryption, key):
        return Fernet(key).decrypt(encryption)
    
    @staticmethod
    def __save_encryption(encryption, path):
        with open(path, 'wb') as f:
            f.write(encryption)
    
    @classmethod
    def create_encryptionAndkey(cls, plainstring, key_save_path, encryption_save_path):
        key = cls.__create_key()
        cls.__save_key(key, key_save_path)
        bplaintext = cls.__load_plainstring_to_binary(plainstring)
        encryption = cls.__plaintext2encryption(bplaintext, key)
        cls.__save_encryption(encryption, encryption_save_path)
    
    @classmethod
    def load_encryption2plaintext(cls, key_load_path, encryption_load_path, return_plain_text_with_decode=True):
        bencryption = cls.__load_encryption(encryption_load_path)
        key = cls.__load_key(key_load_path)

        if return_plain_text_with_decode:
            return cls.__encryption2plaintext(bencryption, key).decode()
        else:
            return cls.__encryption2plaintext(bencryption, key)
