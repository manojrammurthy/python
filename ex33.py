#i = 0
numbers = []
def recu(var):
    i = 0
    while i < var:
        print "At the top i is %d" % i
        numbers.append(i)
    
        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
     
        print "The numbers: "

print recu(6)
for num in numbers:
     print num 