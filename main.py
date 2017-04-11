import glob, os
import matplotlib.pyplot as plt
from normalizer import *

CHARSET = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
           '(', ')', '!', ':', '?', '.', ',', '-', ';', '\n',
           ' ', '_', '\'', '\"'}

PAGESIZE = 70

def appr(array):
    res_array = [_ for _ in array]
    for i in range(len(array)-4):
        res_array[i+1] = float(array[i] + array[i+1] + array[i+2] + array[i+3] + array[i+4])/5.0
    return res_array




def normalize(word):
    word = word.lower()
    for char in CHARSET:
        word = word.replace(char, '')
    return word

class Book:
    def __init__(self, file_name):
        self.name = file_name
        self.array = []
        self.word_count = 0
        self.unic_count = 0
        count_str = 0
        f = open(file_name, "r")
        for row in f:
            count_str += 1
        f.close()
        PAGESIZE = count_str/50
        f = open(file_name, "r")
        wordset = set()
        temp_count = 0
        count = 0
        for row in f:
            temp_count += 1
            if temp_count == PAGESIZE:
                temp_count = 0
                self.array.append(count)
                count = 0

            for word in row.split(' '):
                    word = normalize(word)
                    self.word_count += 1
                    if not word in wordset:
                        count += 1
                        wordset.add(word)

        self.unic_count = len(wordset)
        self.array.append(count)
        f.close()
        return

os.chdir("data")
for file in glob.glob("*.txt"):
    book = Book(file)
    array = appr(book.array)
    plt.plot(book.array)
    #plt.plot(array)


plt.show()

