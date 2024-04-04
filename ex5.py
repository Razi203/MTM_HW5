import os
import json


class Cipher():
    def encrypt(self, string):
        return self.modify_string(string, 1)
    
    def decrypt(self, string):
        return self.modify_string(string, -1)
    
    def modify_letter(self, letter, key):
        if not letter.isalpha(): 
            return letter
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if letter.islower():
            letters = letters.lower()
        index = letters.find(letter)
        new_index = (index + key) % len(letters) 
        return letters[new_index]
    
    def modify_string(self, string, modifier):
        modified = ""
        for c in string:
            modified += self.modify_letter(c, modifier*self.get_key()) if c.isalpha() else c
        return modified
    
    def get_key(self):
        raise("Abstract base class should not be used!")


class CaesarCipher(Cipher):
    def __init__(self, key):
        self.key = key

    def key_shift(self, delta):
        self.key += delta
    
    def get_key(self):
        return self.key
    

class VigenereCipher(Cipher):
    def __init__(self, keys):
        self.keys = keys
        self.index = 0
    
    def get_key(self):
        new = self.keys[self.index % len(self.keys)]
        self.index += 1
        return new
    
    def encrypt(self, string):
        self.index = 0
        return self.modify_string(string, 1)
    
    def decrypt(self, string):
        self.index = 0
        return self.modify_string(string, -1)


def loadEncryptionSystem(dir_path, plaintext_suffix):
    files = [os.path.join(dir_path, name) for name in os.listdir(dir_path)]
    config_path = os.path.join(dir_path, 'config.json')
    with open(config_path, 'r') as f:
        config = json.load(f)
        
    if config['type'] == 'Caesar':
        cipher = CaesarCipher(config['key'])
    else:
        cipher = VigenereCipher(config['key'])

    org_suffix, new_suffix = (plaintext_suffix, 'enc') if config['encrypt'] == 'True' else ('enc', plaintext_suffix)

    for file_path in files:
        if not file_path.endswith(org_suffix):
            continue
        with open(file_path, 'r') as file:
            message = cipher.encrypt(file.read()) if config['encrypt'] == 'True' else cipher.decrypt(file.read())
        new_file_path = os.path.splitext(file_path)[0] + '.' + new_suffix
        with open(new_file_path, 'w') as file:
            file.write(message)


     