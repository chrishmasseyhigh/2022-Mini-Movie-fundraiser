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
            
        
#main routine
yes_no_list=["yes","no"]
payment_list=["cash","credit","debit"]

having_fun = string_checker("Are you having fun? ", 1, yes_no_list)
print(having_fun)

payment_method = string_checker("Payment method? cash / credit / debit? ", 2, payment_list)
print(payment_method)