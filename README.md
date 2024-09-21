# Python Password Generator by S-Navjot

This project is a Python script that allows you to generate password based on selected criterias. The script uses the `secret` library to generate password, as well as `string` to perform a characters searching. `regex` is used to check for the strength of the generated password.

## Features  

- Generate password
- User can decide for number of characcters, adding specials characters
- If generated password is not strong, user can generate a new one

## Installation  

### Prerequisites  

- Python 3.x must be installed on your machine. You can download it from [python.org](https://www.python.org/).

### Installation Steps  

1. Clone the GitHub repository:

   ```sh
   git clone https://github.com/S-Navjot/Password_generator.git

### Usage Steps    

Open the Terminal
```sh
$ cd Password_generator
$ python3 main.py
```

1. Enter the number of characters you want the password to have 
2. Enter if you want to add a special characters  
3. If you're not satisfied with generated password, you can generate a neew one  

### Libraries Used  

* secret (https://docs.python.org/fr/3/library/secrets.html)
* os (https://docs.python.org/fr/3/library/os.html) 
* string (https://docs.python.org/fr/3/library/string.html#module-string)
* re (https://docs.python.org/3/library/re.html)


### OS

Working on :
* Windows
* Linux
* MAC

### Versions

V1 (3rd August 2024)
--------------------
- First release

V1.1 (6th August 2024)
--------------------
- If user select a password with less than 14 characters, it'll be shown as weak criteria
