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
"""
user_input = int(input("Your number :"))
for i in range(2,user_input):
  if user_input % i == 0:
    print(False)
    break;
  i = i+1
if i == (user_input-1):
  print(True)
"""
# Maximum number
"""
number_of_numbers = int(input("How many nmumber are there :"))
values = []
for i in range(number_of_numbers):
  user_number = int(input("Your number :"))
  values.append(user_number)
print("Largest value of your numbers :" , max(values))
"""
#Exercise 1
"""
low  = int(input("Low  :"))
high = int(input("High :"))
for i in range(low,(high+1)):
  print(i**2)
"""
#Exercise 2
"""
low  = int(input("Low  :"))
high = int(input("High :"))
summ = 0
for i in range(low,(high+1)):
  summ = summ + i
print(summ)
"""
#Exercise 3
"""
low  = int(input("Low  :"))
high = int(input("High :"))
for i in range(low,(high+1)):
  print(i)
"""
#Exercise 4
"""
low  = int(input("Low  :"))
high = int(input("High :"))
for i in range(low,(high+1)):
  for k in range(2,i):
    if i % k == 0:
      break;
  if k == (i-1):
    print(i)
"""
