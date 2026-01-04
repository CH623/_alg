def edit_distance(word1, word2):
    m = len(word1)
    n = len(word2)

    # 建立 DP 表
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 初始化
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # 填表
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i][j - 1] + 1,      # 插入
                    dp[i - 1][j] + 1,      # 刪除
                    dp[i - 1][j - 1] + 1   # 取代
                )

    return dp[m][n]

print(edit_distance("horse", "ros"))
