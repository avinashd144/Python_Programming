# Week 2: Python Basic Exercises
# Provide the file including successfully executable codes for the following tasks:
    
#%% 1. Write a program that prints "Hello, World!" to the console.

print("Hello, World!")

#%% 2. Calculate the area of a rectangle given its length and width.

# Asking inputs from user
l = int(input("Input the length of rectangle in unit:"))
w = int(input("Input the width of rectangle in unit:"))
# Calculating the required area of rectangle 
A = l*w
# Printing area at output
print("Area of the rectangle in square unit:",A)


#%% 3. Convert temperature from Celsius to Fahrenheit and vice versa.

# Asking inputs from user
c = int(input("Input the temperature in Celsius:"))
# converting Celsius to Fahrenheit
f = c*1.8+32
print("temperature in Fahrenheit: ",f)

#
# Asking inputs from user
f = int(input("Input the temperature in Fahrenheit:"))
# converting Fahrenheit to Celsius
c = (f-32)/1.8
print("temperature in Celsius: ",c)

#%% 4. Create a list of numbers and print the sum of all the elements.

# Creating a list
l1 = list(range(100))
# Using sum function
#tot = sum(l1)

tot = 0
for i in l1:
    tot += i
print(tot)

#%% 5. Write a program to check if a given number is even or odd.

n = int(input("Input a given number:"))

if n%2 == 0:
    print("The given number is Even")
else:
    print("The given number is Odd")

    

#%% 6. Generate a random number between 1 and 100 and ask the user to guess it.

import random

r = random.randint(1,100)
g = int(input("guess a number between 1 and 100:"))
if g == r:
    print("Wow, you guessed it correctly")
else:
    print("No, it's not correct, try again!")
print(r)

#%% 7. Write a function to check if a given string is a palindrome.

def check_palindrome(string):
    # cleaning the string
    c_string = ''.join(char.lower() for char in string if char.isalnum())
    # checking palindrome
    if c_string == c_string[::-1]:
        #print("Given string is palindrome")
        return print(f'Given string "{string}" is palindrome')
    else:
        #print("Given string is not a palindrome")
        return print(f'Given string "{string}" is not a palindrome')
        
#string = "A mam an"
string = "A mam a"
check_palindrome(string)

#%% 8. Calculate the factorial of a given number.

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return  n * factorial(n - 1)
        
n = 5
ans = factorial(n)
print(f'The factorial of the given number is {ans}')

#%% 9. Write a program to find the largest element in a list.

def LargestNum(l):
    largest  = l[0]
    for i in l:
        if i > largest:
            largest = i
    return i

list1 = [10,20,30,40]
Largest_Num_In_List = LargestNum(list1)
print(f'The largest number in list is {Largest_Num_In_List}')


#%% 10. Create a simple calculator that can perform addition, subtraction, multiplication, and division.

# To perform addition
def addition(a,b):
    return print('addition of given numbers is: ', a+b)

# To perform subtraction
def subtraction(a,b):
    return print('subtraction of given numbers is: ', a-b)

# To perform multiplication
def multiplication(a,b):
    return print('multiplication of given numbers is: ', a*b)

# To perform division
def division(a,b):
    # To check if denominator is O
    if b == 0:
        return print('division by 0 is not valid')
    return print('multiplication of given numbers is: ', a/b)


addition(659,589)
subtraction(4587,4548)
multiplication(456,711)
division(1548,795)

    

#%% 11. Write a function to find the square root of a number using Newton's method.

def sqrtByNewtonsMethod(n, tol=1e-14):
    if n < 0:
        return 'squre root is not valid for negative numbers'

    # Initial guess
    guess = n
    
    while True:
        # For nearer guess to root
        guess_updated = 0.5 * (guess + n / guess)
        
        # To check the updated guess is within given tolerance
        if abs(guess_updated - guess) < tol:
            return guess_updated
        # now assigning guess by guess_updated
        guess = guess_updated
    return print(guess)

n = 625
sqrtByNewtonsMethod(n)

#%% 12. Reverse a given list without using the reverse() method.

def reverse(lst):
    list1 = []
    for i in range(len(lst) - 1, -1, -1):
        list1.append(lst[i])
    return list1

# Example usage
lst = [22, 33, 44, 55, 66]
list1 = reverse(lst)
print(f"Given list: {lst}")
print(f"Reversed list: {list1}")

#%% 13. Write a program to find all the prime numbers between 1 and 100.

def primeNumbersBet1_100():
    primes_list = []
    for i in range(2, 101):  # starting with 2 to exclude 1 from the list, and 2 is the first prime number
        for j in range(2, i):
            if i % j == 0:  
                break
        else:
            primes_list.append(i)
    return print(primes_list)

primeNumbersBet1_100()

#%% 14. Calculate the Fibonacci sequence up to a given number.

def Fibonacci(n):
    lst = [0, 1]
    while True:
        new = lst[-1] + lst[-2]
        if new > n:
            break
        lst.append(new)
    return print(lst)

Fibonacci(17)

#%% 15. Write a function to count the number of vowels in a given string.

def vowelsCount(string):
    vowels = "AaEeIiOoUu"
    tot = 0
    for i in string:
        if i in vowels:
            tot = tot + 1
    return tot

string = input("Enter a string to count vowels in given string: ")
vowelsCount = vowelsCount(string)
print(f"The number of vowels in the given string is: {vowelsCount}")

#%% 16. Check if a given year is a leap year.

def LeapYearCheck(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return print('The given year is leap year')
    else:
        return print('The given year is not a leap year')
    
LeapYearCheck(1900)  
#%% 17. Remove duplicates from a list without using sets.

def remove_duplicates(lst):
    final_list = []
    for i in lst:
        if i not in final_list:
            final_list.append(i)
    return final_list

lst = [3, 8, 6, 3, 8, 7, 6]
final_list = remove_duplicates(lst)
print(f"Given list: {lst}")
print(f"final list: {final_list}")

#%% 18. Write a program to sort a list of numbers using bubble sort.

def srt(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

num_list = [64, 34, 25, 12, 22, 11, 90]
srt(num_list)
print("New sorted list:", num_list)

#%% 19. Create a dictionary of names and ages, and print the name of the oldest person.

# dictionary of names and ages
names_ages = {
    "Raju": 17,
    "Balu": 15,
    "Sonu": 47,
    "Monu": 46,
    "Don": 46
}

# print the name of the oldest person.
oldest_person = max(names_ages, key=names_ages.get)
print(oldest_person)


#%% 20. Write a program to find the least common multiple (LCM) of two numbers.

import math as mt

def lcm(n1, n2):
    LCM = (abs(n1 * n2) // mt.gcd(n1, n2))
    return print('LCM of the given two numbers is:', LCM)

lcm(18, 27)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    