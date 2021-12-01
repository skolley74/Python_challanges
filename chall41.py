# Ask a user to enter their name and a number. If the number is less than 10 , then display their name that number
# of times. Otherwise display the meaasge "too high" 3 times.

name = input("please inter your name:")
num = int(input("please enter a number:"))
if num < 10:
    for i in range (0, num):
         print(name)
else:
     for i in range(0, 3):
           print("too high")


