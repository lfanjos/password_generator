import random
import string

from utilities.cool_functions import valid_input

alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase
numbers = string.digits
special_chars = string.punctuation

print("******************** GERADOR DE SENHAS ********************")

length = int(valid_input(input("Informe o tamanho da senha (max 99): "),
                         {
                             'length': 2,
                             'min': 0,
                             'chars': numbers
                         }))
upper_letters = int(valid_input(input(f"Número de letras maiúsculas (max {length}): "),
                                {
                                    'max': length,
                                    'min': 0,
                                    'chars': numbers
                                }))
lower_letters = int(valid_input(input(f"Número de letras minúsculas (max {length - upper_letters}): "),
                                {
                                    'max': length - upper_letters,
                                    'min': 0,
                                    'chars': numbers
                                }))
punctuations = int(valid_input(input(f"Número de pontuação (max {length - upper_letters - lower_letters}): "),
                               {
                                   'max': length - upper_letters - lower_letters,
                                   'min': 0,
                                   'chars': numbers
                               }))

new_password = ''


for _ in range(upper_letters):
    new_password += random.choice(alphabet_upper)
for _ in range(lower_letters):
    new_password += random.choice(alphabet_lower)
for _ in range(punctuations):
    new_password += random.choice(special_chars)
if (punctuations + lower_letters + upper_letters) < length:
    for _ in range(length - punctuations - lower_letters - upper_letters):
        new_password += random.choice(numbers)

new_password = list(new_password)
random.shuffle(new_password)
new_password = ''.join(new_password)

print(f"Seu novo password é: {new_password}")
