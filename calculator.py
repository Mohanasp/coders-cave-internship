print("select an operation to perform")
print("1.ADDITION")
print("2.SUBTARCTION")
print("3.MULTIPLICATION")
print("4.DIVISION")

operation = input()

if operation == "1":
 num1=input("enter first number")
 num2=input("enter second number")
 print("addition of two numbers is" + str(int(num1) + int(num2)) )
elif operation == "2":
    num1=input("enter first number")
    num2=input("enter second number")
    print("subtraction of two numbers is" + str(int(num1) - int(num2)) )
elif operation == "3":
    num1=input("enter first number")
    num2=input("enter second number")
    print("multiplication of two numbers is" + str(int(num1) * int(num2)) )
elif operation == "4":
    num1=input("enter first number")
    num2=input("enter second number")
    print("division of two numbers is" + str(int(num1) / int(num2)) )
else:
    print("invalid entry")
    
