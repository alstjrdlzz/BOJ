import sys
input = sys.stdin.readline
from collections import defaultdict

T = int(input())
for _ in range(T):
    # 팀의 개수, 문제의 개수, 당신 팀의 ID, 로그 엔트리의 개수
    n, k, t, m = map(int, input().split())
    # 팀별: [최종점수, 제출횟수, 마지막제출시간]
    dict_ = defaultdict(lambda: [0, 0, 0])
    # 점수 테이블 (팀 * 문제)
    tb = [[0] * (k + 1) for _ in range(n + 1)]
    # 서버에 제출된 로그 순회
    for i in range(m):
        tid, qnum, score = map(int, input().split())
        # 점수
        tb[tid][qnum] = max(tb[tid][qnum], score)
        # 제출횟수
        dict_[tid][1] += 1
        # 마지막제출시간
        dict_[tid][2] = i
    # 팀별 최종점수
    for i in range(1, n + 1):
        dict_[i][0] = sum(tb[i])
    # 당신 팀(t)의 랭크
    rank = 1
    for i in range(1, n + 1):
        if i == t:
            continue
        if dict_[i][0] > dict_[t][0]:
            rank += 1
        elif dict_[i][0] == dict_[t][0]:
            if dict_[i][1] < dict_[t][1]:
                rank += 1
            elif dict_[i][1] == dict_[t][1]:
                if dict_[i][2] < dict_[t][2]:
                    rank += 1       
    print(rank)