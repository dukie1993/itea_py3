import random

# заготовки для робочого поля
up = """+-----+-----+-----+-----+
|     |     |     |     |"""

mid = """|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |"""

bot = """|     |     |     |     |
+-----+-----+-----+-----+"""

def get_new_random():
    line = list(range(16))
    random.shuffle(line)
    return line

def print_board(new_game):
    print(up)
    for i in range (0, 16):
        if new_game[i]<10:
            if new_game[i] == 0:
                print('| ', end = '  ')
            else:
                print('| '+str(new_game[i])+' ', end = '  ')
        else:
            num = str(new_game[i])
            print('| '+num[0]+''+num[1]+' ', end = ' ')
        if i == 3 or i == 7 or i == 11:
            print('|')
            print(mid) 
    print('|')
    print(bot)

def answer():
    while True:
        text = input('Введіть число от 1 до 15:')
        if text.isdigit() == False:
            print('Вводьте тільки цілі числа!')
        elif 15<int(text) or int(text)<0:
            print('Немає такого числа на ігровому полі!')
        else:
            return int(text)
            

def possible_moves(new_game):
    moves = []
    index = new_game.index(0)
    if index == 0:
        moves.append(new_game[1])
        moves.append(new_game[4])
    elif index == 1:
        moves.append(new_game[0])
        moves.append(new_game[2])
        moves.append(new_game[5])
    elif index == 2:
        moves.append(new_game[1])
        moves.append(new_game[3])
        moves.append(new_game[6])
    elif index == 3:
        moves.append(new_game[2])
        moves.append(new_game[7])
    elif index == 4:
        moves.append(new_game[0])
        moves.append(new_game[5])
        moves.append(new_game[8])
    elif index == 5:
        moves.append(new_game[1])
        moves.append(new_game[4])
        moves.append(new_game[6])
        moves.append(new_game[9])
    elif index == 6:
        moves.append(new_game[2])
        moves.append(new_game[5])
        moves.append(new_game[7])
        moves.append(new_game[10])
    elif index == 7:
        moves.append(new_game[3])
        moves.append(new_game[6])
        moves.append(new_game[11])
    elif index == 8:
        moves.append(new_game[4])
        moves.append(new_game[9])
        moves.append(new_game[12])
    elif index == 9:
        moves.append(new_game[5])
        moves.append(new_game[8])
        moves.append(new_game[10])
        moves.append(new_game[13])
    elif index == 10:
        moves.append(new_game[6])
        moves.append(new_game[9])
        moves.append(new_game[11])
        moves.append(new_game[14])
    elif index == 11:
        moves.append(new_game[7])
        moves.append(new_game[10])
        moves.append(new_game[15])
    elif index == 12:
        moves.append(new_game[8])
        moves.append(new_game[13])
    elif index == 13:
        moves.append(new_game[9])
        moves.append(new_game[12])
        moves.append(new_game[14])
    elif index == 14:
        moves.append(new_game[10])
        moves.append(new_game[13])
        moves.append(new_game[15])
    else:
        moves.append(new_game[11])
        moves.append(new_game[14])

    return moves




# основний код гри
win = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
new_game = get_new_random()
print_board(new_game)

while True:
    moves = possible_moves(new_game)
    move_num = answer()
    if move_num in moves:
        index_move = new_game.index(move_num)
        index_0 = new_game.index(0)
        new_game[index_0] = move_num
        new_game[index_move] = 0
        print_board(new_game)
    else:
        print('Це число не можна перемістити!')
    if new_game == win:
        print('Вітаю! Ви виграли!')
        break
    else:
        None
    