a,c=input("").split()
c=int(c)
b=a[len(a)-c]
for i in range(len(a)-(c-1),len(a)):
  b+=a[i]
print(b)
