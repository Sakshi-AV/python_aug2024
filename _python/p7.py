# Program to check if a number is perfect square

number=int(input("Enter a number"))
sqrt_number=int(number**0.5)
if sqrt_number**2==number:
    print("The number is perfect square")
else:
    print("The number is not a perfect square")