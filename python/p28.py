n = int(input("Enter the size of original list"))
original_list = []
print(f'Enter {n} elements to the original list')
for i in range(n):
    original_list.append(input())
m = int(input("Enter the size of transported list"))
transported_list = []
print(f'Enter {n} elements to the transported list')
for i in range(n):
    transported_list.append(input())

missing_list = []
j = 0
if m == 0:
    missing_list = original_list
else:
    for i in range(len(original_list)):
        if original_list[i] == transported_list[j]:
            j += 1
        else:
            missing_list.append(original_list[i])
        if j == m and i!= n-1:
            missing_list.extend(original_list[i+1:])
            break
print('Missing elements are: ', set(missing_list))
