# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    r = int(number*(10**ndigits) + 0.5)/(10**ndigits)
    return r

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    num_lst = []
    i = 0
    if 100000 <= ticket_number <= 999999:
        while ticket_number > 0:
            a = ticket_number % 10
            num_lst.append(a)
            ticket_number = ticket_number // 10
            i += 1
        if sum(num_lst[:3]) == sum(num_lst[3:]):
            return 'У вас счастливый билет!!!'
        else:
            return 'Повезет в следующий раз.'
    else:
        return 'Не верный номер билета'


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(123219))