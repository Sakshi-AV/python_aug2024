# Accept a string of Pairs of Peranthesis and check if they are arranged properly. If so, print the number of pairs of peranthesis else print improper arrangement.
def check_arrangement(str):
    open = close = 0
    arrangement = True
    for char in str :
        if char =='(':
             open +=1
        else:
             close +=1
        if close > open:
            arrangement = False
            break 
    if arrangement and open == close:
        print("No. of pairs =",open)
    else:
        print("Improper arrangement")
str = input("Enter the string pairs of parenthesis")       
    
