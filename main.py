import glob, os
import matplotlib.pyplot as plt
from book_proto import Book
import numpy as np

CHARSET = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
           '(', ')', '!', ':', '?', '.', ',', '-', ';', '\n',
           ' ', '_', '\'', '\"'}

PAGESIZE = 70


def normalize(word):
    word = word.lower()
    for char in CHARSET:
        word = word.replace(char, '')
    return word



#os.chdir("data")
for file in glob.glob("data/*.txt"):
    book = Book(file)
    print book.name
    print "           Page count: ", book.page_count
    print "           Word count: ", book.word_count
    print "           Unic count: ", book.unic_count
    #array = appr(book.array)
    y = book.array
    x = [i for i in range(len(y))]
    #plt.plot(x,y, 'ro')
    plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), label = book.name)


    #plt.plot(array)
plt.show()



