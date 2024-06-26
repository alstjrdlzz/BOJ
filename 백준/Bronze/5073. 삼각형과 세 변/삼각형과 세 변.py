import sys
input = sys.stdin.readline

while True:
    lst = list(map(int, input().split()))
    lst.sort()
    # 종료 조건
    if lst[0] == 0:
        break
    
    if lst[2] >= sum(lst[0:2]): # 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면 삼각형의 조건을 만족 X 
        print("Invalid")
        
    elif len(set(lst)) == 1:
        print("Equilateral")
        
    elif len(set(lst)) == 2:
        print("Isosceles")
        
    elif len(set(lst)) == 3:
        print("Scalene")     