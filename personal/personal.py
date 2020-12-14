my_list = ["x","x",6,9,"x"]
indexes = []
for i in range(0,len(my_list)):
  c = my_list[i]
  if  c == 'x':
    b = my_list.find(my_list[i])
    indexes.append(b)
print(indexes)
