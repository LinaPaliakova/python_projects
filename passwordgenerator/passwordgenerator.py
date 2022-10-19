import random 
digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
chars = ''

number_of_passwords = int(input("Сколько паролей вы хотите сгенерировать? "))
length_of_one_password = int(input("Какая должна быть длина одного пароля? "))
contains_digit = input("Включать ли цифры 0123456789? ").strip()
contains_uppercase = input("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? ").strip()
contains_lowercase = input("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? ").strip()
contain_nonalpha = input("Включать ли символы !#$%&*+-=?@^_ ?").strip()
controversive_symbols = input("Исключать ли неоднозначные символы il1Lo0O ? ").strip()


if contains_digit.lower() == "да":
    chars = chars + digits
if  contains_uppercase.lower() == "да":
    chars = chars + uppercase_letters
if  contains_lowercase == "да":
    chars = chars + lowercase_letters
if  contain_nonalpha.lower() == "да":
    chars = chars + punctuation
if  controversive_symbols.lower() == "да":
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')
        
def generate_password(length, chars):
     password = ""
     for i in range(length):
       password += random.choice(chars)
     return password
     
for _ in range(number_of_passwords):
    print(generate_password(length_of_one_password, chars))