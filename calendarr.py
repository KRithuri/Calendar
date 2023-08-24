#import module
from calendar import *

#ask user for input
year = int(input("Enter year: "))

#print output to user
print(calendar(year,3,1,8,3))

#3 = characters for days
#1 = line for each row
#8 = rows for each month
#3 = columns of the month