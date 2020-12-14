#example 1
'''
def square_of_sum(our_list):
  summation = 0
  for i in our_list:
    summation += i
  return summation**2
toplam = square_of_sum([1,2,3,4,5])
print(toplam)
'''

'''
def sort_st_int(enter_list):
  str_list = []
  int_list = []
  for i in enter_list:
    if type(i) == str:
      str_list.append(i)
    elif type(i) == int:
      int_list.append(i)
  str_list.sort()
  int_list.sort()
  sorted_list = str_list + int_list
  return sorted_list
listemiz = [4,5,7,3,42,45,12,87,"d","a","b"]
sorted_listemiz = sort_st_int(listemiz)
print(sorted_listemiz)
'''
def prime(our_value):
  is_prime = []
  for i in range(2,our_value):
    if our_value%i == 0:
      is_prime.append(i)
  if is_prime != []:
    return "not prime"
  else:
    return "prime"

def all_prime_between(first,second):
  for i in range(first,second+1):
    is_prime = prime(i)
    if is_prime == "prime":
      print(i)

all_prime_between(10,56)