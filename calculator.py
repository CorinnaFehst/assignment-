def multiply (a,b):
    return a * b

def divide (a,b):
    return a / b

def add (a,b):
    return a + b

def subtract (a,b):
    return a - b

print "I'm going use the calculator functions to multiply 5 and 6"
x = multiply(5,6)
print x

def square (a):
    return a ** 2

def cube (a):
    return a ^ 3

def square_n (a,n):
    return a ** (n * 2)

print "I am going to use the square function to square the number 4"
x = square (4)
print x

print "I am going to use the square_n function to square the number 4 3 times"
x = square_n (4,3) 
print x
