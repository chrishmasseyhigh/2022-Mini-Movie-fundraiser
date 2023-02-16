#functions go here
# checks the amount of rounds and activate infine mode if user enters enter
def check_rounds(question):
    while True:
        # ask for round amount

        response = input(question)

        # error
        round_error = "Please enter an intiger that is more than zero"
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue
            except ValueError:
                print(round_error)
                continue

        return response


#main rotine
tickets=0
max_tickets= check_rounds("what is the max tickets? ")
while tickets<max_tickets:

    name = input("please enter your name or xxx to quit: ")
    print(name)
    if name =="xxx":
        break

    else:
        tickets +=1
        print(tickets)

if tickets == max_tickets:
    print("congratulations on selling all the tickets ")
else:
    print("You have sold {} ticket/s there are {} ticket/s remaning".format(tickets, max_tickets- tickets))