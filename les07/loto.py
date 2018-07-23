import random
import sys


class Game():
    def __init__(self):
        self.status_game = -1
        self.casks = Casks()
        self.user_card = Card('user')
        self.comp_card = Card('comp')
        self.game_step()

    def __str__(self):
        return f"{self.casks.get_cask()}\n{self.user_card}\n{self.comp_card}"

    def game_step(self):
        for c in self.casks:
            if c != -1:
                print(self)
                self.status_game = -1
                while self.status_game == -1:
                    self.result_of_step()
                    if self.user_card.all_num == 0 or self.comp_card.all_num == 0:
                        self.status_game = 0
                if self.status_game == 0:
                    self.game_over()
                continue
            break
        self.game_over()

    def result_of_step(self):
        answer = input('Зачеркнуть число? Y/N:')
        check_user = self.user_card.check_hit(self.casks.current_cask)
        check_comp = self.comp_card.check_hit(self.casks.current_cask)
        if answer.upper() == 'Y':
            if check_user == 0:
                self.status_game = 0
            else:
                self.status_game = 1
        elif answer.upper() == 'N':
            if check_user == 1:
                self.status_game = 0
            else:
                self.status_game = 1
        else:
            print('Введите только "Y" или "N"')
            self.status_game = -1

    def game_over(self):
        print("Your game is over!")
        if self.user_card.all_num == 0 and self.comp_card.all_num == 0:
            print("Победила дружба!")
        elif self.user_card.all_num == 0:
            print("Congratulations!! Пользователь победил!")
        elif self.comp_card.all_num == 0:
             print("Пользователь проиграл! :(")
        else:
            print("Пользователь проиграл из-за не внимательности!")
        sys.exit(0)


class Card:
    def __init__(self, gamer):
        self.card = [['' for _ in range(9)] for _ in range(3)]
        self.all_num = 15
        self.gamer = gamer
        # Наполняем карточку числами
        for line in self.card:
            q = 0
            while q < 5:
                index = random.randrange(9)
                if line[index] == '':
                    line[index] = random.choice(Casks().lst_casks)
                    # Проверка на уникальность
                    count = 0
                    for l in self.card:
                        for el in l:
                            if line[index] == el:
                                count += 1
                                if count == 2:
                                    line.remove(el)
                                    line.append('')
                                    q -= 1
                                    break
                    q += 1

    def __str__(self):
        if self.gamer == 'user':
            header = f"{'-' * 6} Карточка пользователя {'-' * 6}"
        elif self.gamer == 'comp':
            header = f"{'-' * 7} Карточка компьютера {'-' * 7}"
        row1 = '\t'.join(map(str, self.card[0]))
        row2 = '\t'.join(map(str, self.card[1]))
        row3 = '\t'.join(map(str, self.card[2]))
        footer = f"{'-' * 35}"
        return f'{header}\n{row1}\n{row2}\n{row3}\n{footer}'


    def check_hit(self, num):
        for line in self.card:
            for el in line:
                if num == el:
                    index = line.index(el)
                    line[index] = '--'
                    self.all_num -= 1
                    return 1
        return 0


class Casks:
    def __init__(self):
        self.lst_casks = list(range(1, 91))
        self.current_cask = -1

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.lst_casks) > 0:
            self.current_cask = random.choice(self.lst_casks)
            self.lst_casks.remove(self.current_cask)
            return self.current_cask
        else:
            return -1

    def get_cask(self):
        return f'Новый бочонок: {self.current_cask} (осталось: {len(self.lst_casks)})'


match = Game()
