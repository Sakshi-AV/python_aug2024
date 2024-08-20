# Program to accept three distinct numbers  and find smallest among them

input_num1 = int(input("enter 1st number :"))
input_num2 = int(input("enter 2nd number :"))
input_num3 = int(input("enter 3rd number :"))
if input_num1< input_num2 and input_num1< input_num3:
    print(input_num1,' is smallest')
elif input_num2< input_num3:
    print(input_num2,'is smallest')
else:
    print(input_num3,'is smallest')