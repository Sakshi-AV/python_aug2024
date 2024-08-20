# Read a number from the user and check a number is even or not

my_number=(input("Enter a number to check if it is even or not")) 
if my_number % 2 ==0:
    print(my_number," is an Even number")
else:
    print(f"{my_number}is not an even number")