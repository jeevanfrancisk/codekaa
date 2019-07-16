dmy=int(input())
a=input("")
a=list(a.split(" "))
f=[]
for i in range(0,len(a)):
  for j in range(i+1,len(a)):
    if a[i]==a[j]:
      f.append(a[i])
if(len(f)==0):
  print("unique")
else:
  print(f[0])
