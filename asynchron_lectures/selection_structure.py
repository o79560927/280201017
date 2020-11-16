
input_values = input("Please enter three values separeted with commas :")
x1,x2,x3 = input_values.split(',')
x1 = int(x1)
x2 = int(x2)
x3 = int(x3)

if x1 > x2 and x1 > x3:
  print("the largest value is :",x1)
elif x2 > x1 and x2 > x3:
  print("the largest value is :",x2)
else:
  print("the largest value is :",x3)



input_values = input("Please enter three values separeted with commas :")
x1,x2,x3 = input_values.split(',')
x1 = int(x1)
x2 = int(x2)
x3 = int(x3)

max_num = x1
if x2 > max_num:
  max_num = x2
if x3 > max_num:
  max_num = x3
print(max_num)

