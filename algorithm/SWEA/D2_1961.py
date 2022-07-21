T = int(input())

def rotate(list):
    new_list = [ [0] * len(list) for _ in range(len(list)) ]
    for i in range(len(list)): # 0 1 2 # 3
        for j in range(len(list)):
            new_list[j][len(list) - i -1 ] = list[i][j]
    return new_list

for t in range(1, T+1):
    N = int(input())
    old_list = list()
    for n in range(N):
        old_list.append(list(map(int, input().split())))

    rotate_90 = rotate(old_list)
    rotate_180 = rotate(rotate_90)
    rotate_270 = rotate(rotate_180)

    print(f'#{t}')
    for n in range(N):
        print(''.join(map(str, rotate_90[n])), end=' ')
        print(''.join(map(str, rotate_180[n])), end=' ')
        print(''.join(map(str, rotate_270[n])))