#we are passing a string with value 10 and assigning it to variable x
x = " There are %d types of people,"%10
# we are assigning a variable binary
binary = "binary"
#we are assigning a value to a variable do_not
do_not = "don,t"
#we are creating a variable y and assigning a string which takes other two variables as parameters inside the string
y = "Those who know %s and those who %s." % (binary,do_not)
#print the value of x
print x
#print the value of x
print y

#printing a string by passing the variable with % , here we have used %r which outputs the raw data
print "I said: %r." %x
# printing a string by passing a variable y
print "I also said: '%s'."%y

# declaring a variable hilarious and assigning a value false to it
hilarious = False
# declaring a variable with the carriage return %r in it
joke_evaluation = "Isn't that joke so funny?! %r"

# printing variable joke_evaluation and passing parameter hilarious as input to string
print joke_evaluation % hilarious

# declaring a variable w
w = "This is the left side of ..."
# declaring a variable e
e = "a string with a right side."

# printing the variable w and e concatinating them using + symbol
print w + e
