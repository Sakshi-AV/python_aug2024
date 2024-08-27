def binary_search(elements, search_element):
    while start_index <= end_index:
        mid_index = (start_index + end_index)//2
        if elements[mid_index]  == search_element:
            return mid_index
        elif search_element < elements[mid_index]:
            end_index = mid_index - 1
        else:
            start_index = mid_index +1
    return -1
start_index = int(input("Enter the start index"))
end_index = int(input('Enter end index: '))

elements = []
print(f'Enter the {end_index} elements in ascending order')
for i in range(end_index):
    elements.append(input())

print('The input data is \n', elements)
search_element = input('Enter the search element: ')

index = binary_search(elements, search_element)
if index == -1:
    print(f'{search_element} was not found in the list')
else:
    print(f'{search_element} was found at position {index+1}')