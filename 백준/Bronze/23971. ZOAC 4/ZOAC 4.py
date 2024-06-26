import sys
input = sys.stdin.readline
import math

H, W, N, M = map(int, input().split())

r = math.ceil(H/(N + 1))
c = math.ceil(W/(M + 1))
       
print(r * c)