dy=int(input())
a=input(" ")
a=list(a.split(' '))
freq={}
for i in a:
  if i in freq:
    freq[i]+=1
  else:
    freq[i]=1
for key,value in freq.items():
  if value==1:
    print(key)
