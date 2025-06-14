#Week 3 Exercise2: Data Types and Variables


#%% 1. Create a variable age and assign it the value 25.

age = 25
print(age)

#%% 2. Create a variable name and assign it a string containing your name.

name = "Avinash"
print(name)

#%% 3. Print the type of the variable age.

print(type(age))

#%% 4. Convert the variable age to a string and store it in a new variable age_str.

age_str = str(age)
print(type(age_str))

#%% 5. Create a variable height and assign it the value 175.5 (floating-point number).

height = 175.5
print(height)

#%% 6. Print the type of the variable height.

print(type(height))

#%% 7. Create a variable is_student and assign it a boolean value representing whether you are a student or not.

is_student = True 

#%% 8. Print the type of the variable is_student.

print(type(is_student))

#%% 9. Create a list colors containing the names of three colors.

colors = ['Red', 'Green', 'Blue']

#%% 10. Print the second element of the list colors.

print(colors[1])

#%% 11. Create a tuple dimensions containing the length, width, and height of a box.

dimensions = (5, 6, 7) # The length, width, and height of a box.

#%% 12. Print the third element of the tuple dimensions.

print(dimensions[2])

#%% 13. Create a dictionary person with keys "name", "age", and "city", and assign appropriate values.

person = {
    'name':'Avinash',
    'age':31,
    'city':'Pune'
    }

#%% 14. Print the value associated with the key "age" in the dictionary person.

print(person['age'])

#%% 15. Create a set unique_numbers containing three unique integers.

unique_numbers = {14, 8, 93}
print(unique_numbers)

#%% 16. Add a new integer to the set unique_numbers.

unique_numbers.add(92)
print(unique_numbers)


#%% 17. Create a variable x and assign it the value 10.

x = 10
print(x)

#%% 18. Increment the value of x by 5.

x = x + 5
print(x)


#%% 19. Create a variable y and assign it the value of x squared.

y = x**2 
print(y)

#%% 20. Swap the values of variables x and y.

print('x:',x)
print('y:',y)
x, y = y, x
print('After swap')
print('x:',x)
print('y:',y)

