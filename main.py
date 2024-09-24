import secrets
import os
import string
import re

NUMBER_CHARACTER_MINIMUM = 14

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def number_characters():
    while True:
        try:
            user_number_carac = int(input("Enter number of characters you want to have in your password : "))
            if user_number_carac < 14:
                final_choice = int(input(f"""\nPassword should not have less than {NUMBER_CHARACTER_MINIMUM} characters. Are you sure you want to continue ? 
                                         \nPress 1 if you want to keep a password with {user_number_carac} characters, other characters if you want to change it : """))
                if final_choice == 1:
                    return user_number_carac
                else:
                    number_characters()
            else:
                return user_number_carac
        except ValueError:
            print("Error ! Enter a valid number. ")

def is_special_caracters():
    while True:
        try:
            user_caracter_choice = input("""\nDo you want to include special characters to your password ? (Recommended) : 
                                            \n-Press 1 for yes, other caracter for no : """)
            return user_caracter_choice
        except:
            print("Error")
       
def generate_password(number_caract, special_caracters):
    characters_choice = string.ascii_letters + string.digits
    if special_caracters == "1":
        characters_choice += string.punctuation
    password = ''.join(secrets.choice(characters_choice) for i in range(number_caract)) 
    return password

def strong_password(password):
    global NUMBER_CHARACTER_MINIMUM
    lower_criteria = re.search("[a-z]", password)
    upper_criteria = re.search("[A-Z]", password)
    digit_criteria = re.search("[0-9]", password)
    special_criteria = re.search(r'[!#$%&\'()*+,\-./:;<=>?@[\]^_`{|}~"]', password)
    all_criteria = [("lower character", lower_criteria),
                    ("upper character", upper_criteria),
                    ("digit character", digit_criteria),
                    ("special character", special_criteria),
                    ]
    if all(criteria[1] for criteria in all_criteria) and len(password) >= NUMBER_CHARACTER_MINIMUM:
        print("\nPassword is strong !")
        return True
    else:
        print("\nPassword is weak, following criteria(s) is/are missing")
        for name, met in all_criteria:
            if not met:
                print(f"-{name}")
        if len(password) < NUMBER_CHARACTER_MINIMUM:
            print(f"-number of characters")
        return False

def main():
    clear_screen()
    number = number_characters()
    special_caracters = is_special_caracters()
    password_generated = generate_password(number, special_caracters)
    if strong_password(password_generated):
        print(f"Password generated : ",password_generated)
        pass
    else:
        regenerate = input(f"\nSince password is weak {password_generated}, do you want to regenerate a new one? Press 1 for yes, other character for no : ")
        if regenerate == '1':
            main()
        else:
            print(f"Password generated : ",password_generated)

main()