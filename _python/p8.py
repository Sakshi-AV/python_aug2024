#program to check if user given year is a leap year

year=int(input("Enter year"))
if year % 4 == 0 and year % 100 !=0 or year % 400 == 0:
    print(f'{year} is a leap year')