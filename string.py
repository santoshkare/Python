str=input('enter main string:')
sub=input('enter sub string:')
i=0
flag=False
n=len(str)
while i<n:
   pos=str.find(sub,i,n)
   if pos !=-1:
       print('found at position:',pos+1)
       i=pos+1
       flag=True
   else:
      i=i+1
   if flag==False:
       print('sub string is not found')