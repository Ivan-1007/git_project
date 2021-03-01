import bulls_and_cows_engine as game

print('Начнем игру!\nЯ загадал число ХХХХ, как Вы думаете какое это число?')

game.get_secret_number()

while True:
    player_number = None
    while True:
        player_number = input('Введите предпологаемое число\n')
        if game.is_invalid_input(player_number):
            print('Неправильный ввод, попробуйте еще ...')
        else:
            break

    if game.is_win(player_number=player_number):
        print(f'Вы выйграли, я загадал {player_number}!')
        break

    print(game.number_check(player_number=player_number), '\n Введите следуещее предпологаемое число!')
