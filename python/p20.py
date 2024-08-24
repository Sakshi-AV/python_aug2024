# Program to count digits of a number

number = int(input("Enter a number to count the number of digits in it"))
count = 0
while (number > 0):
    count  = count +1
    num = number // 10
print(f'No of digits in {number} is {count}')