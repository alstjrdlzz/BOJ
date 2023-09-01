import sys
input = sys.stdin.readline


n = int(input())

meetings = []
for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))
    
meetings.sort(key=lambda x: (x[1], x[0]))

now = 0
answer = 0
for meeting in meetings:
    if meeting[0] >= now:
        answer += 1
        now = meeting[1]
        
print(answer)