# Program to reverse a number

number = int(input("Enter a number to find reverse of it"))
reverse = 0
while number!=0:
    remainder = number % 10
    reverse = reverse * 10 + remainder
    number = number//10
print("Reverse of a number is", reverse)

