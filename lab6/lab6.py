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

liste = []
for i in range(999999):
  a = random.randint(0,1)
  liste.append(a)

print('0:',liste.count(0))
print('1:',liste.count(1))