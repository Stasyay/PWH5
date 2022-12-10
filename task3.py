# Создайте программу для игры в ""Крестики-нолики"".import random
import random

board = list(range(1,10))

def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-------------")


def get_winner(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def take_input(player_step):
    valid = False
    while not valid:
        player_answer = int(input(f'Куда поставим {player_step}? '))
        if player_answer >= 1 and player_answer <= 9:
            if(str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_step
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")

def main(board):
    count = 0
    win = False
    player1 = input('Введите свое имя: ')
    player2 = input('Введите свое имя: ')
    first_step = random.randint(0,1)
    
    if first_step == 0: print(f'Крестиками играет {player1}')
    else: print(f'Крестиками играет {player2}')

    while not win:
        print_board(board)

        if not count % 2:
            take_input("X")
        else:
            take_input("O")

        count += 1

        if count > 4:
            tmp = get_winner(board)
            if tmp:
                print(tmp, "выиграл!")
                win = True

        if count == 9:
            print("Ничья!")
            break

    print_board(board)
main(board)            
