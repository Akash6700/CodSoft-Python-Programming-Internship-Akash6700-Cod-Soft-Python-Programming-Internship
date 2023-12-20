import random
import string

def generate_password(length):
    # Define the set of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password using random.choice
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    # Prompt the user to specify the desired length of the password
    password_length = int(input("Enter the desired length of the password: "))

    # Generate the password
    generated_password = generate_password(password_length)

    # Display the generated password
    print("Generated Password:", generated_password)

if __name__ == "__main__":
    main()
