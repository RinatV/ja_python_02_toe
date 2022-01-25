# write your code here
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


cells_inp = input('Enter cells: ')


def print_cells():
    cells = [cells_inp[i] for i in range(9)]
    cells = [c if c in ['X', 'O'] else ' ' for c in cells]
    cells = [[cells[i * 3 + j] for j in range(3)] for i in range(3)]
    print('---------')
    for i in range(3):
        print(f'| {cells[i][0]} {cells[i][1]} {cells[i][2]} |')
    print('---------')
    return cells


cells = print_cells()

while True:
    try:
        r, c = tuple(map(int, input('Enter the coordinates: ').split()))
    except:
        print('You should enter numbers!')
        continue

    if not r in [1, 2, 3] or not c in [1, 2, 3]:
        print('Coordinates should be from 1 to 3!')
        continue

    c_index = (r - 1) * 3 + c - 1

    ch = cells_inp[c_index]

    if ch == '_':
        lst = list(cells_inp)
        lst[c_index] = 'X'
        cells_inp = ''.join(lst)
        cells = print_cells()
        break
    else:
        print('This cell is occupied! Choose another one!')

# print(game_result(cells))
