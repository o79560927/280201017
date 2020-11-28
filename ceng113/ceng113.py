user_input = str(input("Enter your first equation:"))
equation1 = user_input.split("=")
lhsofe,rhsofe = [],[]
for i in equation1[0]:
  lhsofe.append(i)
for k in equation1[1]:
  rhsofe.append(k)
if lhsofe.count('x') + rhsofe.count('x') == 0:
  




elif lhsofe.count('y') + rhsofe.count('y') == 0:




else:
  
#print(lhsofe[lhsofe.index('x')-2] + lhsofe[lhsofe.index('x')-1] + lhsofe[lhsofe.index('x')])
















# +2x-2y+5+4y=+18-1x