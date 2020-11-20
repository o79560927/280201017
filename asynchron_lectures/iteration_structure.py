#For loops Example
"""
number_of_numbers = int(input("how many number you will enter? :"))
summ = 0
for i in range(number_of_numbers):
  number = int(input(str(i+1) + ". sayinizi girin : "))
  summ = summ + number
print(summ/number_of_numbers)
"""
#Trace Tables Example1
"""
for i in range(1,6):
  for i in range(1,(i+1)):
    print("*"*i)
  print("\n")
"""
#Trace Tables Example 2

user_input = int(input("Your number :"))

for i in range(2,user_input):
  if user_input % i == 0:
    print(False)
    break;
  i = i+1
if i == (user_input-1):
  print(True)


