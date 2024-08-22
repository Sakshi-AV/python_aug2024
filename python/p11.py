import math
input_number = int(input("Enter a number to check if it is perfect square"))
root_num = math.sqrt(input_number)
root_num = math.floor(root_num)
product = root_num * root_num
if product == input_number:
    print(input_number,'is a perfect square')
else:
    print(input_number,'is not a perfect square')