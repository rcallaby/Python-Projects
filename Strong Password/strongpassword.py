import random

# define the length of the password
length = 10

# define the characters to be used when generating a password
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'

# define an empty string to store the generated characters
password = ''

# loop to generate the password
for i in range(length):
    # randomly select a character and add it to the password
    password = password + random.choice(chars)

# print the generated password
print("Your new password is:", password)
