A=int(input())
a=input("")
a1=list(a.split(" "))
b=[]
for i in range(0,len(a1)):
  for j in range(i+1,len(a1)):
    if(a1[i]==a1[j]):
      if a1[i] not in b:
        b.append(a1[i])
if len(b)==0:
  print("unique")
else:
  c=" ".join(b)
print(c)
