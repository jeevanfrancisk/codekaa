my=int(input())
a=[int(x) for x in input().split()]
lst1=[]
for i in range(0,len(a)):
  if(i%2==0):
    if(a[i]%2!=0):
      lst1.append(a[i])
  else:
    if(a[i]%2==0):
      lst1.append(a[i])
for i in lst1:
  print(i,end=" ")
