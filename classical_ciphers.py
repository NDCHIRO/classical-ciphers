import string
import numpy as np

def chunks(str,n):
    chunks = [str[i:i + n] for i in range(0, len(str), n)]
    #print(chunks)
    return chunks

def Convert(word):
    return [char for char in word]
###################################################################################################
################################ caesar cipher function ###########################################
###################################################################################################
def CaesarCipherEncrypt(plainText, shiftNumber):
    #print("Caesar Cipher encryption")
    result = ""
    for i in range(len(plainText)):
        char = plainText[i]
        result += chr((ord(char) + shiftNumber - 97) % 26 + 97)
    return result


###################################################################################################
################################ playfair functions ###############################################
###################################################################################################
squareList = [['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''],
              ['', '', '', '', '']]


# make the 5*5 square
def makeSquare(square, alpha_list):
    i = 0
    # make the square with right indics
    while (True):
        if (i == 26):
            break
        if (alpha_list[i] in square or alpha_list[i] == 'j'):
            i += 1
            continue
        square.append(alpha_list[i])
        i += 1

    # make the square as 2d array
    k = 0
    for i in range((5)):
        for j in range(5):
            squareList[i][j] = square[k]
            k += 1
    print(squareList)
    # print the square
    k = 0
    #print()
    for i in range((5)):
        for j in range(5):
            # squareList.append((square[k]))
            print(" " + (squareList[i][j]), end=" ")
            print("|", end=" ")
            k += 1
        print("\n-------------------------")

    return squareList
def playFairEncrypt(plainText, key):
    encryptionText = []
    plain = []
    plain.append(plainText)
    #print("playfair encryption")
    alpha_list = []
    for i in string.ascii_lowercase:
        alpha_list.append(i)
    square = []
    for i in (key):
        square.append(i)

    squareList = makeSquare(square, alpha_list)

# check if the two characters are in the same column or no
splitColumn = 0


def sameColumn(splitText, squareList, encryptionText):
    col1 = 5000  # random values just to make sure that they will not col1 equal col2
    row1 = -1
    col2 = -1000
    row2 = -1

    same = False
    for i in range(len(squareList)):
        for j in range(len(squareList)):
            if (splitText[splitColumn][0] == squareList[i][j]):
                col1 = j
                row1 = i
            if (splitText[splitColumn][1] == squareList[i][j]):
                col2 = j
                row2 = i
            if (col1 == col2):
                splitColumn += 1
                print(splitColumn)
                same = True
                if (row1 != 4):
                    encryptionText.append(squareList[row1 + 1][j])
                    print(squareList[row1 + 1][j])
                elif (row1 == 4):
                    encryptionText.append(squareList[row1 - 4][j])
                    print(squareList[row1 - 4][j])
                if (row2 != 4):
                    encryptionText.append(squareList[row2 + 1][j])
                    print(squareList[row2 + 1][j])
                elif (row1 == 4):
                    encryptionText.append(squareList[row2 - 4][j])
                    print(squareList[row2 - 4][j])
                return

            # playfair function


def playfair(plain,key):
    key = key.upper()
    plain = str(plain).upper().replace("J","I")
    posdic = dict() # represent the order of each letter in the key matrix if it was 1D
    index = 0# the index of the current letter in the posdic
    letters = ""

    for k in key:
        if(k not in posdic):
            letters+=k
            posdic[k] = index
            index += 1

    for i in range(ord("A"),ord("Z") + 1):
        if(i == ord("J")):
            continue
        if(chr(i) not in posdic):
            posdic[chr(i)] = index
            letters+=chr(i)
            index += 1

    pairs = list()
    i = 0
    while i < len(plain):
        if i == len(plain) - 1: # only last letter left
            if(plain[i] == "X"): # if the single letter is x append z
                pairs.append(("X","z"))
            else: # if last letter not x append x
                pairs.append((plain[i],"X"))
        elif plain[i] == plain[i+1]: # letter is same as next one
            pairs.append((plain[i],"X"))
        else:
            pairs.append((plain[i],plain[i+1]))
            i+=1
        i += 1

    def getitem(row,col):
        i = row * 5 + col
        return letters[i]
    def shiftright(row,col):
        return getitem(row,(col+1) % 5)
    def shiftdown(row,col):
        return getitem((row + 1) % 5,col)
    def encrypt(pair:tuple):
        row1 = posdic[pair[0]] // 5 # 0,1,2,3,4 will ll return 0 which is required
        col1 = posdic[pair[0]] % 5 # 0,5,10 all return 0 which is required
        row2 = posdic[pair[1]] // 5 # 0,1,2,3,4 will ll return 0 which is required
        col2 = posdic[pair[1]] % 5 # 0,5,10 all return 0 which is required
        ans = str()
        if row1 == row2:
            ans += shiftright(row1,col1)
            ans += shiftright(row2,col2)
        elif col1 == col2:
            ans += shiftdown(row1,col1)
            ans += shiftdown(row2,col2)
            pass
        else:
            ans += getitem(row1,col2)
            ans += getitem(row2,col1)
        return ans
    res = ""
    for i in pairs:
        res += encrypt(i)
    return res

def readFile(filename):
    file = open(filename, "r")
    ans = []
    for p in file.readlines():
        ans.append(p.replace("\n",""))
    return ans

def writeFile(filename, strlist):
    file = open(filename, "w")
    for st in strlist:
        file.write(st + "\n")
###################################################################################################
################################ hill functions ###################################################
###################################################################################################
alphabet = "abcdefghijklmnopqrstuvwxyz "
alphabet = alphabet.upper()
# print(alphabet)
letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


# function takes the letters and change them to numbers from 0-25
def to_numbers(alphabit):
    numbers_for_alphabit = []
    for letter in alphabit:
        if (letter_to_index.get(letter) != None):
            numbers_for_alphabit.append(letter_to_index.get(letter))
    return numbers_for_alphabit


# function takes the numbers and change them to letters
def to_letters(numbers):
    letters_for_numbers = []
    for number in numbers:
        if (index_to_letter.get(number) != None):
            letters_for_numbers.append(index_to_letter.get(number))
    return letters_for_numbers


# take a list and return it as a string
def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


def HillCipherEncrypt(plainText, key):
    # change text from string to numbers
    plainText = to_numbers(plainText)
    plainText = np.array(plainText)
    #plainText = np.transpose(plainText)
    #print(plainText)
    matrixMulti = np.dot(key, plainText,out=None)
    matrixMulti = matrixMulti % 26
    #print(matrixMulti)
    matrixMulti = to_letters(matrixMulti)
    #print(matrixMulti)
    encryptedmessage = listToString(matrixMulti)
    #print(encryptedmessage)
    return encryptedmessage


###################################################################################################
################################ Vigenere Cipher functions ########################################
###################################################################################################
# Vigenere Cipher function
def VigenereCipherEncrypt(message, key, auto):
    message = list(message)
    # from letter to numbers a-z--->0-25 for message
    numbers_for_message = to_numbers(message)
    # from letter to numbers a-z--->0-25 for key
    key = list(key)
    numbers_for_key = to_numbers(key)

    length = len(numbers_for_message)
    encrypt_message = []
    # auto=False then  we will repeat the key
    if auto == False:
        i_message = 0
        i_key = 0
        while (length != 0):
            if (i_key == len(numbers_for_key)):
                i_key = 0
            encrypt_message.append((numbers_for_key[i_key] + numbers_for_message[i_message]) % 26)
            i_key += 1
            i_message += 1
            length -= 1
        encrypt_message = to_letters(encrypt_message)
        return encrypt_message
    # auto=True then  we will concatenate the key with the plaintext
    else:
        i_message = 0
        i_key = 0
        i_continue = 0  # when i_key=length of the key array we start from 0 in the message array
        while (length != 0):
            if (i_key < len(numbers_for_key)):
                encrypt_message.append((numbers_for_key[i_key] + numbers_for_message[i_message]) % 26)
            elif (i_key == len(numbers_for_key)):
                encrypt_message.append((numbers_for_message[i_continue] + numbers_for_message[i_message]) % 26)
                i_continue += 1
            else:
                encrypt_message.append((numbers_for_message[i_continue] + numbers_for_message[i_message]) % 26)
                i_continue += 1
            i_key += 1
            i_message += 1
            length -= 1
        encrypt_message = to_letters(encrypt_message)
        return encrypt_message


###################################################################################################
################################ Vernam Cipher functions ##########################################
###################################################################################################
def VernamCipherEncrypt(message, key):
    if (len(key) != len(message)):
        print("key length must be the same as message length")
        exit()
    # change message and key frmo letters to numbers
    message = to_numbers(message)
    key = to_numbers(key)
    #print("message:", message)
    #print("key    :", key)
    encrypted_message = []
    for i in range(len(message)):
        encrypted_message.append((message[i] + key[i]) % 26)
    #print("encrypt:", encrypted_message)
    return listToString(to_letters(encrypted_message))


###################################################################################################
#########################################  main  ##################################################
###################################################################################################
def main():


    file1 = readFile("caesar_plain.txt")
    count = 0
    allCiphers = []
    allCiphers.append("------------------------------------Caesar Cipher Cipher ------------------------------------")
    for line in file1:
        text = line
        allCiphers.append("-------plain text: {}--------".format(line.strip()))
        shift = [3, 6, 12]
        for i in range(len(shift)):
            allCiphers.append("Shift       : " + str(shift[i]))
            cipherText = CaesarCipherEncrypt(text, shift[i])
            allCiphers.append("Cipher text : " + cipherText)
        count+=1
        print("\n")
        allCiphers.append("\n")
        writeFile("caesar_encrypted.txt", allCiphers)




    # key for playfair
    #print("------------------------------------playFair Cipher ------------------------------------")
    """print("--------------------------------------------------------")
    #playFairKey=input("please enter playfair key for encryption : ")
    #playFairEncrypt(text,playFairKey)"""
    plains = readFile("playfair_plain.txt")  # playfair
    keys = ["RATS", "ARCHANGEL"]
    ciphers = []
    #ciphers.append(makeSquare())

    for k in keys:
        #ciphers.append(playFairEncrypt(plains, keys))
        ciphers.append("key: " + str(k))
        for p in plains:
            ciphers.append(playfair(p, k))
        ciphers.append("\n")
    writeFile("playfair_cipher.txt", ciphers)




    # hill cipher 2x2
    #print("------------------------------------Hill Cipher 2x2 ------------------------------------")
    file1 = readFile("hill_plain_2x2.txt")
    allCiphers = []
    allCiphers.append("------------------------------------Hill Cipher 2x2------------------------------------")
    key_2 = [[5, 17], [8, 3]]
    allCiphers.append("default key matrix 2x2:{}".format(key_2))
    for line in file1:
        plainText = line
        allCiphers.append("plain text: {} ".format(line.strip()))
        chunk_of_2s=chunks(plainText,2)
        concate_all_cipher=""
        for i in chunk_of_2s:
            concate_all_cipher= concate_all_cipher+HillCipherEncrypt(i, key_2)
        allCiphers.append(concate_all_cipher)
        writeFile("Hill_2x2_encrypted.txt", allCiphers)




        # hill cipher 3x3
        # print("------------------------------------Hill Cipher 3x3 ------------------------------------")
    file1 = readFile("hill_plain_3x3.txt")
    allCiphers = []
    allCiphers.append("------------------------------------Hill Cipher 3x3------------------------------------")
    key = [[2 ,4 ,12],
                [9, 1, 6],
                [7 ,5 ,3]]
    allCiphers.append("default key matrix 3x3:{}".format(key))
    for line in file1:
            plainText = line
            plainText=Convert(plainText)
            plain_without_last_two_chars=""
            for i in range(len(plainText)-2):
                plain_without_last_two_chars=plain_without_last_two_chars+plainText[i]
            #print(plain_without_last_two_chars)
            begin=len(plainText)-2
            end=len(plainText)
            last_two=plainText[begin:end]
            allCiphers.append("plain text: {} ".format(line.strip()))
            chunk_of_3s = chunks(plain_without_last_two_chars, 3)
            concate_all_cipher = ""
            for i in chunk_of_3s:
                concate_all_cipher = concate_all_cipher + HillCipherEncrypt(i, key)
            concate_all_cipher = concate_all_cipher + HillCipherEncrypt(last_two, key_2)
            allCiphers.append(concate_all_cipher)
            writeFile("hill_3x3_encrypted.txt", allCiphers)


    # VigenereCipherEncrypt
    file1 = readFile("vigenere_plain.txt")
    allCiphers = []
    allCiphers.append("------------------------------------Vigenere Cipher------------------------------------")
    key="pie"
    key=key.upper()
    allCiphers.append("----------repeating mode----------\n")
    allCiphers.append("default key is   {}  for repeating mode".format(key))

    for line in file1:
        #print("------------------------------------Vigenere Cipher ------------------------------------")
        message = line.upper()
        #key = input("enter the key please:  ")
        #auto = int(input("do you want auto to be true or false? 1 for True, 0 for False: "))
        auto=0
        #print("auto:", auto)
        encrypted_message = listToString(VigenereCipherEncrypt(message, key, auto))
        allCiphers.append("Original message : " + message.lower())
        allCiphers.append("Encrypted message: {} \n".format(encrypted_message.lower()))
        #allCiphers.append("\n")
    key = "aether"
    key = key.upper()
    allCiphers.append("---------- auto mode----------\n")
    allCiphers.append("default key is   {}  for auto mode".format(key))

    for line in file1:
        # print("------------------------------------Vigenere Cipher ------------------------------------")
        message = line.upper()
        # key = input("enter the key please:  ")
        # auto = int(input("do you want auto to be true or false? 1 for True, 0 for False: "))
        auto = 0
        # print("auto:", auto)
        encrypted_message = listToString(VigenereCipherEncrypt(message, key, auto))
        allCiphers.append("Original message : " + message.lower())
        allCiphers.append("Encrypted message: {} \n".format(encrypted_message.lower()))
        # allCiphers.append("\n")

    writeFile("vigenere_encrypted.txt",allCiphers)




        # Vernam Cipher




    file1 = readFile("vernam_plain.txt")
    allCiphers = []
    allCiphers.append("------------------------------------Vernam Cipher ------------------------------------")
    key = "SPARTANS"
    allCiphers.append("default key :{} \n".format(key))
    for line in file1:
        message = line
        encrypted_message = VernamCipherEncrypt(message, key)
        allCiphers.append("Original message : " + message)
        allCiphers.append("Encrypted message: {} \n".format(encrypted_message))
    writeFile("vernam_encrypted.txt",allCiphers)

if __name__ == "__main__":
    main()