def area(l,b):
    return l * b

def peri(l,b):
    return 2*(l + b)


length = int(input("Enter the length "))
breadth = int(input("Enter the Breadth "))

area = area(length,breadth)
peri = peri(length, breadth)

print(f"Area of the rectangle {area}")
print(f"Perimeter of the rectangle {peri}")
