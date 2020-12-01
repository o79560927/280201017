'''
xvariables = []
soldigit = ['-','3','x']
for i in range(len(soldigit)):
  xvariables.append(soldigit[i])
  soldigit[i] = '!'
  if soldigit[i] == 'x':
    soldigit[i] = '!'
    break
print(xvariables)
print(soldigit)
'''
liste = ['!', '!', '!', '!',7,8, '!', '!', '!', '!', '!',6]
a = liste.count('!')
for i in range(a):
  liste.remove('!')
print(liste)




