def ceil(x, y):
    return (x + y - 1) // y

class Solution:
    def minOperations(self, S, K):
        N = len(S)
        Z = S.count("0")
        if N == K:
            return 0 if Z == 0 else 1 if Z == N else -1

        ans = inf
        if Z % 2 == 0:
            M = max(ceil(Z, K), ceil(Z, N - K))
            M += M & 1
            ans = min(ans, M)
        if Z % 2 == K % 2:
            M = max(ceil(Z, K), ceil(N - Z, N - K))
            M += M & 1 == 0
            ans = min(ans, M)
        return ans if ans < inf else -1

#####################################################################################

from sortedcontainers import SortedList
from collections import deque

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        cnt0 = s.count('0')
        
        if cnt0 == 0:
            return 0
        
        ts = [SortedList(range(0, n + 1, 2)), SortedList(range(1, n + 1, 2))]
        ts[cnt0 % 2].remove(cnt0)
        
        q = deque([cnt0])
        ans = 0
        
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == 0:
                    return ans
                
                lo = cur + k - 2 * min(cur, k)
                hi = cur + k - 2 * max(0, k - (n - cur))
                
                t = ts[lo % 2]
                idx = t.bisect_left(lo)
                while idx < len(t) and t[idx] <= hi:
                    nxt = t[idx]
                    t.remove(nxt)
                    q.append(nxt)
            ans += 1
        
        return -1
