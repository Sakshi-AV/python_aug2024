number_of_lines = int(input("Enter number of lines to draw the star shape"))
for i in range(1, number_of_lines+1):
    for j in range(1, number_of_lines+1):
        if j==1 or j== number_of_lines or i == j or j == number_of_lines-i+1:
            print('* ',end=" ")
        else:
            print("  ",end=' ')
    print()
    