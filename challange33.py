# (1) Ask user to enter 2 numbers. Use whole number division to divide the first by the second.
# Work out the remainder and display the answer in the format e.g '7 divided by 2 is 3 with 1 remaining'

num1 = int(input("please enter num1:"))
num2 = int(input("please enter num2:"))
# whole number division
ans1 = num1 // num2
# mod or reminder
ans2 = num1 % num2
print(num1, "divided by", num2, "is", ans1, "with", ans2, "remaining")

