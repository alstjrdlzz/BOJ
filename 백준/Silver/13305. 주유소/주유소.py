n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

# 누적비용, 최소가격 초기화
cost = price[0] * dist[0]
_min = price[0]
for i in range(1, n-1):
    # 최소가격 업데이트
    if _min > price[i]:
        _min = price[i]
    # 누적비용 업데이트
    cost += _min * dist[i]

print(cost)