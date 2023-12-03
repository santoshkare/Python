##String Rotation:
##Given two strings, write a function to check if one is a rotation of the other. For 
##example, "waterbottle" is a rotation of "erbottlewat."
str1 = "waterbottle"
str2 = "erbottlewat"
if len(str1) == len(str2) and len(str1) > 0:
    concatenated_str = str1 + str1
    if str2 in concatenated_str:
        print(f"{str1} is a rotation of {str2}.")
    else:
        print(f"{str1} is not a rotation of {str2}.")
else:
    print("Invalid input strings.")
