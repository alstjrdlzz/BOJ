TC = int(input())
for _ in range(TC):
    lst = list(map(int, input().split())) # T + h[] 총 길이 21
    T = lst[0]
    h = lst[1:]
    
    # [1] 아무나 한 명(h[0])을 뽑아 줄의 맨 앞에 세움
    fwd = [h[0]]
    cnt = 0
    for ci in range(1, 20):
        # [2] 
        for i in range(len(fwd)):    # 자기 앞 학생들 확인
            if fwd[i] > h[ci]:                    # 키가 큰 학생이 한 명 이상 있다면 
                fwd = fwd[:i] + [h[ci]] + fwd[i:] # 그중 가장 앞에 있는 학생의 바로 앞에 세우고, 그 뒤 학생들은 뒤로 물러 섬
                cnt += (len(fwd) - (i + 1))       # cnt 증가
                break
        else:                                     # 키 큰 학생이 한 명도 없다면 맨 뒤에 세움
            fwd = fwd + [h[ci]]
            
    print(T, cnt)