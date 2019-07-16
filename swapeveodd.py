a=input("")
n=len(a)
b=list(a)
for i in range(0,n+1):
  if(i%2!=0):
    b[i-1],b[i]=b[i],b[i-1]
d=""
for s in b:
  d+=s
print(d)
