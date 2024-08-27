
n = int(input('Enter input size: '))

student = dict()
print(f'Enter the {n} student roll no.s and names')
for i in range(n):
    id = int(input())
    name = input()
    student[id]=name

print('The input data is \n', student)
search_id = int(input('Enter the search id.: '))

try:
    name = student[id]
    print(f'Student with id {search_id} was found at position {student[id]}')
except KeyError:
    print(f'Student with {search_id} was not found in the list')


    