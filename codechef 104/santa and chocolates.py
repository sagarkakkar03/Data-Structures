for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    x = sum(arr)
    if x < len(arr) :
        print('NO')
    elif x%len(arr)==0:
        print('YES')
    elif k == 0:
        print('NO')
    else:
        print('YES')
