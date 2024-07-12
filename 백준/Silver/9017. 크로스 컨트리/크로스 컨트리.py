import sys
input = sys.stdin.readline
from collections import Counter

TC = int(input())
for _ in range(TC):
    N = int(input())
    lst = list(map(int, input().split()))
    
    #[1] 팀별 선수 수 계산 -> 여섯명이 안되는 팀 제외
    counter = Counter(lst)
    for team in counter:
        if counter[team] < 6:
            lst = [v for v in lst if v != team]
    
    #[2] 팀별 점수 계산
    arr = [[] for _ in range(len(counter) + 1)]
    for i in range(len(lst)): # 팀 번호: [선수1 점수, 선수2 점수, ...]
        arr[lst[i]].append(i + 1)
                     
    scores = [] # [(팀 번호, 팀 점수, 5번째 선수 개인 점수)]
    for team in set(lst):
        score = 0
        for i in range(4):
            score += arr[team][i] # 상위 4명 점수 합
        fifth = arr[team][4] # 5번째 선수 점수  
        scores.append([team, score, fifth])
    
    #[3] 우승팀 선정
    scores.sort(key = lambda x: (x[1], x[2])) # 팀 점수, 5번째 선수 개인 점수를 key로 오름차순 정렬
    print(scores[0][0]) 