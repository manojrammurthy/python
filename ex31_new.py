print "there is a fire in the building escape out of it you have two options staircase, lift"

use = raw_input("> ")

if use == "1":
    print "you chose to use lift"
    print "select 1 for going to 4th floor"
    print "select 2 for going to groundfloor"
    
    floor = raw_input("> ")
    
    if floor == "1":
        print "you did the right job:"
    elif floor == "2":
        print "sorry lift just got broke down in between "
    elif floor >= "3" and floor <= "7":
        print "you have to take staircase from here"
    else:
        print "You'r Dead"
else:
    print "You'r safe"
    
            