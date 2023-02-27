#functions

def ticket_price_calculator(var_age):
    
    if var_age<=15:
        price = 7.5
    elif 15<var_age<=64:
        price =10.5
    
    else:
        price=6.5
    return price
#main routine
age=int(input("age? "))

ticket_price=ticket_price_calculator(age)
t_price=f'your ticket price is ${ticket_price} '
print(t_price)