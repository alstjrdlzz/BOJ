import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

lst = lst1 + lst2
lst.sort()
    
print(*lst)