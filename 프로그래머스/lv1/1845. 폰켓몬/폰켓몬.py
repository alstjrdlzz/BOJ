import collections

def solution(num):
    answer = int(min(len(num)/2 , len(list(collections.Counter(num)))))

    return answer