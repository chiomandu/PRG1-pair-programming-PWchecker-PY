import datetime
#checks for checking password log
INPUT_FILE = "./common_passwords.txt"
OUTPUT_FILE = "./checking_password_log.txt"





def get_current_datetime_formatted():
    now = datetime.datetime.now()
    return now.strftime("%d-%m-%Y %H:%M:%S")


def read_in_file(filename):
    with open(filename, "r") as f:
            return f.read()
    

def is_strong_password(password):
    if len(password) <= 8:
        return False
    
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    
    return has_upper and has_lower


password=(input("Give me a password? : "))

def is_common_password(password):
     common_passwords_text= read_in_file(INPUT_FILE)
     common_passwords_list=common_passwords_text.splitlines()
     return password in common_passwords_list
if is_common_password(password):
         print("Too common")

     


def check_password(password):
    
    is_strong = is_strong_password(password)
    
    # Log the check
    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        strength = "Strong" if is_strong else "Weak"
        current_time_and_date = get_current_datetime_formatted()
        f.write(f"{current_time_and_date} - Password checked: {strength}\n")
    
    return is_strong



# Sample calls to test the program

print(check_password("ada"))  # Predict weak password (false)
print(check_password("AdaLovelace123"))  # Predict strong password (strong is debatable!)  (true)