import random

passwords = []
chars = 'abcçdefghijklmnopqrstuvwxyzABCÇDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*().,?0123456789'
number = int(input('Quantas senhas gerar? '))
length = int(input('Qual o tamanho das senhas? '))

for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    passwords.append(password)

file = open("passwords.txt", "a")

for i in range(number):
    file.write(f'Senha {i+1} - {passwords[i]} \n')

file.close()

print('Senhas geradas no arquivo: passwords.txt')