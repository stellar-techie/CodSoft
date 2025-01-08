#PASSWORD GENERATOR

import random
import string

def generate_password(length):

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    characters = lowercase + uppercase + digits + punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Hi! let's create a safe password for you buddy :)")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("oops! Length must be a positive number. Please try again :( ")
            elif length > 8:
                print("oops! Length must not exceed 8 characters. Please try again :(")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    
    password = generate_password(length)
    
    print("here's your password :", password)
    print("Thank you for using me :)\n bye bye.")

if __name__ == "__main__":
    main()
