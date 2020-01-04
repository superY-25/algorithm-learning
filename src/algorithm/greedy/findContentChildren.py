

class Solution:
    def findContentChildren(self, g: list, s: list) -> int:
        g = sorted(g)
        s = sorted(s)
        i, j = 0, 0
        n_g = len(g)
        n_s = len(s)
        ret = 0
        while i < n_g and j < n_s:
            if s[j] >= g[i]:
                i += 1
                j += 1
                ret += 1
            else:
                j += 1
        return ret