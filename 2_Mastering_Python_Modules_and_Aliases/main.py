import text_utils as tu

user_input = input("Please input some text.: ")
print(f"You entered: {user_input}")
print(f"Your text reversed: {tu.reverse_string(user_input)}")
print(f"Your text all capitalized: {tu.capitalize_string(user_input)}")