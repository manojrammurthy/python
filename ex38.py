ten_things = "aPPLES oRANGES CROWS tELEPHONE lIGHT SUGAR"
print "Wait there's not 10 things in that list , lets fix  that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()# pop takes the last element from list
    print "Adding:",next_one
    stuff.append(next_one)# append adds the element at last
    print "There's %d items now." %len(stuff)
    
print "There we go :", stuff

print "let's do some things with stuff."

print "let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ''.join(stuff)
print '#'.join(stuff[3:5])
