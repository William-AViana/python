for i in range(1, 11):
    print('i = {}'.format(i))

for j in range(10):
    print(f'j = {j}')

for x in range(0, 11):
    for y in range(0, 11):
        print(f'{x} x {y} = {x * y}')
        if y == 10:
            print('==========')
