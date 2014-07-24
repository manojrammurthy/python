from sys import argv
script, filename= argv

txt = open(filename)

print "now we will read the file"
print txt.read()