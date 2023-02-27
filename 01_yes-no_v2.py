#functions go here

#Yes or no checker
def yes_no(question):
    yes_ok = ["no","n","nope","nah"]
    no_ok = ["yes","y","yep","yea"]

    valid= False
    while not valid:
            response = input(question).lower().strip()
            #if they say yes, output 'program continues'
            if response in no_ok:
                return True
            #if they say no, output 'displays instructions'
            elif response in yes_ok:
                return False
            #else, output'Please enter yes or no'
            else:
                print()
                print("Please enter'yes or 'no/")
                print()

#main rotine goes here
want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions:
    print("instructions")
else:
    print("nope")
print()
print("program continues")
print()