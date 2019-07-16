mummy=int(input())
num=[int(i) for i in input().split()]
lst=[]
for i in range(0,len(num)):
  if i==num[i]:
    lst.append(num[i])
if len(lst)==0:
  print("-1")
else:
  for x in range(len(lst)): 
    print(lst[x],end=" ")
