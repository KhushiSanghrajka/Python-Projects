import random
print('Welcome to Password Genertor')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYX!@$%^&*.,?0123456789'
number = int(input('How many passwords do you want to generate? '))
length = int(input('Enter the length of password: '))

print("Generated Passwords are:")

for pwd in range(0, number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)

