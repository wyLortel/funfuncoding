n=int(input())
dp = [1]*10
dp2 = [1]*10
dp[0]=0
for _ in range(n-1):
    for i in range(10):
        if i==0:
            dp2[i]=dp[i+1]
        elif i==9:
            dp2[i]=dp[i-1]
        else:
            dp2[i]=dp[i-1]+dp[i+1]
    dp = dp2.copy()
