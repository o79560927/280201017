#example1
import random

"""
user_input = str(input("What is your e mail :"))
user_input.lower()
number_of_signs = user_input.count('@')

if number_of_signs == 1:
  a = user_input.split('@')
  email = a[0].replace(".","") + "@" + a[1]
  if email == "ceng113@example.com":
    print("yess")
  else:
    print("no")
else:
  print('please write valid e mail')
"""
#example2
"""
grades = []
number_of_students = int(input("Number of students :"))
for every in range(number_of_students):
  print("for the" , every+1 , ".student")
  midterm1 = int(input("midterm1 :"))
  midterm2 = int(input("midterm2 :"))
  final = int(input("final :"))
  grades.append([midterm1,midterm2,final])
for i in grades:
  avarage_grade = i[0]*0.3 + i[1]*0.3 + i[2]*0.4
  print("students grade =", avarage_grade) 
"""
#example3
"""
#[5, 91, 55, 20, 69, 19, 5, 20, 69, 78, 78]
#[91, 78, 69, 55, 20, 19, 5]
item_number = int(input("What is the number of items? :"))
user_item_list = []
for i in range(item_number):
  item = int(input("item:"))
  if user_item_list.count(item) == 0:
    user_item_list.append(item)
user_item_list.sort(reverse = True)
print(user_item_list)

"""
#example4
'''
input_number = int(input("Insert the number to build an identity matrix. "))
matrix = []
counter = 1
for x in range(input_number) :
  matrix = []
  for y in range(1, input_number + 1) :
    if y == counter :
      matrix.append(1)
    else :
      matrix.append(0)
  counter += 1
  print(matrix)
'''

#example5
'''
n = int(input("Matrix number: "))
string = ''
sum_list = []
for i in range(n):
    for j in range(n):
        number = int(input("Input number: "))

        if i == j:
            sum_list.append(number)
sum = 0
for i in sum_list:
    sum += i

print("Output: ", sum)
'''
