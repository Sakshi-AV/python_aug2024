# Program to find factorial using recursive function

def factorial(number):
    if number == 1:
        return 1
    else:
        return (number * factorial(number - 1))
    
number = int(input("Enter a number to find factorial of it"))
print("Factorial of",number,"is",factorial(number))
