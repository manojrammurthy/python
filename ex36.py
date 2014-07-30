from sys import exit
import random
import time

def stay(choice):
    print choice, "Thank You for not participating!"
    exit(0)
 
def gold_room():
    print "This room is full of gold.  How much do you take?"

    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        stay("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        stay("You greedy bastard!") 
          
def gomine():
    print "There are three rooms in the farm in one of the room there is gold  "
    print "and also there are dogs in the random room "
    print "\n one of the dog is aggressive be carefull"
    print "type 1 for room 1 , 2 for room 2, 3 for room 3"
    dog_moved = False
    
    while True:
        choice = raw_input("> ")
        
        if choice == "1" and not dog_moved:
            print "wait for some time dog might move "
            time.sleep(5)
            print "Dog didn't move you got bit by dog"
            stay("you have to rush to hospital")
            dog_moved = True
        elif choice == "2" :
            gold_room()
        else:
            print "You entered farm house" 
            stay("you may find some laptop's take and move")
             
def bus():
    print "since you took bus you are 3 mins late you have to do mathe to enter farm"
    list = ['1','2','3','7','8','9','10']
    var = int(random.choice(list))
    op = var * var
   # print op
    print " what is the out put of %d * %d" %(var,var)
    mulval =int(raw_input("> "))
    if mulval == op:
        print"your Math is correct"
        gomine()
    elif mulval > op:
        print "do you want to do math once again?"
        print "1 for yes"
        print "2 for no"
    choice = raw_input("> ")
    if "1" in choice:
        bus()
    else:
        print "Thank you for participating"
        exit(0)
            
def bike():
    print "You arrived at the right time"
    gomine()
    
def start():
    print "You are in kagglipura, you have to reach farmhouse in 12 mins"
    print "you have two options for travelling"
    print "enter 1 for bus"
    print "enter 2 for bike"
    
    choice = raw_input("> ")
    
    if choice == "1":
        bus()
    elif choice == "2":
        bike()
    else:
        stay("stay in kagglipura")
        
start()