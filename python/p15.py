 # Program to assume 1 and 2 are 1st 2 terms of the series and print the 1st n term of Fibonacci series

number = int(input("Enter number to print Fibonacci series"))
number1,number2 = 1,2
if number <= 0:
    print("Enter a positive number")
else:
    print("Fibonacci Series",number1,number2,end=" ")
    for i in range(2,number):
        number3 = number1 + number2
        number1 = number2
        number2 = number3
        print(number3, end=" ")
