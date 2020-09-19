class Solution:

    def new21Game(self, N: int, K: int, W: int) -> float:

        dp = [0.0] * (K + W)
        for k in range(K, min(N + 1, K + W)):
            dp[k] = 1.0

        S = min(N - K + 1, K + W)
        for k in range(K - 1, -1, -1):
            dp[k] = S / float(W)
            S += dp[k] - dp[k + W]

        return dp[0]


if __name__ == '__main__':
    s = Solution()
    print(s.new21Game(21, 17, 10))