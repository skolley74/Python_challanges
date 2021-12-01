# Ask how many people a user wants to invite to a party. If they enter a number below 10, ask for the names and after
# each name display "name has been invited". If they enter more than 10, display the message "too many people"

num = int(input("How many people do you want to invite:"))
if num < 10:
    for i in range(0, num):
         name = input("enter name:")
         print(name, "has been invited")

else:
    if num > 10:
        print("too many people")

