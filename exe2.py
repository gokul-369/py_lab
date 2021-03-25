import math  #import the math module 
print("*****FACTORIAL*****")
a=int(input("enter the the number:"))
print("the factorial of the given number is", math.factorial(a))  #returns factorial of the given number 
print("\n")
print("*****ABSOLUTE VALUE*****")
b=int(input("enter the the number:"))
print("the absolute float value of the given number is", math.fabs(b))  #returns the absolute value 
print("\n")
print("*****MODULUS*****")
x = int(input("enter the the nominator:"))
y=int(input("enter the the denominator:"))
print("the modulus of the given number is",math.fmod(x,y)) #Returns the remainder when x is divided by y
print("\n")
print("*****SQUARE ROOT*****")
c=int(input("enter the the number:"))
print("the squareroot of the given number is", math.sqrt(c))  #returns the square root value 
print("\n")
print("*****pi value*****")
r=int(input("enter the the radius:"))
print("the area of the circle is", math.pi * r * r)  #returns the pi value(3.14) 
print("\n")
print("*****TRUNCATE*****")
d=int(input("enter the the number:"))
print("the truncate value of the given number is",math.trunc(d)) #returns the truncated integer value
print("\n")
print("*****SIN*****")
e=int(input("enter the the number:"))
print("the sine value of the given number is", math.sin(e))  #returns the sine value 
print("\n")
print("*****COS*****")
f=int(input("enter the the number:"))
print("the cosine value of the given number is", math.cos(f))  #returns the cosine value 
print("\n")
print("*****TAN*****")
g=int(input("enter the the number:"))
print("the tangent value of the given number is", math.tan(g))  #returns the tangent value 
print("\n")
print("*****INFINITY*****")
h=int(input("enter the the number:"))
print("the given number is",math.isinf(h)) #returns True if the given number is a positive or negative infinity
