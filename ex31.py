print "You enter a dark room with two doors. Do you go through door #1 or door #2" 

door = raw_input(">")

if door == "1":
    print "There's a gaint bear here eating a cheese cake.what do you do?"
    print "1. Take the cake."
    print "2. scream at the bear."
    
    bear = raw_input("> ")
    
    if bear == "1":
        print "The bear eats your face off, Good job!"
    elif bear == "2":
        print " the bear eats your legs off. Good job!"
    else:
        print "well, doing %s is probably better bear runs away." % bear
        
        insanity = raw_input("> ")
        
        if insanity == "1" or insanity == "2":
            print " your body survives powered by a mind of jello Good jb!"
        else:
            print " The insanity rots your eyes into a pool of muck. Goodjob!"  

else:
         print "You stumble around and fail on a knife and die Good job!"
          
        