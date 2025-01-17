# import calendar
# year = int(input("enter the year: "))
# month = int(input("enter the month: "))
# print(calendar.month(year,month))

# import calendar
# year = int(input("enter the year: "))
# print(f"The calendar of the year {year} is {calendar.calendar(year)}")

# import calendar
# year = int(input("enter the year:"))
# for i in range(1,13):
#     month = i 
#     print(calendar.month(year,month))

import calendar
year = int(input("enter the year: "))
for i in range(1,13):
    month= i
    if i % 2 == 0:
        print(f"The even months of year {year} are {calendar.month(year,month)}")