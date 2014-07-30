from sys import exit

def gold_room():
    print "This room is full of gold . How much do you take?"
    
    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
         how_much = int(choice)
    else:
        dead("Man, learn to type number.")
        
    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")
        
def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "the fat bear is in front of another door"
    print "How are you going to move the bear?"
    print "Enter 1 to take honey, 2 taunt bear when bear is there, 3 to taunt when bear is moving, 4 to open door when bear is moving." 
    bear_moved = False
    
    while True:
        choice = raw_input("> ")
        
        if choice == "1":
            dead("The bear looks at you then slaps your face off")
        elif choice == "2" and not bear_moved:
            print "The bear has moved from the door. you can go through it now."
            bear_moved = True
        elif choice == "3" and  bear_moved:
            dead("The bear gets pissed off and chews your leoff.")
        elif choice == "4" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means." 
def cthulhu_room():
    print "Here you see the grear evil cthulu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"
     
    choice = raw_input("> ")
    
    if "flee" in choice:
           start()
    elif "head" in choice:
        dead("well that was tasty!")
    else:
        cthulhu_room()
        
def dead(why):
    print why, "good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "which one do you take? typr 1 for left and 0 for right"
    
    choice = raw_input("> ")
    
    if choice == "1":
        bear_room()
    elif choice == "0":
        cthulhu_room()
    else:
        dead("You stumble arround the room until you starve:")
start()

    
              