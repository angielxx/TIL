T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    cases = list()
    for n in range(N):
        cases.append(list(map(int, input().split())))

    sum_list = list()
    for i in range(N - M + 1):
        sum = 0
        for j in range(N - M - 1):
            for k in range(M):
                sum += cases[i][j+k]
        sum_list.append(sum)
    sum_list.sort(reverse = True)
    print(f'#{t} {sum_list[0]}')

    """
    [0][0] + [0][1] + [0][2] + [1][0] + [1][1] + [1][2]
    """