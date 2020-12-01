#example1
"""
inputlist = []
for _ in range(5):
  name = input("Enter name :")
  age = int(input("Enter age :"))
  person = (name,age)
  inputlist.append(person)

for name,age in inputlist:
  if age > 18:
    print(name)
"""
#example2
"""
books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict = dict()
for i in range(len(books)):
  key = books[i]
  character = len(key)
  unique_characters = len(set(key))
  value = (character,unique_characters)
  book_dict[books[i]] = value
print(book_dict)
"""
#example3
'''
books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict = dict()
for i in range(len(books)):
  key = books[i]
  character = len(key)
  unique_characters = len(set(key))
  average = (character+unique_characters)/2
  value = (character,unique_characters,average)
  book_dict[books[i]] = value
for i in book_dict:
  print(i,book_dict[i])
'''
#example4
'''
employee_dict = dict()
for k in range(2):
  name = input("What is the name of employee :")
  salary = int(input("What is the salary :"))
  employee_dict[name] = salary
name = ""
max_salary = 0
for i in employee_dict:
  if employee_dict[i] > max_salary:
    max_salary = employee_dict[i]
    name = i
  print(i,"--->",employee_dict[i])
print("highest salary = ",i,"with",max_salary,"$")
'''
"""
normalde a = herhangibirliste[index] dersen a yi oindexte ne varsa ona esitler
ama = herhangibirsozluk[key] dersen a yi parantezin icine yazdigin keyin valuesuna esitliyo
"""