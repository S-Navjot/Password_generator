import secrets
import os
import string
import re

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def number_caracters():
    while True:
        try:
            user_number_carac = int(input("Enter number of caracters you want to have in your password : "))
            if user_number_carac < 14:
                final_choice = int(input(f"""\nPassword should not have less than 14 caracters. Are you sure you want to continue ? 
                                         \nPress 1 if you want to keep a password with {user_number_carac} caracters
                                         \nPress any other caracters if you want to change it : """))
                if final_choice == 1:
                    return user_number_carac
                else:
                    number_caracters()
            else:
                return user_number_carac
        except ValueError:
            print("Error ! Enter a valid number. ")

def is_special_caracters():
    while True:
        try:
            user_caracter_choice = input("""Do you want to include special caracters to your password ? (Recommended) : 
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
    lower_criteria = re.search("[a-z]", password)
    upper_criteria = re.search("[A-Z]", password)
    digit_criteria = re.search("[0-9]", password)
    special_criteria = re.search(r'[!#$%&\'()*+,\-./:;<=>?@[\]^_`{|}~"]', password)
    all_criteria = [("lower character", lower_criteria),
                    ("upper character", upper_criteria),
                    ("digit character", digit_criteria),
                    ("special character", special_criteria),
                    ]
    if all(criteria[1] for criteria in all_criteria):
        print("\nPassword is strong !")
    else:
        print("\nPassword is weak, following criteria(s) is/are missing")
        for name, met in all_criteria:
            if not met:
                print(f"-{name}")
        return False
    return True


def main():
    clear_screen()
    number = number_caracters()
    special_caracters = is_special_caracters()
    password_generated = generate_password(number, special_caracters)
    if not strong_password(password_generated):
        while True:
            regenerate = input(f"\nSince password is weak {password_generated}, do you want to regenerate a new ? Press 1 for yes, other character for no : ")
            if regenerate == '1':
                main()
            else: 
                break
    print(password_generated)

main()