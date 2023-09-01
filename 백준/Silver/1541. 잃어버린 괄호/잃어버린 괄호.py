import sys
input = sys.stdin.readline


raw = input().split("-")

processed = []
for i in range(len(raw)):
    processed.append(sum(list(map(int, raw[i].split("+")))))
    
answer = processed[0]
for i in range(1, len(processed)):
    answer -= processed[i]
    
print(answer)