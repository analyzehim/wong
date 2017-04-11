
PUNCTUATION = '1234567890!@#$%^&*()_+-=<>?,./|'

def remove_puctuation(word):
    word = word.lower()
    for char in PUNCTUATION:
        word = word.replace(char, '')
    word = word.replace('\n', '')
    return word



f = open("data/Frankenstein.txt")
array = []
count = 0
for row in f:
    count += 1
    if count == 100:
        break
    array += row.split(' ')

for word in array:
    print remove_puctuation(word)