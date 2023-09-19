import sys
input = sys.stdin.readline


def solution(forms):
    last = forms[0]
    
    if last == "c":
        answer = 26
    else:
        answer = 10
        
    for i in range(1, len(forms)):
        cur = forms[i]
        if last == "c" and cur == "c":
            answer *= 25
        elif last == "c" and cur == "d":
            answer *= 10
        elif last == "d" and cur == "d":
            answer *= 9
        else:
            answer *= 26
        last = cur
    return answer
            

f = input().strip()

print(solution(f))
