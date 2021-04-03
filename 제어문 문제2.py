sum = 0
i = 0

while i <= 100:
    if i %4 ==0:
        sum = sum+i

    i = i+1

print('1부터 100까지의 자연수 중 4의 배수의 합 : %d' % (sum))