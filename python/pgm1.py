import pdb
pdb.set_trace()

def find_factorial_iterative(num):
    factorial_number = 1
    if num == 0 or num == 1:
        return factorial_number
    for i in range(2,num+1):
        factorial_number = factorial_number * i
    return factorial_number
    

def find_factorial_recursive(num):
    if num == 0 or num == 1:
        return 1
    return num*find_factorial_iterative(num-1)

input_number = int(input("Enter a number to find factorial "))
choice = int(input("1. Iterative  2. Recursive \n Your choice is:"))

factorial_number = 0
if choice ==1:
    factorial_number = find_factorial_iterative(input_number)
else:
    factorial_number = find_factorial_recursive(input_number)

print(f'Factorial of {input_number} = {factorial_number}')
