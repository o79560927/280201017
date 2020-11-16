"""
inp = int(input("Enter an integer :"))
for i in range(1, 11):
    print(inp, "x", i, "=", inp * i)
"""
number = int(input("How many numbers will be :"))
list = []
for i in range(number):
  input_ = int(input("Enter a number :"))
  if input_%2 == 0:
    list.append(input_)

print((len(list)/number)*100)