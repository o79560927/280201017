#example 1
"""
inp = int(input("Enter an integer :"))
for i in range(1, 11):
    print(inp, "x", i, "=", inp * i)
"""
#example 2
""" 
n = 0
number = int(input("How many numbers will be :"))
for i in range(number):
  input_ = int(input("Enter a number :"))
  if input_%2 == 0:
    n = n+1

print((n/number)*100 )
"""

#example 3
"""
n1 = int(input("Enter the number pls : "))
n2 = int(input("Enter the number pls : "))
same = 0
while n1 > 0 and n2 > 0:
    if n1 % 10 == n2 % 10:
        same += 1
    n1 //= 10
    n2 //= 10
print(same)
"""
#example 4
"""
password = "abc123"

for i in range(4):
  guess = input("password :")
  if guess != password and guess != "help":
    print("wrong number")
  if guess == "help":
    print(password[0])
  if guess == password:
    print("correct")
    break;
  break;
 """
#example 5
"""
number = int(input("enter a number :"))
a = 1
b = 1
print(a)
print(b)
for i in range(number-2):
  c = a+b
  a = b
  b = c
  print(c)
"""