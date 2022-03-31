import random

letters_upper = 'ABCDEIFGHIJKLMNOPQRSTUVWXYV'
letters_lower = 'abcdefghijklmnopqrstuvwxyz'
symbols = '!@#$%¨&*()?/{}*+'
numbers = '1234567890'

qnt = 15
intQtn = int(qnt)
lenght = intQtn 

password = letters_upper + letters_lower + symbols + numbers 
passwordgen = "".join(random.sample(password, lenght))

print('Suggested password: ' + passwordgen)
