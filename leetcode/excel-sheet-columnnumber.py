class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        
        n = len(columnTitle) - 1
        c = 0
        ans = 0
        print(n)
        
        while(n>=0):
            ans = ans + (26**(c))*((ord(columnTitle[n]) - ord('A'))+1)
            n = n - 1
            c = c + 1
            
        return ans
