def insertion_sort(array):
    for i in range(1,len(array)):
        element = array[i]
        j = i-1
        while j >= 0 and element < array[j]:
            array[j+1]=array[j]
            j = j - 1
        array[j+1] = element

n = int(input('Enter input size: '))

array = []
print(f'Enter the {n} elements')
for i in range(n):
    array.append(input())
print("Before sorting\n",array)
print("After sorting")
insertion_sort(array)