import sys
input = sys.stdin.readline

st = "0" + input().rstrip()

dp = [0] * 5001
dp[0] = 1

flag = 0
for i in range(1, len(st)):
    if i == 1:
        if st[i] == "0":
            flag = 1
            break
        else:
            dp[i] = 1
    else:
        if st[i] == "0":
            if st[i - 1] == "1" or st[i - 1] == "2":
                dp[i] = dp[i - 2] 
            else:                                   
                flag = 1
                break        
        else:
            if 11 <= int(st[i - 1]) * 10 + int(st[i]) < 27:
                dp[i] = dp[i - 2] + dp[i - 1]
            else:
                dp[i] = dp[i - 1]

if flag:
    print(0)
else:
    print(dp[len(st) - 1] % int(1e6))