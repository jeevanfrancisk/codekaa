a,c=input("").split()
a1=list(a)
b1=list(c)
count=0
for i in range(0,len(a1)):
  if(a1[i]!=b1[i]):
    count+=1
if(count==1):
  print("yes")
else:
    print("no")
