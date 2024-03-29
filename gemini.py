
import os
import json

class CaesarCipher:
    def __init__(self, key):
        self.key = key % 26  # Ensures the key is between 0 and 25

    def key_shift(self, amount):
        self.key = (self.key + amount) % 26

    def encrypt(self, string):
        cipher = ''
        for char in string:
            if not char.isalpha():
                cipher += char
            else:
                new_ord = ord(char) + self.key
                if char.isupper():
                    cipher += chr((new_ord - ord('A')) % 26 + ord('A'))
                else:
                    cipher += chr((new_ord - ord('a')) % 26 + ord('a'))
        return cipher

    def decrypt(self, string):
        cipher = ''
        for char in string:
            if not char.isalpha():
                cipher += char
            else:
                new_ord = ord(char) - self.key
                if char.isupper():
                    cipher += chr((new_ord - ord('A')) % 26 + ord('A'))
                else:
                    cipher += chr((new_ord - ord('a')) % 26 + ord('a'))
        return cipher
    
class VigenereCipher:
    def __init__(self, keys):
        self.keys = keys
        self.key_index = 0

    def encrypt(self, string):
        cipher = ''
        self.key_index = 0
        for char in string:
            if not char.isalpha():
                cipher += char 
            else:
                key = self.keys[self.key_index]
                new_ord = ord(char) + key
                if char.isupper():
                    cipher += chr((new_ord - ord('A')) % 26 + ord('A'))
                else:
                    cipher += chr((new_ord - ord('a')) % 26 + ord('a'))

                self.key_index = (self.key_index + 1) % len(self.keys)  # Update key index

        return cipher

    def decrypt(self, string):
        plain_text = ''
        self.key_index = 0
        for char in string:
            if not char.isalpha():
                plain_text += char
            else:
                key = self.keys[self.key_index]
                new_ord = ord(char) - key
                if char.isupper():
                    plain_text += chr((new_ord - ord('A')) % 26 + ord('A'))
                else:
                    plain_text += chr((new_ord - ord('a')) % 26 + ord('a'))

                self.key_index = (self.key_index + 1) % len(self.keys)  # Update key index

        return plain_text



def loadEncryptionSystem(dir_path, plaintext_suffix):
    # Load configuration
    with open(os.path.join(dir_path, "config.json"), 'r') as f:
        config = json.load(f)

    # Determine action and set appropriate suffix
    if config["encrypt"]:
        output_suffix = "enc"
    else:
        output_suffix = plaintext_suffix

    # Process files in the directory
    for filename in os.listdir(dir_path):
        if filename.endswith(output_suffix):  # Skip already processed files
            continue

        base_filename, file_extension = os.path.splitext(filename)

        if file_extension[1:] == plaintext_suffix:  # Suitable for encryption/decryption
            input_filepath = os.path.join(dir_path, filename)
            output_filepath = os.path.join(dir_path, base_filename + '.' + output_suffix)

            process_file(config, input_filepath, output_filepath)

def process_file(config, input_filepath, output_filepath):
    with open(input_filepath, 'r') as infile, open(output_filepath, 'w') as outfile:
        text = infile.read()

        if config["type"] == "Caesar":
            cipher = CaesarCipher(config["key"])
        elif config["type"] == "Vigenere":
            cipher = VigenereCipher(config["key"])
        else:
            print(f"Unknown encryption type: {config['type']}")
            return

        if config["encrypt"]:
            result = cipher.encrypt(text)
        else:
            result = cipher.decrypt(text)
        outfile.write(result)

loadEncryptionSystem(".", "txt")  # Example with .txt files
