n = int(input())
data = list(map(int, input().split()))

sorted_data = sorted(data)

print(sorted_data[0], sorted_data[-1])