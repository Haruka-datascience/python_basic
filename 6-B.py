n = int(input())
total = [(x,y) for x in ['S', 'H', 'C', 'D'] for y in range(1,14)]
taro = []
for i in range(n):
    a,b = input().split()
    taro.append((a, int(b)))
for i in total:
    if i not in taro:
        print(*i)
