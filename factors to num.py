def lcm(a, b):
    i = 1
    while 1:
        if i % a == 0 and i % b == 0:
            return i
        i += 1

out = lcm(5, 10)
print(out)



