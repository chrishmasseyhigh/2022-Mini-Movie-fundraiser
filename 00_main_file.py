#functions go here

#check if the input matches 
def string_checker(question,num_letters,valid_response):
    
    error = "Please choose "
    
    for item in valid_response[:-1]:
        error += item
        error += " "
        
    error += "or "
    error += valid_response[-1]
    
    if num_letters ==1:
        short_version=1
    else:
        short_version=2
    
    while True:
        response=input(question).lower().strip()
        
        for item in valid_response:
            if response == item[:short_version] or response== item:
                return item
            
        print(error)
            
# Adds decoration above, below and before / after text
def statement_decorator(statement, decoration):
    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement,sides)
    top_bottom = decoration * len(statement)
    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""      
#calcuclates ticket price
def ticket_price_calculator(var_age):
    
    #calculates age to ticket price
    if var_age<=15:
        price = 7.5
    elif 15<var_age<=64:
        price =10.5
    
    else:
        price=6.5
    #returns calcualted price
    return price

#makes sure input is not blank
def not_blank(question):
    while True:
        response = input(question).strip()

        if response == "":
            print()
            print("sorry this result can't be blank")
            print()

        else:
            return response

#checks if it is a int
def num_check(to_check):
    
    while True:
        
        try:
            response = int(input(to_check))
            return response
        
    
        except ValueError:
            print('Please enter an integer')

#checks age
def age_checker(question):
    while True:
        response = num_check(question)
        
        if 12 <= response <= 120:
            return response
        
        elif response < 12:
            print("sorry you are too young")
            return "invalid"
                          
        else:
            print("oops - this looks like a typo <pretend you are a bit younger?>")
            return "invalid"
        

#main routine goes here

#sets lists for string checker
yes_no_list=["yes","no"]
payment_list=["cash","credit","debit","xxx"]

#sets tickets
tickets=0
max_tickets= 5

#asks for instructions
want_instructions = string_checker("Do you want to read the instructions? ",1,yes_no_list)

if want_instructions == "yes":
    print("instructions")

#gets users name and loops for ticket amount
while tickets < max_tickets:
    
    #gets name
    print()
    name = not_blank("Please enter your name or xxx to quit: ")
    print()
    statement_decorator("your name is {}".format(name),"(")
    print()
    if name =="xxx":
        break
    
    #gets age
    print()
    age= age_checker("what is your age? ")
    print()
    if age == "invalid":
        continue
    
    #caclulates ticket price
    ticket_price=ticket_price_calculator(age)
    t_price=f'your ticket price is ${ticket_price} '
    
    statement_decorator(t_price,"{")
    print()    
    
    #asks for payment method
    payment_method = string_checker("Payment method? cash / credit / debit (xxx to quit)? ", 2, payment_list)
    statement_decorator(payment_method,"-")
    print()
    if payment_method =="xxx":
        continue
    
    
    statement_decorator("enjoy the movie","*")
    
    #ups the ticket count
    tickets +=1
 

#sold all tickets
if tickets == max_tickets:
    print("congratulations on selling all the tickets ")

#tell you how many you have sold
else:
    ticket_info=f'You have sold {tickets} ticket/s there are {max_tickets-tickets} ticket/s remaning'
    print(ticket_info) 
    