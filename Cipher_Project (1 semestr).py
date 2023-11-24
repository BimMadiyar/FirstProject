alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def menu():
    print("1. Caesar")
    print("2. Vigenere")
    print("3. Playfair")
    try:
        choose_cipher = int(input("Which Cipher type do you want to use? (1 / 2 / 3): "))
        if choose_cipher == 1:
            print()
            caesar()
        elif choose_cipher == 2:
            print()
            vigenere()
        elif choose_cipher == 3:
            print()
            playfair()
        else:
            menu()
    except ValueError:
        print("Please choose the number from (1 - 3): ")
        menu()

def caesar():
    print("1. Encipher")
    print("2. Decipher")
    try:
        choose_caesar = int(input('Which one do you want to use? (1 / 2): '))
        if choose_caesar == 1:
            print()
            encipher_caesar()
        elif choose_caesar == 2:
            print()
            decipher_caesar()
        else:
            print('Please choose the number 1 or 2? ')
            caesar()
    except ValueError:
        print('Please choose the number 1 or 2? ')
        caesar()

def encipher_caesar():
    plaintext = input('Enter the Plaintext: ').lower().split()
    while True:
        try:
            key = int(input('Enter the Key (1 - 26): '))
            if key >= 1 and key <= 26:
                break
        except ValueError:
            print("Please enter the number from (1 - 26): ")
    print('Cipher text:', end=' ')
    for word in plaintext:
        if plaintext.index(word) != 0:
            print(end=' ')
        for letter in word:
            index_cipher = alphabet.index(letter) + key
            if index_cipher >= 26:
                index_cipher = index_cipher - 26
            print(alphabet[index_cipher], end='')
    print()
    print()

def decipher_caesar():
    ciphertext = input('Enter the Ciphertext: ').lower().split()
    while True:
        try:
            key = int(input('Enter the Key (1 - 26): '))
            if key >= 1 and key <= 26:
                break
        except ValueError:
            print("Please enter the number from (1 - 26): ")
    print('Cipher text:', end=' ')
    for word in ciphertext:
        if ciphertext.index(word) != 0:
            print(end=' ')
        for letter in word:
            index_plain = alphabet.index(letter) - key
            if index_plain < 0:
                index_plain = 26 + index_plain
            print(alphabet[index_plain], end='')
    print()
    print()

def vigenere():
    print("1. Encipher")
    print("2. Decipher")
    try:
        choose_vigenere = int(input("You want Encipher or Decipher? (1 / 2): "))
        if choose_vigenere == 1:
            print()
            encipher_vigenere()
        elif choose_vigenere == 2:
            print()
            decipher_vigenere()
        else:
            print("Please choose the number 1 or 2: ")
            vigenere()
    except ValueError:
        print("Please choose the number 1 or 2: ")
        vigenere()

def encipher_vigenere():
    plaintext = input("Enter the Plaintext: ").lower().split()
    full_plaintext = ''.join(plaintext)
    keyword = input("Enter the Keyword: ")
    full_key = []
    while len(full_key) < len(full_plaintext):
        for i in range(len(keyword)):
            full_key.append(keyword[i])
            if len(full_key) == len(full_plaintext):
                break
    print("The Cipher text is:", end=' ')
    for word in plaintext:
        if plaintext.index(word) != 0:
            print(end= ' ')
        for i in range(len(word)):
            index_cipher = alphabet.index(word[i]) + alphabet.index(full_key[0])
            full_key.remove(full_key[0])
            if index_cipher >= 26:
                index_cipher = index_cipher - 26
            print(alphabet[index_cipher], end='')
    print()
    print()

print("Hi, this is Types of Ciphering!")
while True:
    menu()