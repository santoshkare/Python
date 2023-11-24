#write a function to check whether given no. is prime or not

def prime(num):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count += 1
    return(count == 2)

out = prime(7)
print(out)
