# write your code here
cells = input('Enter cells: ')
cells = [cells[i] for i in range(9)]
cells = [[cells[i * 3 + j] for j in range(3)] for i in range(3)]
print('---------')
for i in range(3):
    print(f'| {cells[i][0]} {cells[i][1]} {cells[i][2]} |')
print('---------')


def is_user_win(u, c):
    if c[0][0] == c[0][1] == c[0][2] == u:
        return True
    if c[1][0] == c[1][1] == c[1][2] == u:
        return True
    if c[2][0] == c[2][1] == c[2][2] == u:
        return True
    if c[0][0] == c[1][1] == c[2][2] == u:
        return True
    if c[0][2] == c[1][1] == c[2][0] == u:
        return True
    if c[0][0] == c[1][0] == c[2][0] == u:
        return True
    if c[0][1] == c[1][1] == c[2][1] == u:
        return True
    if c[0][2] == c[1][2] == c[2][2] == u:
        return True
    return False


def user_count(u, c):
    cnt = 0
    for i in range(3):
        for j in range(3):
            if c[i][j] == u:
                cnt += 1
    return cnt


def game_result(c):
    if abs(user_count('X', c) - user_count('O', c)) > 1:
        return 'Impossible'
    if is_user_win('X', c) and is_user_win('O', c):
        return 'Impossible'
    if is_user_win('X', c):
        return 'X wins'
    if is_user_win('O', c):
        return 'O wins'
    if user_count('X', c) + user_count('O', c) == 9:
        return 'Draw'

    return 'Game not finished'


print(game_result(cells))
