# == Лото ==
# Правила игры в лото.
#
# Игра ведется с помощью специальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
#
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
import random

card_user = []
card_pc = []
len_of_line = 9

# заполняем карточки
def fill_card(card):
    # Создаем пустую карточку
    card = [['' for _ in range(len_of_line)] for _ in range(3)]
    # Наполняем карточку числами
    for line in card:
        q = 0
        # добавляем 5 рандомных чисел в ряд
        while q < 5:
            idx = random.randrange(len_of_line)
            if line[idx] == '':
                line[idx] = random.randint(1, 91)
                # проверяем на уникальность
                count = 0
                # проходим по всей карточке
                for l in card:
                    for el in l:
                        if line[idx] == el:
                            count += 1
                            if count == 2:
                                line.remove(el)
                                line.append('')
                                q -= 1
                                break
                q += 1
    return card


# Выводим карту на экран
def print_card(card):
    print('-' * 45)
    for line in card:
        for el in line:
            print(f'{el:>3} |', end='')
        print()
    print('-' * 45)


# class Game
def step():
    pass


card_user = fill_card(card_user)
card_pc = fill_card(card_pc)

print('Карточка пользователя')
print_card(card_user)
print('Карточка компьютера')
print_card(card_pc)

