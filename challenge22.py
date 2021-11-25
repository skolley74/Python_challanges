# Ask the user to enter their first name and surname in lower case. Change the case to title case and join them together
#Display rhe final results.

firstname = input("enter first name:")
surname = input ("enter your surname:")
firstname = firstname.title()
surname = surname.title()
fullname = firstname + " " + surname
print (fullname)