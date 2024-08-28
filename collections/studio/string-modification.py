my_string = "LaunchCode"

# a) Use string methods to remove the first three characters from the string and add them to the end.
new_string =my_string[3:] + my_string[:3]
print(new_string)
# Use a template literal to print the original and modified string in a descriptive phrase.

print(f"{my_string} translates into python-latin as {new_string}")

# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.
translator_input = input("Enter a word for the translator:")
translator_output = translator_input[3:] + translator_input[:3]
print(f"{translator_input} translates into python-latin as {translator_output}")

# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.
### !!!!! #####