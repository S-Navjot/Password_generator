import secrets
import os
import string
import re
import random

NUMBER_CHARACTER_MINIMUM = 14

def clear_screen(): #Clear terminal on Windows/Linux/Mac
    os.system("cls" if os.name == "nt" else "clear")

def get_valid_choice():#Function to choose password criteria. (if the user need special character, if the user want to generate a secure password.)
    choice = ''
    while choice not in ['1', '2', '3']:
        clear_screen()
        choice = input("""Select your option:
        \n1 - Special characters included
        \n2 - No special characters
        \n3 - Generate strong password (between 20 and 30 characters, with special, lower, upper and digits)
        \nMake your choice (1, 2 or 3): """)
    return choice

def number_characters(): #If the user selects option 1 or 2 on previous function, he has to choose the number of characters he wants. If number of characters is under 14, a security message is displayed and the user need to validate his choice
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
  
def generate_password(number_caract, special_characters): #Generate a random based on user choice (number of characters, if special characters)
    characters_choice = string.ascii_letters + string.digits
    if special_characters == "1":
        characters_choice += string.punctuation
    password = ''.join(secrets.choice(characters_choice) for i in range(number_caract)) 
    return password

def strong_password(password):#Check that all security criterias (password length, digit, lower, upper and special) are present in the generated password. If not, missing criteria are displayed
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

def write_password_in_file(password): #Generate a txt file in the script location. Password is saved in this txt file
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "password.txt")
    with open(file_path, 'w') as f:
        f.write(password)
        print(f"Password succefully generated in {file_path} file.")

print("""Welcome in this Password Generator !
        \nGithub : https://github.com/S-Navjot/Password_generator/blob/main/main.py
        """)

def main(): #Main function
    while True:
        choice = get_valid_choice()
        special_characters = '1' if choice == '1' or choice == '3' else '0'
        number = random.randrange(20, 30) if choice == '3' else number_characters()   
        while True:
            password_generated = generate_password(number, special_characters)
            if strong_password(password_generated):
                print(f"\nPassword generated: {password_generated}")
                write_password_in_file(password_generated)
                break
            else:
                regenerate = input(f"\nPassword is weak ({password_generated}). Regenerate? Press 1 for yes, any other key for no: ")
                if regenerate != '1':
                    print(f"\nPassword generated: {password_generated}")
                    write_password_in_file(password_generated)
                    break  
        break
    
main()
