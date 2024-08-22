# Program to print right angled pattern

number = int(input("Enter a number to print right angled pattern"))
for i in range (1, number+ 1):
    for j in range(1, number + 1):
        if j<=i:
            print('*',end=" ")
        else:
            print('')
    print()

