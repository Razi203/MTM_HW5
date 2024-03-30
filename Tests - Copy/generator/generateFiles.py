import random
import string
import sys
import os

def main(n):
    suffixes = ['ERROR', 'brr', 'enc']
    storage = string.whitespace[:3] + string.digits + string.ascii_letters + string.punctuation
    for i in range(1,n+1):
        text = "".join([random.choice(storage) for i in range(500)])
        name = 'input' + str(i) + '.' + random.choice(suffixes)
        with open(os.path.join(os.getcwd(), 'caesar_enc3', name), 'w') as f:
            f.write(text)
    

if __name__ == "__main__":
    fileCount = 1000
    main(fileCount)