# Pssword strenght checker

import re

# def check_password_strenght(password):
#     if len(password) < 8:
#         return " Weak: password must be at least 8 chars"
#     if not any(char.isdigit() for char in password):
#         return "weak: password must contain a digit"
#     if not any (char.isupper() for char in password):
#         return "weak: Password must have contain a upper value"
    
#     if not any (char.islower() for char in password):
#         return "weak: Password must have contain a lower  value"
    
#     if not re.search(r'[!@#$^&*]', password):
#         return "medium password must contain a special character"
    
#     return "Strong: your password secure"

# def password_checker():
#     print("welcome to the checker")

#     while True:
#         password = input("enter you password")
        
        
#         if password.lower() == 'exit':
#             print("thank u for using this tool")
#             break
#         result = check_password_strenght(password)
#         print(result)


# if __name__ == "__main__":
#     password_checker()

        
        
        
        
        
        
        
def password_strenght(password):
    if len(password) < 8:
        return "Weak: Password must have 8 character"
    
    if not any (char.isdigit() for char in password):
        return "Weak: Password must have a digit"
    
    if not any (char.islower() for char in password):
        return "Weak: Password must have a lower value"
    
    if not any (char.isupper() for char in password):
        return "Weak: Password must have a upper value"
    
    if not re.search(r'[!@#$%^&*()]',password):
        return "Weak : password must have a special character"
    
    return " STRONG PASSWORD"

def password_checker():
    print("WELCOME TO PASSWORD CHECKER")

    while True:
        password = input("Enter password")

        
        if password.lower() == 'exit':
            print("THank for ")
            break
        result = password_strenght(password)
        print(result)
        
if __name__ == "__main__":
     password_checker()


    
    


        
        
    
    
        
        
        
        
        
        
        
        
         

