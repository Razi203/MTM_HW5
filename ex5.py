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
        if letter.islower():
            start = ord('a')
        else:
            start = ord('A')
        new = (ord(letter) - start + key) % (ord('z') - ord('a') + 1)
        return chr(start + new)
    
    def modify_string(self, string, modifier):
        return "".join([self.modify_letter(c, modifier*self.get_key()) if c.isalpha() else c for c in string])
    
    def get_key(self):
        return 0


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

    for file_path in files:
        if config['encrypt'] == 'True':
            if not file_path.endswith(plaintext_suffix):
                continue
            with open(file_path, 'r') as file:
                message = cipher.encrypt(file.read())
            new_file_path = os.path.splitext(file_path)[0] + '.enc'
            with open(new_file_path, 'w') as file:
                file.write(message)
        else:
            if not file_path.endswith('enc'):
                continue
            with open(file_path, 'r') as file:
                message = cipher.decrypt(file.read())
            new_file_path = os.path.splitext(file_path)[0] + '.' + plaintext_suffix
            with open(new_file_path, 'w') as file:
                file.write(message)

if __name__ == '__main__':
    loadEncryptionSystem('.', 'my')

                


    

