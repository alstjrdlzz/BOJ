import sys
input = sys.stdin.readline


n = int(input())
S = list(map(int, input().split()))

start = 0
end = n - 1

answer = abs(S[start] + S[end])
answer_start = start
answer_end = end

while (start < end):
    temp = S[start] + S[end]
    if abs(temp) < answer:
        answer_start = start
        answer_end = end
        answer = abs(temp)
       
    if temp < 0:
        start += 1
    else:
        end -= 1

print(S[answer_start], S[answer_end])