# Ask user to enter a sentence and display the length of the sentence. Ask for a starting and ending number
# and display just that section of the text

phrase = input("I am from London")
length = len(phrase)
print ("this has ", length, "letters in it")
start = int(input("enter a starting number:"))
end = int (input("enter an ending number:"))
part = (phrase[start:end])
print(part)


