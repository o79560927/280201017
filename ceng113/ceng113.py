equation1 = str(input("Enter your first equation:"))

left_and_right_side_equation1 = equation1.split("=") 
left_side_equation1,right_side_equation1 = [],[] # left hand side of equation 1 and right hand side of equation 2
for _ in left_and_right_side_equation1[0]:
  left_side_equation1.append(_)
for _ in left_and_right_side_equation1[1]:
  right_side_equation1.append(_)
all_equation1 = left_side_equation1 + right_side_equation1
if left_side_equation1.count('y') + right_side_equation1.count('y') == 0:
  ###################################
  number_of_x = all_equation1.count('x')
  x_indexes = []
  start_index = 0
  value = ""
  for _ in range(number_of_x):
    x_indexes.append(all_equation1.index('x',start_index))
    start_index = all_equation1.index('x',start_index) + 1
  xinkatsayilari_liste = [[],[],[]]
  toplamx = 0
  for _ in range(len(x_indexes)): 
    b = x_indexes[_]
    a = all_equation1[b]
    while a != '+' and a != '-':
      b = b-1
      a = all_equation1[b]
      xinkatsayilari_liste[_].append(a)
    xinkatsayilari_liste[_].reverse()
    real_number = ""
    for i in xinkatsayilari_liste[_]:
      real_number = real_number+i
    
    toplamx += int(real_number)
  ################################### #'toplamx' sana x in katsayisini vericek
  for _ in range(number_of_x):
    all_equation1.remove('x')
  for _ in range(len(xinkatsayilari_liste)):
    for i in xinkatsayilari_liste[_]:
      all_equation1.remove(i)
  all_equation1.reverse()
  print(all_equation1)
  
  
#-8x-58x-8+59-71=+8+7x
#-8+59-71+8