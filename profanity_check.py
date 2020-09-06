import urllib.request
def read_file():
    file = open("D:\\new.txt")
    file_contents = file.read()
    #print(file_contents)
    check_profanity(file_contents)
    file.close()

def check_profanity(file_contents):
    file_contents = urllib.parse.quote(file_contents)
    connection = urllib.request.urlopen('http://www.wdylike.appspot.com/?q='+file_contents)
    if (connection.read().decode('utf8')) == 'true':
        print("Prtofanity alert!!!!!!!")
    else:
        print("All Clear")
    connection.close()


read_file()
