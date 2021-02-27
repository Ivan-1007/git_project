from random import randint

_secret_number = []


def get_secret_number():
    global _secret_number
    number_list = list(range(0, 10))
    _secret_number.append(randint(1, 9))
    number_list.remove(_secret_number[0])
    for i in range(1, 4):
        rand_index = randint(0, 9 - i)
        _secret_number.append(number_list[rand_index])
        number_list.remove(number_list[rand_index])

    _secret_number = [1, 2, 3, 4]


def number_check(player_number):
    player_number_list = []
    for i, char in enumerate(player_number):
        player_number_list.append(int(char))
    res = {'bull': 0, 'crow': 0}
    for i in range(0, 4):
        if player_number_list[i] == _secret_number[i]:
            res['bull'] = res['bull'] + 1

    for i in range(0, 4):
        for j in range(0, 4):
            if i == j:
                continue
            if player_number_list[i] == _secret_number[j]:
                res['crow'] = res['crow'] + 1

    return res


def is_not_valid_input(player_number):
    if len(player_number) == 4:
        for i in range(0, 4):
            for j in range(0, 4):
                if i == j:
                    continue
                if player_number[i] == player_number[j]:
                    return True
                else:
                    return False
    else:
        return True


def is_win(player_number):
    player_number_list = []
    for i, char in enumerate(player_number):
        player_number_list.append(int(char))
    return player_number_list == _secret_number
