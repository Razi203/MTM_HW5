from solver import *

def main():
    dict_v = {"type": "Vigenere",
    "encrypt": "True",
    "key": [ 9, 18, 14, 13, -9, 4, 24, 22, 8, 19, 7, -5, 14, 13, 0, 11, 15, 7, 0, 2, 7, 0, -20, 18]}

    with open(os.path.join('vigenere', 'config.json'), 'w') as f:
        json.dump(dict_v, f, indent=4)

    loadEncryptionSystem('vigenere', 'vigenere')


    dict_v_enc = {"type": "Vigenere",
    "encrypt": "False",
    "key": [4, 8, -4, 13, -9, 4, -124, 22, 8, 19, 7, -5, 14, 513, 0, 11, 15, 7, 0, 2, 7, 0, -20, 18 ]}

    with open(os.path.join('vigenere_encrypted', 'config.json'), 'w') as f:
        json.dump(dict_v_enc, f, indent=4)

    loadEncryptionSystem('vigenere_encrypted', 'out')
    values = [-18,9,-8,20]
    for i in range(1,5):
        dict_c = {"type": "Caesar",
        "encrypt": "True",
        "key": values[i-1]}
        with open(os.path.join('caesar', 'config.json'), 'w') as f:
            json.dump(dict_c, f, indent=4)
        loadEncryptionSystem('caesar', 'c' + str(i))


    values = [-2,3,0]
    for i in range(3,4):
        dict_c = {"type": "Caesar",
        "encrypt": "False",
        "key": values[i-1]}
        with open(os.path.join('caesar_enc' + str(i), 'config.json'), 'w') as f:
            json.dump(dict_c, f, indent=4)
        loadEncryptionSystem('caesar_enc' + str(i), 'c' + str(i))

if __name__ == '__main__':
    main()