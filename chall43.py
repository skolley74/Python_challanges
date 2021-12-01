# Ask a user which direction they want to count(up or down). If they select up, then ask them for the top number and
# then count from 1 to that number. If they select down, ask them to enter a number below 20 and then count down from
# 20 to that number. If they entered something else..display "i don't understand".

direction = input("which direction do you want to go up or down?")
if direction == "u":
    num = int(input("what is the top number:"))
    for i in range(0, num+1):
        print(i)
elif direction == "d":
    num = int(input("input number below 20:"))
    for i in range(20, num-1, -1):
        print(i)

else:
    print("i don't understand")
