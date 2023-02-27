#functions go here
def not_blank(question):

     while True:
         response = input(question)

         if response =="":
             print("sorry this result can't be blank")

         else:
             return response


#main rotine checker goes here

while True:
    name = not_blank("please eneter your name or 'xxx' to quit ")

    if name=='xxx':
        break

print('we are done')