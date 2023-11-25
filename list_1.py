list_1 = [1,2,3,4,5,7,8,9]
##list_1 = int(input("Enter the number to add in a list..."))
empty_list = []
for i in list_1:
   a = i**2
   print(a)
   if a%2!=0:
       empty_list.append(a)
       
##    else:
##        print("None")
##        
print(empty_list)

n = eval(input("enter any value"))
print(n)