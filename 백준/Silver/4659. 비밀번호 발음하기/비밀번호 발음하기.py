import sys
input = sys.stdin.readline

def con1(s):
    """
    조건 1: 모음(a,e,i,o,u) 하나를 반드시 포함
    return
        하나라도 포함 하면 1
        하나도 포함하지 않으면 0
    """
    for ch in s:
        if ch in "aeiou":
            return 1
    return 0

def con2(s):
    """
    조건 2: 모음이 3개 혹은 자음이 3개 연속으로 오면 안 됨
    return
        모음이 3개 혹은 자음이 3개 연속으로 오지 않으면 1
        모음이 3개 혹은 자음이 3개 연속으로 오면 0
    """
    cnt = 1
    old = s[0]
    for ch in s[1:]:
        if (ch in "aeiou") == (old in "aeiou"):
            cnt += 1
        else:
            cnt = 1
            old = ch
            
        if cnt == 3:
            return 0
    return 1
              
def con3(s):
    """
    조건 3: 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용
    return
        연속으로 나온 같은 글자가 "e" 나 "o"가 아니면 0
        그 이외의 경우 1
    """
    old = s[0]
    for ch in s[1:]:
        if ch == old and ch != "e" and ch != "o":
            return 0
        else:
            old = ch
    return 1
        
    
while 1:
    s = input().rstrip()
    if s == "end":
        break
        
    if con1(s) and con2(s) and con3(s):
        print(f"<{s}> is acceptable.")
    else:
        print(f"<{s}> is not acceptable.")