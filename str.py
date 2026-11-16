a = int(input("enter a number:"))
if(a < 0):
    print( a , "is negative number")
elif(a > 0):
    print(a , "is positive number")
else:
    print("number is zero")
if(a % 2 == 0):
    print(a, "is even number")
else:
    print(a, "is odd number")


marks = int(input("enter your marks:"))
if(marks >= 90):
    print("GRADE A")
elif(marks >= 80):
    print("GRADE B")
elif(marks >= 70):
    print("GRADE C")
elif(marks >=60):
    print("GRADE D")
else:
    print("GRADE F")



a = float(input("enter first number:"))
b = float(input("enter second number:"))
c = float(input("enter third number:"))
if(a >= b and a >= c):
    print(a , "is the largest number among" , b , "and" , c)
elif(b >= a and b >= c ):
    print(b, "is the largest number among", a , "and" , c)
else:
    print(c , "is the largest number among", a , "and" , c) 