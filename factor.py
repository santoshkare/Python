#write a program to display the divisor of the number

def divisors(num):
    count = []
    for i in range(1,num+1):
        if num % i == 0:
            count.append(i)
    return count

out = divisors(6)
print(out)
