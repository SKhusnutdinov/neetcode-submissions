class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance_map = defaultdict(int)

        for a, b, value in transactions:
            balance_map[a] -= value
            balance_map[b] += value
        
        balance_list = [amount for amount in balance_map.values() if amount]
        n = len(balance_list)

        def dfs(i):
            while i < n and balance_list[i] == 0:
                i += 1
            
            if i == n:
                return 0
            
            ans = float("inf")

            for j in range(i + 1, n):
                if balance_list[j] != 0 and (
                    (balance_list[i] > 0 and balance_list[j] < 0) or
                    (balance_list[i] < 0 and balance_list[j] > 0)
                ):
                    balance_list[j] += balance_list[i]
                    ans = min(ans, 1 + dfs(i+1))
                    balance_list[j] -= balance_list[i]
            
            return ans

        return dfs(0)