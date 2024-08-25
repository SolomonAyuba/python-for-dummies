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



print(topic_sep)