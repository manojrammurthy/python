from sys import exit
stuff =  raw_input("> ")
words = stuff.split()
def convert_numbers(s):
    try:
        return int(s)
    except ValueError:
        return None
        