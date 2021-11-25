# (1) ask user to enter an integer that is over 500. Work out the square root and display answer in
# 2 decimal places


import  math

num = int(input("input number over 500:"))
ans = math.sqrt(num)
# print ans first
print(ans)
# then round it to 2 dp
print(round(ans, 2))