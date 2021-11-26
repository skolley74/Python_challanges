# Ask user for a name and number. Display their name a letter at a time on each time and repeate
# this for the number of times they entered.


num = int(input("please enter a number:"))
name = input("please enter your name:")
for x in range(0, num):

    for i in name:
        print(i)
