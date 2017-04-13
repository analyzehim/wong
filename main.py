import glob, os, time
import matplotlib.pyplot as plt
from book_proto import Book
import numpy as np



#os.chdir("data")
timestamp = time.time()
for file in glob.glob("data/*s.txt"):
    book = Book(file)
    print book.name
    print "           Page count: ", book.page_count
    print "           Word count: ", book.word_count
    print "           Unic count: ", book.unic_count
    #array = appr(book.array)
    count = 0
    number = 0
    for word_count in book.array:
        number += 1
        count += word_count
        if float(count)/float(book.unic_count) > 0.75:
            print "           ",number, "/", book.page_count
            break
    '''
    y = book.array
    x = [i for i in range(len(y))]
    plt.plot(x,y)
    plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), label = book.name)
    '''


    #plt.plot(array)
print time.time() - timestamp
plt.show()



