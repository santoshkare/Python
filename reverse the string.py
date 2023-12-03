##Reverse a String:
##Write a function that reverses a given string without using any built-in reverse 
##functions or methods.
def reverse_string(input_str):
    reversed_str = ""
    for char in input_str:
        reversed_str = char + reversed_str
    return reversed_str
original_str = "Hello, World!"
reversed_str = reverse_string(original_str)
print(f"Original String: {original_str}")
print(f"Reversed String: {reversed_str}")
