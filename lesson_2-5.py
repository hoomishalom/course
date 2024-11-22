import math

print("First Lesson!!")

# first of all the most important part of programing is *data*
# in python we have 4 basic data types str - String which is a data type for words or characters for example: "1", "a", "A1", "Tom", "Hi My Name Is Tom!"
#                                      int - Integer which is a data type for whole numbers for example: 1, 2, 3, 0, -1, -3213123, 32131231
#                                      float - Floating Point Number is a data type for decimal numbers for example: 0.1, -0.1, 1.1, 321312.231312
#                                      bool - Boolean which is a binary data type which its state is True or False 



# print()
# the print() function is the most important function in all of python because it's our way as programmers to display data to the user or to ourselves for debuging reasons 

def print_exm():
    print(1)

    print("a")

    print("Hi My Name Is Tom" + " " + "And I'm 16 Years Old!")

# print_exm()


# input()
# the input() function is a way to get data from the user the data will always be of the string type

def input_exm():
    name = input("what is your name?: ")
    print("name = " + name) 

    age = input("how old are you?: ")
    print("age = " + age) 

    sentence = "hi " + name  + " you are " + age + " years old"
    print("sentence = " + sentence)

# input_exm()


# str - String

def str_exm():
    a = "Hi My Name Is Tom"
    print("a = " + a) 

    b = "And I'm 16 Years Old!"
    print("b = " + b) 

    c = a + b       # adding two strings will combine them without a space in between
    print("c = " + c) 

    d = a + " " + b # we can solve the problem from before by adding another string which only contains a space
    print("d = " + d) 

# str_exm()


# int - Integer

def int_exm():
    a = 10     # declartion of an integer
    print("a = " + str(a))  
    b = -10    # integers can be negative
    print("b = " + str(b))  
    c = a + b  # integers can be manipulated by math
    print("c = " + str(c))  

# int_exm()


# float - Floating Point Number

def float_exm():
    a = 1.1    # declration of a float
    print("a = " + str(a))

    b = -1.1   # floats can be negative
    print("b = " + str(b))

    c = a + b  # floats can be manipulated by math
    print("c = " + str(c))

    d = 1.0    # a float can also be an integer
    print("d = " + str(d))

# float_exm()


# bool - Boolean

def bool_exm():
    a = True   # booleans have two states True or False
    print("a = " + str(a))

    b = False  # booleans have two states True or False
    print("b = " + str(b))

    c = not a  # a boolean's state can be toggled by the *not* keyword
    print("c = " + str(c))
    
    d = not b  # a boolean's state can be toggled by the *not* keyword
    print("d = " + str(d))

    e = 1 == 1 # you can compare two variabels and in return you get a boolen (True if the variables are equal and False if they are not equal)
    print("e = " + str(e))

    f = 1 != 1 # the opposite of *==* returns True if the variables are not equal and False if they are equal
    print("f = " + str(f))

    g = 2 > 2  # the bigger then operator *>*
    print("g = " + str(g))

    h = 2 >= 2 # the bigger then or equal operator *>=*
    print("h = " + str(h))

# bool_exm()


# math - math annotation in python

def math_exm():
    b = 1 + 1           # addition
    print("b = " + str(b))

    c = 2 - 1           # subtraction
    print("c = " + str(c))

    d = 2 * 2           # multiplaction
    print("d = " + str(d))
    
    e = 5 / 2          # division with reminder
    print("e = " + str(e))
    
    f = 5 // 2          # division without reminder
    print("f = " + str(f))
    
    g = 2 ** 2          # 2 raised to the power of 2
    print("g = " + str(e))

    h = math.sqrt(4)    # the square root of 4
    print("h = " + str(f))

# math_exm()


# math tips

def math_tips_exm():
    a = 1
    print("a = " + str(a))
    a += 1  # fast addition
    print("a = " + str(a))

    b = 2
    print("b = " + str(b))
    b -= 1  # fast subtraction
    print("b = " + str(b))

    c = 2
    print("c = " + str(c))
    c *= 2  # fast multiplication
    print("c = " + str(c))

# math_tips_exm()

