# Write a program to swap two variables without using a third variable.
a = 5
b = 10
a, b = b, a
print(a,b)

# a = a+b  # 15
# b = a-b  # 5
# a = a-b
# print(a,b)
#........................................................................................

# Create a program that takes user input for name and age, then prints a formatted message using f-strings.
# name = input("enter your name ")
# age = int(input("enter you age "))
# print(f"your name is {name} and you age is {age}")
#.....................................................................................

# Write a program to check if a number is even or odd using modulo operator.
# number = int(input("enter your number "))
# if(number % 2 == 0) :
#     print("given number is even ")
# else :
#     print("given number is odd ")    
#............................................................................................

# Convert temperature from Celsius to Fahrenheit and vice versa.

# formulas c to f = (c*9/5)+32
# formulas f to c = (f-32)* 5/9
# temp1 = float(input("enter the temperature  "))
# conv_temp = (temp1 * 9/5) +32
# conv_temp1 = (temp1 -32) *5/9
# print("the temperature after converting  ",conv_temp1)
#..........................................................................................

# Check if a given string is a palindrome (case-insensitive).

# name = input("enter the name ") 

# name = "madam"
# rev = ""
# for val in name :
#     rev = val + rev
# print(rev)
# if(rev == name) :
#     print("string is palindrome")
# else :
#     print("not palindrome")  
#.................................................................................  

# Count the frequency of each character in a string using a dictionary.

# str = "ababeciifbhidasisvahs"
# count_dict = {}

# for ch in str:
#     count_dict[ch] = count_dict.get(ch,0) + 1

# print(count_dict)


# str1 = "ajhjjhdsjhhgjhsdjhgjhsdgjhgdjhfgjshgjshdgsdjhgsjh"
# dict1 = {}
# for i in str1 :
#     if i in dict1 :
#         dict1[i] += 1
#     else :
#         dict1[i] = 1    
# print(dict1)
#........................................................................................

# Write a program to format a string using all three formatting methods (%, .format(), f-strings).
# name = "abhay"
# age = 22
# print(f"your age is{age} and your name is {name}")
# print("your age is %d and your name is %s"%(age,name))
# print("your age is {0} and your name is {1}".format(age,name))

# Write a program to check if a year is a leap year.

# year = 2026
# if(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0 )) :
#     print("leap year ")
# else :
#     print("not leap year ")    
#...............................................................................

# Check if two strings are anagrams of each other.

str1 = "tea"
str2 = "eat"
if(str1.len)






# Create a CLI calculator that performs basic arithmetic operations based on user input with input validation.

n = int(input("enter the number of digits  "))
values = []
i = 1
while i <= n :
    a  = input("enter number ")
    values.append(a)
    i += 1
print(values)    
sum = 0
for i in values :
    i = int(i)
    sum = i + sum
print(f"the sum is {sum}")    



# 
