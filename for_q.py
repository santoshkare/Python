num = int(input("enter the number"))
sum=0
for i in range (1,num+1):
   if i%2==0 and i%3==0:
       sum=sum+i
print("sum=",sum)
