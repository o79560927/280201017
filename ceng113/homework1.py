print("Enter the first equation:")  
first_input  = input()
print("Enter the second equation:")
second_input = input()

x1left  ,  y1left   ,   c1left    = 0,0,0 # Left and right means "side"
x1right ,  y1right  ,   c1right   = 0,0,0 # Left and right means "side"
x2left  ,  y2left   ,   c2left    = 0,0,0 # Left and right means "side"
x2right ,  y2right  ,   c2right   = 0,0,0 # Left and right means "side"

_1 = first_input.replace("+","!+").replace("-","!-")  #In this  point meanless, this will help us to split in next lines with("!")
_2 = second_input.replace("+","!+").replace("-","!-") #In this  point meanless, this will help us to split in next lines with("!")

denk1 =_1.split("=")[0].split("!")
denk2 =_1.split("=")[1].split("!")
denk3 =_2.split("=")[0].split("!")
denk4 =_2.split("=")[1].split("!")
denk1.remove("")
denk2.remove("")
denk3.remove("")
denk4.remove("")
for element in denk1:
  if element.count("x") != 0  : x1left += int(element[:-1])
  if element.count("y") != 0  : y1left += int(element[:-1])
  if element.count("y") == 0 and element.count("x") ==0 :  c1left += int(element)
for element in denk2:
  if element.count("x") != 0  : x1right += int(element[:-1])
  if element.count("y") != 0  : y1right += int(element[:-1])
  if element.count("y") == 0 and element.count("x") ==0 :  c1right += int(element)
for element in denk3:
  if element.count("x") != 0  : x2left += int(element[:-1])
  if element.count("y") != 0  : y2left += int(element[:-1])
  if element.count("y") == 0 and element.count("x") ==0 : c2left += int(element)
for element in denk4:
  if element.count("x") != 0  :   x2right += int(element[:-1])
  if element.count("y") != 0  :   y2right += int(element[:-1])
  if element.count("y") == 0 and element.count("x") ==0 : c2right += int(element)
x1,y1,c1 = (x1left-x1right),(y1left-y1right),(c1right-c1left) 
x2,y2,c2 = (x2left-x2right),(y2left-y2right),(c2right-c2left) 
for i in range(2,max(x1,y1,c1)):  
  if x1%i ==0 and y1%i == 0 and c1%i ==0 and x1 !=0 and y1 != 0:
    x1,y1,c1 = (x1/i),(y1/i),(c1/i)
for i in range(2,max(x2,y2,c2)):  #Reason of these 2 loops is make the equations more simply eg: instead of 2x + 2y = 4 it will show us x + y = 2
  if x2%i ==0 and y2%i == 0 and c2%i ==0 and x2 !=0 and y2 != 0:
    x2,y2,c2 = (x2/i),(y2/i),(c2/i)

x1,y1,c1,x2,y2,c2 = int(x1),int(y1),int(c1),int(x2),int(y2),int(c2) # To make sure that all variables are integer

print("Equations in the simplified form:")
if y1 >= 0  : y1 = "+{}".format(y1)
if y2 >= 0  : y2 = "+{}".format(y2)
simple_equation1 = "{}x{}y={}".format(x1,y1,c1)
simple_equation2 = "{}x{}y={}".format(x2,y2,c2)
print(simple_equation1)
print(simple_equation2)
x1,y1,c1,x2,y2,c2 = int(x1),int(y1),int(c1),int(x2),int(y2),int(c2)
if x1 == 0 and y2 == 0:     #To prevent zero divison error
  finalx = int(c2/x2)
  finaly = int(c1/y1)
elif x2 == 0 and y1 == 0:   #To prevent zero division error
  finalx = int(c1/x1)
  finaly = int(c2/y2)
else:  
  finaly = int((x2*c1 -x1*c2)/(x2*y1 -x1*y2))
  finalx = int((c1*y2-c2*y1)/(x1*y2-x2*y1))
print("Solution:")
print("x="+"{}".format(finalx))
print("y="+"{}".format(finaly))