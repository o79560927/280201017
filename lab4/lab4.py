# in LESSON
"""
a = -2
b = a**2 +1
c = b**3//2
d = c%b
print(a,b,c,d)

for i in range(1,7,3):
  print(i)

i = 1
best_soccer_players = ['ronaldo','messi','lewandowski','haaland']
for i in range((len(best_soccer_players))):
  print(best_soccer_players[i])
 
best_soccer_players = ['ronaldo','messi','lewandowski','haaland']
string = 'iyte'
for character in string:
  printtype(character)

print(type('a'))

best_soccer_players = ['ronaldo','messi','lewandowski','haaland']
for element in best_soccer_players:
  
  if element == best_soccer_players[1]:
    break
  else:
    print(element)
    
a_dict = {'color':'blue','furit':'apple'}
for key in a_dict:
  print(key)
"""
#example 1
"""
a = int(input())
one = a % 10
ten = a % 100 // 10
print(one+ten)
"""
#example 2
"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
nums = []
total = 0
nums.append(a)
nums.append(b)
nums.append(c)
nums.append(d)
for i in nums:
  total +=i
print(total)
print(nums)
"""

#example 3 
"""
a = int(input())
b = int(input())
d = 1
for i in range(b):
  d *=a
print(d)
"""

#example 4
""""
n =int(input("number : "))
total = 1
for i in range(1,n+1):
  total = total*i  
print(total)
"""