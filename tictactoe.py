# write your code here
cells = input('Enter cells: ')
print('---------')
for i in range(3):
    print(f'| {cells[i * 3]} {cells[i * 3 + 1]} {cells[i * 3 + 2]} |')
print('---------')
