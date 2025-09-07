import random as rd
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]|;:,.<>?/~`'
len = int(input("Enter the length of the password: "))
password = " "
for i in range(len):
    password += rd.choice(chars)
print("Your password is: ", password)
    