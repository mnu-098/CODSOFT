import random 
letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
symbols = '!#$%&()*+'
print('Welcome to the Password Generator!')
nr_letters = int(input('How many letters would you like in your password?\n'))
nr_symbols = int(input(f'How many symbols would you like?\n'))
nr_numbers = int(input(f'How many numbers would you like?\n'))
password_list = []
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))
for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)
password = ''
for char in password_list:
    password += char
print(f'Your password is: {password}')