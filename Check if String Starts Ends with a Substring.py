#Check if String Starts/Ends with a Substring:
input_str = "Hello, World!"
starts_with_hello = input_str[:5] == "Hello"
ends_with_world = input_str[-6:] == "World!"

print(f"Does the string start with 'Hello'? {starts_with_hello}")
print(f"Does the string end with 'World!'? {ends_with_world}")

