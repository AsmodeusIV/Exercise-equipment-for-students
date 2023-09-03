import random
import sys

def Choose_mode():
    print('Выберите режим:')
    print('1. Перевод из 10-й системы счисления в р-ичную')
    print('2. Перевод из р-ичной системы счисления в 10-ую')
    print('3. Сумма в p-ичной системе счисления')
    print('4. Разность  p-ичной системе счисления')
    print()
    print('Введите номер нужного вам режима:')
    mode = input()
    print()
    if(mode.isdigit() and int(mode)<5 and int(mode)>0):
        Training(mode)
    else:
        print('Некорректный ввод')
        Choose_mode()

def Generate_number(size):
    number = ''
    for i in range(size):
        number += str(random.randint(1, 9))
    return number

def Number_to_base(n, b):
    alphabet = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F',]
    if n == 0:
        return 0
    digits = ''
    while n:
        digits += alphabet[n % b]
        n //= b
    return digits[::-1]

def Training(mode):
    len_a = random.randint(3, 6)
    len_b = random.randint(2, len_a)
    a = Generate_number(len_a)
    b = Generate_number(len_b)
    
    new_base = 10
    while(new_base == 10):
            new_base = random.randint(2, 16)
    
    match mode:
        case '1':
            aq =  Number_to_base(int(a), int(new_base))
            print()
            print('Переведите число ', a, ' из 10 в ', new_base, ' систему счисления :')
            print('(алфавит состоит из английских заглавных символов, следите за пробелами)')
            x = input()
            if(x==aq):
                print('great')
            else:
                print('Правильный ответ: ', aq)
        case '2':
            print()
            print('Переведите число ', Number_to_base(int(a), int(new_base)),' из ', new_base, ' системы счисления в 10:')
            print('(алфавит состоит из английских заглавных символов, следите за пробелами)')
            x = input()
            if(x==a):
                print('great')
            else:
                print('Правильный ответ: ', a)
        case '3':
            print()
            print('Введите сумму чисел ', Number_to_base(int(a), int(new_base)) , 'и ', Number_to_base(int(b), int(new_base)), ' в ', new_base, ' системе счисления :')
            print('Числа указаны в ', new_base, 'системе счисления')
            print('(алфавит состоит из английских заглавных символов, следите за пробелами)')
            a = Number_to_base(int(a)+int(b), int(new_base))
            x = input()
            if(x==a):
                print('great')
            else:
                print('Правильный ответ: ', a)
        case '4':
            print()
            print('Введите разность чисел ', Number_to_base(max(int(a), int(b)), int(new_base)), 'и ', Number_to_base(min(int(a), int(b)), int(new_base)), ' в ', new_base, ' системе счисления :')
            print('Числа указаны в ', new_base, 'системе счисления')
            print('(алфавит состоит из английских заглавных символов, следите за пробелами)')
            a = Number_to_base(max(int(a), int(b))-min(int(a), int(b)), int(new_base))
            x = input()
            if(x==a):
                print('great')
            else:
                print('Правильный ответ: ', a)
    print()
    print('Вы хотите повторить упражнение? (y/n)')
    t = input()
    if(t=='y'):
        return Training(mode)
    print()
    print('Вы хотите выбрать другое упражнение? (y/n)')
    t = input()
    if (t=='y'):
        return Choose_mode()
    print()
    print('Всего доброго :)')
    sys.exit()


#Начало
Choose_mode()
