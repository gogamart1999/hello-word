# 1)Write a Python program to get a string from a given string where all occurrences of its "r" char have been changed to '$'.
example: 'restart'
Result : '$esta$t'
course="restart"
print(course.replace("r","$"))


# 2)Write a Python program to swap comma and dot in a string. 
# Sample string: "32.054,23"
# Expected Output: "32,054.23"
price = "32.054,23"
price = price.replace('.',',')
print(price)

# 3) Write a Python program to compute sum of digits of a given string.
string = input("Enter any string: ")
sum_digit = 0
for x in string:
    if x.isdigit():
        sum_digit += int(x)
print("Sum of digits =", sum_digit)

# 4)Write a Python program to remove spaces from a given string.
print("Enter the String: ", end="")
str = input()
str = str.replace(" ", "")
print(str)

# 5)Write python program to print even length words in a string.
def printWords(s):
    s = s.split(' ') 
    for word in s:
        if len(word)%2==0:
            print(word) 
s = "I am Gohar" 
printWords(s) 

# 6)Write a program to count the number of letters in a word.
print("Enter the String: ", end="")
text = input()
textLen = len(text)
sum = 0
for i in range(textLen):
    sum = sum+1
print("" + str(sum))

# 7)Write a Python program to count the number of characters (character frequency) in a string.
# example:"hello world"
# output:
word = input("Enter a word")
from collections import Counter
counts=Counter(word) 
for i in word:
    print(i,counts[i])

# 8) Write a Python script that takes input from the user and displays that input back in upper and lower cases. 
user_input = input("Enter a word ")
print("Enter a word", user_input.upper())
print("Enter a word ", user_input.lower())

# 9)Write a Python script that has a list and convert into comma separated string.
# Sample list:['Geeks', 'for', 'Geeks']
# output:Geeks-for-Geeks
list_of_strings=[ 'Geeks', 'for', 'Geeks']
s='-'.join(list_of_strings)
print(s)

# 10)Python program to convert  starting letter of a word in upper case format or in the title format.
# sample list: ["hello", "this", "is", "pythonlobby"]
# output: Hello This Is Pythonlobby
sample = ["hello", "this", "is", "pythonlobby"]
sample= [i.title() for i in sample]
print('output')
print(sample)