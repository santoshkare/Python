st=input('')
k=int(input(''))
d={}
for i in st:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
ans=""
for i in st:
    if d[i]<k:
        ans=ans+i
print(ans)        
