import random
import string

def generate_password(length, complexity):
    if complexity == "low":
        characters = string.ascii_letters + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation + string.whitespace
    else:
        return "Invalid complexity level. Choose 'low', 'medium', or 'high'."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Password Generator")

while True:
    length = int(input("Enter password length: "))
    complexity = input("Enter complexity level (low/medium/high): ")

    password = generate_password(length, complexity)
    print("Generated Password:", password)

    generate_again = input("Generate another password? (yes/no): ")
    if generate_again.lower() != 'yes':
        break

print("Thank you for using the Password Generator!")
