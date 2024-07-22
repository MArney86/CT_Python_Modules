import text_utils as tu #import our custom module with the alias 'tu'

user_input = input("Please input some text.: ") #get some text from the user
print(f"You entered: {user_input}") #print the input from the user unchanged
print(f"Your text reversed: {tu.reverse_string(user_input)}") #print the input from the user reversed
print(f"Your text all capitalized: {tu.capitalize_string(user_input)}") #print the input from the user with all characters capitalized