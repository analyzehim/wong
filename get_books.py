import urllib, glob, os


def download(count):
    for number in range(1, count):
        testfile = urllib.URLopener()
        URL = "http://www.gutenberg.org/cache/epub/{0}/pg{0}.txt".format(number)
        try:
            testfile.retrieve(URL, "download/{0}.txt".format(number))
        except IOError:
            print "Not Found ", number
        print URL, "OK"


def change_name(file_name):
    f = open(file_name, "r")
    count = 0
    title = ''
    author = ''
    for row in f:
        count += 1
        if "Title:" in row:
            title = row.split('Title:')[1][:-1]
        if "Author:" in row:
            author = row.split('Author:')[1][1:-1]

        if count == 1000:
            break
    f.close()
    name = "[{0}]{1}.txt".format(author, title)
    if name == '[].txt':
        os.remove(file_name)
        print "      delete"
    else:
        os.rename(file_name, "data/" + name)
        print "      rename {0}".format(name)

download(10)
for file_name in glob.glob("download/*"):
    print file_name
    try:
        change_name(file_name)
    except Exception as e:
        os.remove(file_name)
        print "      delete by error"


