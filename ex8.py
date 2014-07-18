# we are declaring a variable formatter with raw format descriptor
formatter = "%r %r %r %r"

# printing the variable formatter with variables
print formatter % (1,2,3,4)
# printing the variable formatter with variables
print formatter % ("one","two","three","four")
# printing the variable formatter with variables
print formatter % (True, False, False, True)
# printing the variable formatter with variables in formatter
print formatter % (formatter,formatter,formatter,formatter)
# printing the variable formatter with variables
print formatter % ( "I had this thing.",
                    "That you could type up right .",
                    "But it didn't sing.",
                    "So I said goodnight."
                    )