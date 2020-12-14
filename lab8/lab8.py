def summ(our_list):
  summation = 0
  for i in our_list:
    summation += i
  return summation**2

toplam = summ([1,2,3,4,5])
print(toplam)