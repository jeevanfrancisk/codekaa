a=input("")
a=list(a)
for i in range(0,len(a)+1):
  if(i%2!=0):
    a[i-1],a[i]=a[i],a[i-1]
d=""
for s in a:
  d+=s
print(d)
