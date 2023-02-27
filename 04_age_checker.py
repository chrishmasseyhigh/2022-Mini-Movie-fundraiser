# functions go here

def num_check(to_check):
    
    while True:
        
        try:
            response = int(to_check)
            return response
        
    
        except ValueError:
            print('Please enter an integer')


def age_checker(question):
    while True:
        response = input(question)

        if response == "xxx":
            return response
        
        num_check(response)
        
        if 12 < response <= 120:
            return response
        elif response <= 12:
            print("You are too young for this movie")
            continue

        else:
            print("??that looks like a typo please try again??")
            continue


# main routine
while True:
    age = age_checker("what is your age xxx to quit: ")
    
    if age =="xxx":
        break