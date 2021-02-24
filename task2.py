#!python3

"""
Create a variable that contains an empy list.
Ask a user to enter 5 words.  Add the words into the list.
Print the list
inputs:
string 
string
string
string
string

outputs:
string

example:
Enter a word: apple
Enter a word: worm
Enter a word: dollar
Enter a word: shingle
Enter a word: virus

['apple', 'worm', 'dollar', 'shingle', 'virus']
"""

inp1=input("Enter a word: ")
inp2=input("Enter a word: ")
inp3=input("Enter a word: ")
inp4=input("Enter a word: ")
inp5=input("Enter a word: ")
words=[]
words.append(inp1)
words.append(inp2)
words.append(inp3)
words.append(inp4)
words.append(inp5)
print(str(words))