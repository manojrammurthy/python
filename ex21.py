def add(a,b):
    print "ADDING %d + %d" % (a,b)
    return a + b
    
def subtract(a,b):
    print "SUBTRACTING %d - %d" % (a,b)
    return a - b

def multiply(a,b):
    print "MULTIPLYING %d * %d" % (a,b)
    return a * b
    
def divide(a,b):
    print "DIVIDING %d / %d" % (a,b)
    return a / b
    
print "lets do some math with just functions!"

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit , type it in anyway.
print "Here is a PUZZLE."
 
what = add(age, subtract(height, multiply(weight, divide(iq,
2))))
print " That becomes: ", what, "can you do it by hand?"
prompt = '>'
var1 = int(raw_input(prompt))
var2 = int(raw_input(prompt))
print "added value : %d" % add(var1,var2)

#permit =multiply(add((add(2,height), multiply(age, height)), add(subtract(weight,
#iq), divide(weight,2))))
#print "permit value : ", permit