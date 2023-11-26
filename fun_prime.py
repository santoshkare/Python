#write a function to check if a number is prime or not.
def num(n):
    count = 0
    for i in range(1,n+1):
        if n%i == 0:
            count+=1
    if count == 2:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")
 
n = int(input("enter the number ==> "))
num(n)   
                  