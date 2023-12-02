
user_input = input("Enter a list of characters: ")
char_list = list(user_input)
letter_frequency = {}
for char in char_list:
    if char.isalpha():
        char = char.lower()
        letter_frequency[char] = letter_frequency.get(char, 0) + 1
print("Letter frequency:")
for letter, frequency in letter_frequency.items():
    print(f"{letter}: {frequency}")
