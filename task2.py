# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

def input_count(name):
    if name == 'bot':
        x = random.randint(1,candies)
    else:
        x = int(input(f'{name}, сколько конфет ты хочешь взять?\n --> '))
    while x > candies  or x <0:
        x = int(input(f'По правилам ты можешь взять не больше {candies} конфет. Попробуй еще раз\n--> '))
    return x

def print_msg(name, candy):
    if name == 'bot':
        return print(f'Бот взял {candy} конфет')

print('Первый ход определяется жеребьёвкой. На столе будет лежать некоторое количество конфет.\n' 
    'За один ход можно забрать не более определенного количества конфет. Обо всем мы договоримся\n' 
    'Все конфеты оппонента достаются сделавшему последний ход.\n '
    'Игра для двоих. Но если ты один, то можешь поиграть с ботом\n'
    'Начнем!')

choose_game = int(input('Игра с человеком [1]\n'
            'Игра с ботом [2]\n'
            '-->'))

if choose_game == 1:
    player1 = input('Введите свое имя: ')
    player2 = input('Введите свое имя: ')
else: 
    player1 = input('Привет, я бот, просто бот, а тебя как зовут? ')
    player2 = 'bot'

total_candies = int(input('Сколько конфет будет лежать на столе?\n'))
candies = int(input('Сколько максимально будем брать конфет за один ход?\n'))

first_step = random.randint(0,1)
if first_step: 
    print(f'Первый ход делает {player1}')
else: 
    print(f'Первый ход делает {player2}')

while total_candies > 0:
    
    if first_step:
        take_candy = input_count(player1)
        total_candies = total_candies - take_candy
        first_step = False
        print_msg(player1, take_candy)
    else:
        take_candy = input_count(player2)
        total_candies = total_candies - take_candy
        first_step = True
        print_msg(player2, take_candy)        

    if total_candies >= 0: print(f'Осталось {total_candies} конфет')
    else: print('Все конфеты разобраны.')

if not first_step:
    print(f'Победитель {player1}!!! Все конфеты достаются победителю')
else: print(f'Победитель {player2}!!! Все конфеты достаются победителю')

