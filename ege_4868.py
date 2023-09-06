def transformation(n):
    sum1 = 0
    for i in str(n):
        if int(i) % 2 == 0:
            sum1 += int(i)
    sum2 = 0
    if len(str(n)) > 1:
        for i in range(1, len(str(n)), 2):
            sum2 += int(str(n)[::1][i])
    return sum1 - sum2

for i in range(1, 999999):
    if transformation(i) == 13:
        print(i)
        break
