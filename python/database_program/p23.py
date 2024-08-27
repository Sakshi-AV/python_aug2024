
def find_sum_of_odd_elements(numbers):
    sum = 0
    for i in range(numofreq-1):
           if i% 2 ==0:
                sum == numbers[i]
    return sum
numofreq = int(input("Enter the number of requests"))
numbers=[]
print("Enter the elements")
for i in range(numofreq):
        numbers.append(input() )
sum = find_sum_of_odd_elements(numbers)
if sum<0:
    print("Memory deallocated")
else:
    print("Memory allocated")


