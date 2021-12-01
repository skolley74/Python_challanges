# Ask a user to enter a number below 50 and then count down from 50 to that number, show the number they have entered
# in the output.

num = int(input("input a number below 50:"))
for i in range(50, num-1, -1):
    print(i)