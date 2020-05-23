# Variables
#Single Assignment of Variable
name = "John"
#Printing Variable with print()
print(name)

friend = "Tom"
#String concatenation
print(name + "'s friend is " + friend)
#Assigning multiple variables with single value
x = y = z = 10
print(x)
print(y)
print(z)
#Assigning multiple variables with different values
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)
#Valid Syntax For Variable Names
_nam_ = "Joe"
print(_nam_)
#Invalid Syntax For Variable Names
#.name = "Joe"
#1name = "Joe"
#Using 'global'keyword to make a variable change at global scope if reassigned inside a function or control flow loops
var = "Johnnie"


def hey():
    global var
    var = "Tommy"
    print(var)

hey()
print(var)

#Video is ending here
#today exercise for you is to make a simple program to store celsius temperature and convert it to fahrenheit temperature
#the solutions will be posted on github repo so you can check after completing the task
