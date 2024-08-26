# Crash course with freeCodeCamp https://youtu.be/rfscVS0vtbw

# 1. Babysteps: Using the Print Statement
print("hello world")

topic_sep = "=========================================="
print(topic_sep)

# Drawing a Shape
print("     /|")
print("    / |")
print("   /  |")
print("  /___|")

print(topic_sep)

# Variables and Datatypes
character_name = "Sowl"
character_age = 19
is_male = True
print("There once was a man named " + character_name + ", ")
print("he was " + str(character_age) + " years. ")
character_name = "Brown"
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + str(character_age) + ".")

print(topic_sep)

# Working with Strings
phrase = "Sowl Brown's\n\"Python for Dummies\""
print(phrase.upper() + " is a game changer")
print(phrase.lower() + " is a game changer")

print(phrase.isupper()) # change string case
print(phrase.isupper()) # check if phras string is lowercase
print(phrase.lower().islower()) # change string case and check if it's lowercase
print(len(phrase)) # length of string
print(phrase[0]) # print index of string. Python starts string index count at 0
print(phrase.index("o")) # prints index location of string
print(phrase.replace("Sowl", "WiseMan")) # replace string function

print(topic_sep)

# Working with Numbers
print(2, 2.097, -2, 3+2, 3/3, 3*2, 3*4+5, 3*(4+5), 10%3) # basic arithmetic
my_num = 5 # integer variable
print(my_num)
print(str(my_num)) # converting number to string
print(str(my_num) + " is my favourite number") # concatenating number and string

abs_num = -10
print(abs(abs_num)) # absolute value function
print(pow(2,6)) # power function
print(max(10,100)) # maximum number
print(min(10,100)) # minimum number function
print(round(3.456))  # round up function

from math import *  # importing external math function into out file
print(floor(33.7)) # round down
print(ceil(33.7))  # round up
print(sqrt(36)) # square root

print(topic_sep)

# Getting Input from Users
#name = input("Enter your name: ")
#age = input("Enter your age: ")
#print("hello " + name + "!, you are " + age)

print(topic_sep)

# Building a Basic Calculator
#num1 =  input("Enter a number: ")
#num2 =  input("Enter another number: ")
#result = int(num1) + int(num2) # whole numbers only
#print(result)

#um1 =  input("Enter a number: ")
#num2 =  input("Enter another number: ")
#result = float(num1) + float(num2) # decimal numbers
#print(result)

print(topic_sep)

# Mad Libs Game
#color = input("Enter a color: ")
#plural_noun = input("Enter a plural noun: ")
#celebrity = input("Enter a celebrity: ")

#print("Roses are " + color)
#print(plural_noun + " are blue")
#print("I love " + celebrity)

print(topic_sep)

# Lists
friends = ["Kevin", "Kloe", "Kim", "Kris", "Kagan", "klaus"]
print(friends)
friends[4] = "Kunle" # modifiy objects in the list.
print(friends[0]) # prints first object in the list
print(friends[-1]) # prints last object in the list
print(friends[1:]) # prints from second object to the last
print(friends[2:5]) #  prints range of elements

print(topic_sep)

# List Functions
lucky_numbers = [4, 8, 15, 16, 23, 42, 1, 0, 6]
friends = ["Kevin", "Kloe", "Kim", "Kris", "Kagan", "klaus", "Kunle", "NA", "NA", "NA"]
friends.extend(lucky_numbers) # append one list to another
friends.append("Konga") # append an object to the list's end
friends.insert(1, "kelly") # inset an object to a specific index in the list
friends.remove("Kim") #remove specific element on the list
#friends.clear() # clears entire list
friends.pop() # removes the last element in the list
print(friends)

print(friends.index("Kunle")) # checking if specific element is in the list.
print(friends.count("NA")) # counts the object's number of occurence

friends = ["Kevin", "Chloe", "Kim", "Cris", "Kagan", "Bobby", "Kunle"]
print(friends.sort()), print(friends) # sort list in alphabetical order
lucky_numbers.sort(), print(lucky_numbers)

print(friends.reverse()), print(friends) # Reverses the list's order.
lucky_numbers.reverse(), print(lucky_numbers)

friends2 = friends.copy()
print(friends2) # copies list to another variable

print(topic_sep)

# Tuples
# A type of data structure. A Container where we can save different values. Different from a list
coordinates = (4,5)
print(coordinates[0])
# Tuples vs Lists
# Tuples are immutable unlike lists
coordinates = [(4,5), (6,7), (80,43)]
print(coordinates[2])

print(topic_sep)

# Functions
def say_hi():
    print("Hello earthling, this is a function")

say_hi() #calling the function

def say_hi(name, age): # using parameters in function
    print("Hello " +name + " are you " + str(age) + "?")

say_hi("Jake", 22)
say_hi("Oba", 42)

print(topic_sep)

# Return Statement
def cube(num):
    return num*num*num

print(cube(3)) # print the return result

result = cube(2) # another way to print the return result
print(result)

print(topic_sep)

# If Statements
is_male = True
is_tall = True

if is_male or is_tall: # using logical OR
    print ("You're maybe a tall male")
else:
    print ("What're you?")

is_male = True
is_tall = True

if is_male and is_tall: # using logical AND
    print ("You're definetly a tall male")
else:
    print ("What're you exactly?")

# else if
is_male = True
is_tall = False

if is_male and is_tall:
    print ("You're a tall male")
elif is_male and not(is_tall):
    print("You're a short male")
elif not(is_male) and is_tall:
    print("You're some tall earthling ")
else:
    print ("What're you exactly?")

print(topic_sep)

# If Statements & Comparisons
def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3 :
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(41,41.1,41.12))

print(topic_sep)

# Building a better Calculator
#num1 = float(input("Enter first number: "))
#operator = input("Enter an operator: ")
#num2 = float(input("Enter second number: "))

#if operator == "+":
#    print(num1 + num2)
#elif operator == "-":
#    print (num1 - num2)
#elif operator == "*":
#    print(num1 * num2)
#elif operator == "/":
#    print(num1 / num2)
#else:
#    print("Invalid operator")

#print(topic_sep)

# Dictionaries
# A special structure in python which allows us to store information in what are called the Key Value Pairs

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions["Jan"])
print(monthConversions.get("Jul"))
print(monthConversions.get("Jab", "Not a valid key "))

print(topic_sep)

# While Loop
i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop")

print(topic_sep)

# Building a Guessing Game
#simple
# secret_word = "wiseman"
# guess = ""

# while guess != secret_word:
#    guess = input("Guess the secret word: ")

# print("You win! Secret word is \"" + secret_word + "\" ")

#advanced version
# secret_word = "wiseman"
# guess = ""
# guess_count = 0
# guess_limit = 4
# out_of_guesses = False

# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Guess the secret word: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True

# if out_of_guesses:
#     print("Sorry, you're out of guesses!")
# else:
#     print("You win! Secret word is \"" + secret_word + "\" ")

# print(topic_sep)

# FOR Loops
for letter in "The Alpha Univas LTD":
    print(letter)

friends = ["Bola", "Jake", "Toph"]
for friend in friends:
    print(friend)

for index in range(3, 10):
    print(index)

for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print(index, "First iteration.")
    else:
        print(index, "not first iterations")


print(topic_sep)

# Exponent Function
print(2**3)
#or
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(5, 3))

print(topic_sep)

# 2D Lists & Nested Loops

print(topic_sep)

#Building a Translator
print(topic_sep)

#Comments
print(topic_sep)

#Try / Except
print(topic_sep)

#Reading Files
print(topic_sep)

#Writing to Files
print(topic_sep)

#Modules & Pip
print(topic_sep)

#Classes & Objects
print(topic_sep)

#Building a Multiple Choice Quiz
print(topic_sep)

#Object Functions
print(topic_sep)

#Inheritance
print(topic_sep)

#Python Interpreter
print(topic_sep)


