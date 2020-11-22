#example 1
"""
users_number = int(input("What is your number : "))
if users_number >= 0 :
  print(users_number)
else:
  print(-users_number)

"""

#example 2
"""
number_1 = int(input("number 1 : "))
number_2 = int(input("number 2 : "))
number_3 = int(input("number 3 : "))

if number_1 < number_2 and number_1<number_3:
  print(number_1)
elif number_2 < number_1 and  number_2<number_3:
  print(number_2)
else:
  print(number_3)
"""

#example 3
"""
gpa = float(input("what is your gpa ? :"))
num_of_lectures = int(input("what is your number of lectures :"))

if gpa < 2.0 and num_of_lectures < 47:
  print("not enough number of lectures and gpa")
elif gpa < 2.0 and num_of_lectures >=47:
  print("not enough gpa")
elif gpa >= 2.0 and num_of_lectures < 47:
  print("not enough number of lectures")
else:
  print("GRADUATED")
"""

#example 4
"""
age = int(input("what is your age? :"))
ticket = 3
if age < 6 or age > 60 :
  print("no ticket price FREE!!!")

elif age > 6 and age <18 :  
  print("%50 discount. your ticket price :",ticket*(1/2),"TL")
else:
  print("Ticket Price : ", ticket)
 """
#example 5
"""
month = int(input("month :"))
day = int(input("day :"))
total = month*30 + day
if total >= 80 and total < 171:
  print("spring")
elif total >= 171 and total < 262:
  print("summer")
elif total >= 262 and total <351:
  print("fall") 
else:
  print("winter")
"""
#example 6
"""
a = int(input("What is a in ax² + bx + c ? :"))
b = int(input("What is b in ax² + bx + c ? :"))
c = int(input("What is c in ax² + bx + c ? :"))
discriminant = b**2 - 4*a*c

if discriminant > 0:
  print("Discriminant = ",discriminant)
  print("There are 2 different real roots")
elif discriminant == 0:
  print("Discriminant = ",discriminant)
  print("There is one real root")
else:
  print("Discriminant = ",discriminant)
  print("There are 2 complex roots")
"""