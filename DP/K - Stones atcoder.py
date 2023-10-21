import sys
sys.setrecursionlimit(10**6)
n, k = map(int, input().split())
arr = list(map(int, input().split()))
stones = [-1 for i in range(k+1)]
def winning(k):
    global arr, stones
    if stones[k] != -1:
        return stones[k]
    for i in arr:
        if k- i == 0:
            stones[k] = True
            return True
        elif k- i > 0:
            if not winning(k-i):
                stones[k] = True
                return True
    stones[k] = False
    return False
print('First' if winning(k) else 'Second')
