"""
users_number = int(input("What is your number : "))
if users_number >= 0 :
  print(users_number)
else:
  print(-users_number)

*************************************************************

number_1 = int(input("number 1 : "))
number_2 = int(input("number 2 : "))
number_3 = int(input("number 3 : "))

if number_1 < number_2 and number_1<number_3:
  print(number_1)
elif number_2 < number_1 and  number_2<number_3:
  print(number_2)
else:
  print(number_3)

*************************************************************
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
  *************************************************************

age = int(input("what is your age? :"))
ticket = 3
if age < 6 or age > 60 :
  print("no ticket price FREE!!!")

elif age > 6 and age <18 :  
  print("%50 discount. your ticket price :",ticket*(1/2),"TL")
else:
  print("Ticket Price : ", ticket)

 """
month = int(input("which month? :"))
day = int(input("which day* :"))

if month == 3 and day >=21  :

