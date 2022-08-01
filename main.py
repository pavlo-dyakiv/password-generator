from random import choice
from string import digits, ascii_lowercase, ascii_uppercase, punctuation


def preparing_password():
    chars = ''
    list_chars = [digits, ascii_lowercase, ascii_uppercase, punctuation, 'il1Lo0O']
    parameters = get_information()

    for i in range(len(parameters)):
        if parameters[i]:
            chars += list_chars[i]
    if parameters[-1]:
        for e in 'il1Lo0O':
            chars = chars.replace(e, '')
    return chars


def get_information():
    questions = ['Включать ли цифры 0123456789? ', 'Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? ',
                 'Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? ', 'Включать ли символы !#$%&*+-=?@^_? ',
                 'Исключать ли неоднозначные символы il1Lo0O? ']

    information = []

    for i in questions:
        if input(i).lower() == 'да':
            information.append(True)
        else:
            information.append(False)

    return information


def generate_password(count, length):
    list_symbol = preparing_password()
    if not list_symbol:
        return "Жаль, но пароль не из чего сгенерировать, так как, на все вопросы Вы ответели 'нет', либо ничего не ответили".split()
    list_passwords = []
    for _ in range(count):
        password = ''
        for _ in range(length):
            c = choice(list_symbol)
            password += c
        list_passwords.append(password)
    return list_passwords


count_passwords = int(input('Пожалуйста, введите количество паролей '))
length_password = int(input('Пожалуйста, введите длинну паролей '))


print(*generate_password(count_passwords, length_password))

