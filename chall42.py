# Set total to 0. Ask a user to enter 5 numbers and after each input ask if they want that number included.
# If they do then add the number to the total. If they don't, do not include. After they have entered all
# 5 numbers, display the total.

total = 0
for i in range(0, 5):
    num = int(input("Enter a number:"))

    ans = input("Do you want this number to be included? (Y/N)")
    if ans == "y":
        total = total + num
print(total)
