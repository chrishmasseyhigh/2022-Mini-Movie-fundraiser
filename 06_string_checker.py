#Yes or no checker
def payment_method(question):
    cash_cash= ["cash","dollar","coin","bank notes","ca"]
    debit_card=["debit","debit card","debitcard","dc","de"]
    credit_card = ["credit","credit card","creditcard","cc","cr"]

    valid= False
    while not valid:
            response = input(question).lower().strip()
            #if they say yes, output 'program continues'
            if response in credit_card:
                return "credit card"
                
            #if they say no, output 'displays instructions'
            elif response in cash_cash:
                return "cash"
            
            elif response in debit_card:
                return"debit card"
            
            elif response =="c":
                print("!!'c' can mean cash or credit please enter a whole word like cash or dollar!!")
                cash_or_credit=input("cash or credit? ")
                
                if cash_or_credit in credit_card:
                    return"credit"
                
                elif cash_or_credit in cash_cash:
                    return "cash"
                else:
                    continue
                    
                
            #else, output'Please enter yes or no'
            else:
                print()
                print("Please enter 'cash' 'credit' or 'debit'")
                print()

#main routine
print()
test=payment_method("cash, credit or debit ")
print()
payment=f'you have chosen to pay with {test}'
print(payment)