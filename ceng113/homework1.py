print("Enter the first equation:")  
first_input  = input()
print("Enter the second equation:")
second_input = input()
_1 = first_input.replace("+","!+").replace("-","!-")  #In this  point meanless, this will help us to split in next lines with("!")
_2 = second_input.replace("+","!+").replace("-","!-") #In this  point meanless, this will help us to split in next lines with("!")

main_list = [_1.split("=")[0].split("!")
            ,_1.split("=")[1].split("!")
            ,_2.split("=")[0].split("!")
            ,_2.split("=")[1].split("!")]

x1left  ,  y1left   ,   c1left    = 0,0,0 # Left and right means "side"
x1right ,  y1right  ,   c1right   = 0,0,0 # Left and right means "side"
x2left  ,  y2left   ,   c2left    = 0,0,0 # Left and right means "side"
x2right ,  y2right  ,   c2right   = 0,0,0 # Left and right means "side"

for side in main_list: 
  if side ==main_list[0]: #It gives x1left, y1left,c1left
    for element in side:
      if   element.count("x") != 0  : x1left += int(element[:-1])
      elif element.count("y") != 0  : y1left += int(element[:-1])
      elif element.count("y") == 0 and element.count("x") ==0 and element != "":  c1left += int(element)
  if side ==main_list[1]: #It gives x1right,y1right,c1right
    for element in side:
      if   element.count("x") != 0  : x1right += int(element[:-1])
      elif element.count("y") != 0  : y1right += int(element[:-1])
      elif element.count("y") == 0 and element.count("x") ==0 and element != "":  c1right += int(element)
  if side ==main_list[2]: #It gives x2left,y2left,c2left
    for element in side:
      if   element.count("x") != 0  : x2left += int(element[:-1])
      elif element.count("y") != 0  : y2left += int(element[:-1])
      elif element.count("y") == 0 and element.count("x") ==0 and element != "" :c2left += int(element)
  if side ==main_list[3]: #It gives x2right.y2right,c2right
    for element in side:
      if   element.count("x") != 0  :   x2right += int(element[:-1])
      elif element.count("y") != 0  :   y2right += int(element[:-1])
      elif element.count("y") == 0 and element.count("x") ==0 and element != "" :   c2right += int(element)

x1,y1,c1 = (x1left-x1right),(y1left-y1right),(c1right-c1left) 
x2,y2,c2 = (x2left-x2right),(y2left-y2right),(c2right-c2left) 

for i in range(2,max(x1,y1,c1)):  
  if x1%i ==0 and y1%i == 0 and c1%i ==0 and x1 !=0 and y1 != 0:
    x1,y1,c1 = (x1/i),(y1/i),(c1/i)
for i in range(2,max(x2,y2,c2)):  #Reason of these for loops is make the equations more simply eg: instead of 2x + 2y = 4 it will show us x + y = 2
  if x2%i ==0 and y2%i == 0 and c2%i ==0 and x2 !=0 and y2 != 0:
    x2,y2,c2 = (x2/i),(y2/i),(c2/i)

print("Equations in the simplified form:")
if y1 >= 0  : y1 = "+{}".format(y1)
if y2 >= 0  : y2 = "+{}".format(y2)
simple_equation1 = "{}x{}y={}".format(x1,y1,c1)
simple_equation2 = "{}x{}y={}".format(x2,y2,c2)
print(simple_equation1)
print(simple_equation2)

x1,y1,c1,x2,y2,c2 = int(x1),int(y1),int(c1),int(x2),int(y2),int(c2) # To make sure that all variables are integer
finaly = int((x2*c1 -x1*c2)/(x2*y1 -x1*y2))
finalx = int((c1 - y1*finaly)/x1)
print("Solution:")

print("x="+"{}".format(finalx))
print("y="+"{}".format(finaly))