#write a function to tell user if he/she able to vote or not.

"""Without parameter and without return value."""
# def age():
#     x=int(input("enter the age ==>" ))
#     if x >=18 :
#         print("you are eligible for vote.")
#     else:
#         print("you are not eligible for vote.")
# age()            
            
"""With parameter and without return value."""
# def age(x):
    
#     if x >=18 :
#         print("you are eligible for vote.")
#     else:
#         print("you are not eligible for vote.")
# x=int(input("enter the age ==>" ))
# age(x)  


"""With parameter and with return value."""
# def age(x):
    
#     if x >=18 :
#         return "you are eligible for vote."
#     else:
#         return "you are not eligible for vote."
# x=int(input("enter the age ==>" ))
# print(age(x))
         
         
"""Without parameter and with return value."""
def age():
    x=int(input("enter the age ==>" ))
    if x >=18 :
        return "you are eligible for vote."
    else:
        return "you are not eligible for vote."

print(age())