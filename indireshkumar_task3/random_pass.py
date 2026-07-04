import random
import string
while True:
    create_password() 
    print("Would you like to create another password? (y/n)")
    user_input = input().strip().lower()
    if user_input != 'y':
        break
    
def create_password():
    length = int(input("Enter the desired password length: "))
    if length < 0:
        print("Password length cannot be negative. Please enter a valid length.")
        return
    if length <8:
        print("Password length should be at least 8 characters. Please enter a valid length.")
        return
    print("Choose the character types to include in the password:")
    print("select atleast two character types:")
    include_uppercase = input("Include uppercase letters? (y/n): ").strip().lower()
    include_lowercase = input("Include lowercase letters? (y/n): ").strip().lower()
    include_digits = input("Include digits? (y/n): ").strip().lower()  
    include_special = input("Include special characters? (y/n): ").strip().lower()
    if (include_uppercase != 'y' and include_lowercase != 'y' and include_digits != 'y' and include_special != 'y'):
        print("You must select at least two character type. Please try again.")
        return
    if (include_uppercase == 'y' and include_lowercase == 'y' and include_digits == 'y' and include_special == 'y'):
        password+= ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, k=length))
        print(f"Your generated password is: {password}")
        return
    if (include_uppercase == 'y' and include_lowercase == 'y' and include_digits == 'y'):
        password = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=length))
        print(f"Your generated password is: {password}")
        return
    if (include_uppercase == 'y' and include_lowercase == 'y' and include_special == 'y'):
        password = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.punctuation, k=length))
        print(f"Your generated password is: {password}")
        return
    if (include_uppercase == 'y' and include_digits == 'y' and include_special == 'y'):
        password = ''.join(random.choices(string.ascii_uppercase + string.digits + string.punctuation, k=length))
        print(f"Your generated password is: {password}")
        return
    if (include_lowercase == 'y' and include_digits == 'y' and include_special == 'y'):
        password = ''.join(random.choices(string.ascii_lowercase + string.digits + string.punctuation, k=length))
        print(f"Your generated password is: {password}")
        return
    if (include_uppercase == 'y' and include_lowercase == 'y'):
        password = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=length))
        print(f"Your generated password is: {password}")
        return
    if (include_uppercase == 'y' and include_digits == 'y'):
        password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        print(f"Your generated password is: {password}")
        return
    if (include_uppercase == 'y' and include_special == 'y'):
        password = ''.join(random.choices(string.ascii_uppercase + string.punctuation, k=length))
        print(f"Your generated password is: {password}")
        return
    if (include_lowercase == 'y' and include_digits == 'y'):
        password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
        print(f"Your generated password is: {password}")
        return
    if (include_lowercase == 'y' and include_special == 'y'):
        password = ''.join(random.choices(string.ascii_lowercase + string.punctuation, k=length))
        print(f"Your generated password is: {password}")
        return
    if (include_digits == 'y' and include_special == 'y'):
        password = ''.join(random.choices(string.digits + string.punctuation, k=length))
        print(f"Your generated password is: {password}")
        return
    
     
    