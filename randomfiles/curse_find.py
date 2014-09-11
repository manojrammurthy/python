import urllib
def read_word():
    quotes = open("/home/lenovo/Desktop/hello")
    read1 = quotes.read()
    #print (read1)
    quotes.close()
    curse_word(read1)

def curse_word(question):
    url = "http://www.wdyl.com/profanity?q="
    connect = urllib.urlopen(url+question)
    output = connect.read()
    #print (output)
    connect.close()
    if "true" in output:
        print"Profanity alert"
    elif "false" in output:
        print"your text is good to go "
    else:
        print"could not scan the document properly"
        
read_word()