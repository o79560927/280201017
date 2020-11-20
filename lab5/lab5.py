"""
inp = int(input("Enter an integer :"))
for i in range(1, 11):
    print(inp, "x", i, "=", inp * i)

n = 0
number = int(input("How many numbers will be :"))
for i in range(number):
  input_ = int(input("Enter a number :"))
  if input_%2 == 0:
    n = n+1

print((n/number)*100 )

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
 
password = input("Enter your password : ")
password1 = input("Enter your password : ")

while password1 != password:
    print('Wrong')
    password1 = input("Please Enter Your Password Again : ")
    if password1 == 'help':
        print(password[0])
        break
if password1 == password:
    print("Welcome ")
"""
