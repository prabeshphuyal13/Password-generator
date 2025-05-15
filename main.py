import random
import string

def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def password_generator(length, is_digits, is_spec_char ):

    letters = list(string.ascii_letters)
    digits = list(string.digits)
    spec = list(string.punctuation)

    pwd = []
    
    if is_digits and is_spec_char:
       
        no_of_digits = random.randint(0,int(length/3))
        no_of_spec = random.randint(0,int(length/3))

        ran_digits = random.choices(digits, k=no_of_digits )
        ran_spec = random.choices(spec, k = no_of_spec )
        ran_letters = random.choices(letters, k = length - no_of_digits - no_of_spec )
        
        pwd = ran_digits + ran_letters + ran_spec

    
    elif is_digits:
        
        no_of_digits = random.randint(0, int(length/2))
        ran_digits = random.choices(digits, k = no_of_digits )
        ran_letters = random.choices(letters, k = length - no_of_digits)
        pwd = ran_digits + ran_letters

    
    elif is_spec_char:
        
        no_of_spec = random.randint(0, int(length/2))
        ran_spec = random.choices(spec, k = no_of_spec )
        ran_letters = random.choices(letters, k = length - no_of_spec)
        pwd = ran_spec + ran_letters

    else:
        ran_letters = random.choices(letters, k = length)
        pwd = ran_letters

    random.shuffle(pwd)
    return "".join(pwd)

def main ():
   
    while True:
        clear()
        print("PASSWORD GENERATOR 🔐")
        len = int(input("\nEnter No. Of Length: "))

        is_yes = lambda x: x.lower() == 'y'

        digit = is_yes(input("Do You Want Digits [y/n]: "))
        spec = is_yes(input("Do You Want Special Characters [y/n]: "))

        clear()
        print("Here are Option for Your Password, Choose and Use 😁\n")

        for i in range(5): print( i+1 ,password_generator(len,digit,spec))

        if "" != input("\nPress ENTER to generate again..\n"):
            exit()


main()