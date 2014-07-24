from sys import argv

script, filename = argv

print "We re going to erase %r ." % filename
print " if you don't want that , hit CTRL-C (^C)/"
print "	If you do want that , hit RETURN. "
#rawinput takes the values entered either enter or CTRL +C
raw_input("?")
#opening the file and saving it in a variable with write mode
print "opening the file..."
target = open(filename,'w')
#truncate erase all the lines in the file
print "Truncating the file . Goodbye!"
target.truncate()
# it takes three values to write in a file
print "now I'm going to ask you three lines. "
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print " And finally , we close it. "
target.close()

