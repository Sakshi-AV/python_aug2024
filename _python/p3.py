# Accept a number as input x and define a logic to get the output as y the input must be 0 or 1 and the output must be 1 if input is 0 and viceversa

x= int(input("Enter the number(0 or 1)"))
if x!=0 and x!=1:
    print("invalid input")
else:
    y=1-x
    print(f'input number={x},output number={y}')