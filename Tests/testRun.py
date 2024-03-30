import os
from ex5 import CaesarCipher, VigenereCipher, loadEncryptionSystem
import json

def compare_files_by_suffix(dir_path, suffix_a, suffix_b):
    file_groups = {}

    # Group files by their base name
    for filename in os.listdir(dir_path):
        base_name, extension = os.path.splitext(filename)
        if extension in (f".{suffix_a}", f".{suffix_b}"):
            base_name_parts = base_name.split('<')  # Assuming format is 'input<number>'
            if len(base_name_parts) == 2:
                group_key = base_name_parts[0]  # Use 'input' part as the group key
                file_groups.setdefault(group_key, []).append(os.path.join(dir_path, filename))

    # Compare files within each group
    for group_key, filenames in file_groups.items():
        if len(filenames) == 2:
            with open(filenames[0], 'rb') as file_a, open(filenames[1], 'rb') as file_b:
                if file_a.read() == file_b.read():
                    pass
                    #print(f"Files for '{group_key}' are identical.")   #   <---- uncomment if you want
                else:
                    print(f"Files for '{group_key}' differ!")
        else:
            print(f"Group '{group_key}': Not enough files for comparison.")


def main():
    path = os.path.join('.', 'vigenre')
    loadEncryptionSystem(path, 'vigenre')
    compare_files_by_suffix(path, 'out', 'enc')


    path = os.path.join('.', 'vigenre_encrypted')
    loadEncryptionSystem(path, 'vigenre')
    compare_files_by_suffix(path, 'out', 'vigenre')

    for i in range(1,4):
        path = os.path.join('.', 'caesar_enc' + str(i))
        loadEncryptionSystem(path, 'caesar')
        compare_files_by_suffix(path, 'out', 'caesar')


    path = os.path.join('.', 'caesar')
    values = [-18,9,-8,20]
    for i in range(1,5):
        dict_c = {"type": "Caesar",
        "encrypt": "True",
        "key": values[i-1]}
        with open(os.path.join('caesar', 'config.json'), 'w') as f:
            json.dump(dict_c, f, indent=4)
        loadEncryptionSystem('caesar', 'c' + str(i))
    compare_files_by_suffix(path, 'out', 'enc')


