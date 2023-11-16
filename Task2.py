import random

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*.()'

length = int(input("Enter the length of the pass: "))

password = ''
for i in range(length):
    password += random.choice(characters)

print('Password is:', password)
