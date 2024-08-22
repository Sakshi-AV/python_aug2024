# Sum of digit of number

number = int(input("Enter a number to find sum of the digits "))
total = 0
while number > 0:
    total += number % 10
    number = number // 10
print("Sum of digits of", number," is",total)
