PAGESIZE = 400
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
PUNCTUATION = '1234567890!@#$%^&*()_+-=<>?,./|'

def normalize(word):

    word = word.lower()
    for char in PUNCTUATION:
        word = word.replace(char, '')
    word = word.replace('\n', '')
    word = porter_stemmer.stem(word)
    return word


class Book:
    def __init__(self, file_name):
        self.name = file_name
        self.array = []
        self.word_count = 0
        self.unic_count = 0
        self.page_count = 0

        f = open(file_name, "r")
        wordset = set()
        temp_count = 0
        count = 0
        for row in f:
            row = ''.join([i if ord(i) < 128 else ' ' for i in row])

            if temp_count >= PAGESIZE:
                self.word_count += temp_count
                self.page_count += 1
                temp_count = 0
                self.array.append(count)
                count = 0

            for word in row.split(' '):
                    word = normalize(word)
                    temp_count += 1
                    if not word in wordset:
                        count += 1
                        wordset.add(word)

        self.unic_count = len(wordset)
        self.array.append(count)
        f.close()
        return