def average(*number):
    sum=0
    for i in number:
        sum=sum+i
    print("average is:",sum/len(number))
average(5,6,7,1)    