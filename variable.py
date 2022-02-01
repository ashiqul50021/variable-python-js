#variable are containers for storing data values

#creating a variable
#python has no command to create a variable
#A variable is created the moment you assing a value to it

x= 5
y = "John"
print(x)
print(y)

#variable do not need to be declared with perticular type, and can even change type after they have been set.
x = 4
x  = "Sally"
print(x)

# casting
#casting is the process of changing the type of data stored in a variable
x = str(3)
y = int(2.9)
z = float(2)

#get the type
#you can get the data type of a variable with the type() function
x = 5
y = "john"
print(type(x))
print(type(y))

#single or double quotes
#string variables can be declared either by using single or double quotes

x = " john"
#is hte same as 
y = 'john'

#the will create two variables
a = 4
A = "sally"

#assign multiple variables
#python allows you to assign multiple variables at once
x,y,z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#one value to multipel variables
#you can assign one value to multiple variables at once
x = y = z = "Orange"
print(x)
print(y)
print(z)

#unpack a collection
#if you have a collection of values in a list, tuple etc. python allows you to extract the values into variables. this is called unpacking

fruits = ["apple", "banana", "cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)

#output variables
#the python print statement is often used to output variables
#to combine both text and a variable, python uses the + operator
x = "awesome"
print("Python is " + x)

#you can also use the + character to add a variable to another variable
x = "Python is "
y = "awesome"
z = x + y
print(z)

#for numbers the +  character works as a mathematical operator
x = 5
y = 10
print(x + y)

#if you try to combine a string and a number, python will give you an error
#x = "awesome"
#y = "john"
print(x + y)

#global variables
#varible that are created outside of a function are known as global variables
#global variable can be used by everyone, both inside of functions and outside.
x = "awesome"
def myfunc():
    print("Python is " + x)
myfunc()

#if you create a variable with the same name inside a function, it is known as a local variable and can only be used inside that function. the global variable with the same name will remain as it was, global and with the original value.
x = "awesome"
def myfunc():
    x = "awesome"
    print ("Python is " + x)

    myfunc()
    print("Python is " + x)
#the global keyword
#normaly, when you create a variable inside a  function , that variable is local, and can only be used inside that function. 
#to create a global varible inside a function, you can use the global keyword. 

#if you use the global keyword, the variable belongs to the global scope:
def myfunc():
    global x
    x = "awesome"
myfunc()
print("Python is " + x)

#also, use the global keyword if you want to change a global variable inside a function
# to change the value of a global varialbe inside , refer to the variable by using the global keyword
x = "awesome"
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)

price = 21
age = 13
temp = 21

name = 'Swaroop'
addres = 'Bangalore'
phone = '1234567890'

passed = True
failed = False