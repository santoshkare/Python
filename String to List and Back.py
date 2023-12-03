#String to List and Back:
input_str = "Python"
char_list = []
for char in input_str:
    char_list.append(char)
new_str = ''.join(char_list)

print(f"Original String: {input_str}")
print(f"String converted to list and back: {new_str}")
