class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        x = {}
        y = {}

        
        for i in s:
            if i not in x:
                x[i] = 1
            else:
                x[i] = x[i] + 1
                
        for i in t:
            if i not in y:
                y[i] = 1
            else:
                y[i] = y[i] + 1
                
        if x == y:
            return True
        else:
            return False

#other solution

    def isAnagram(self, s: str, t: str) -> bool:
        x = [0]*26
        
        for i in s:
            
            x[ord(i) - ord('a')] = x[ord(i) - ord('a')] + 1
                
        print(x)
        
        for i in t:
            
            x[ord(i) - ord('a')] = x[ord(i) - ord('a')] - 1
                
        print(x)
        
        if all(v == 0 for v in x):
            return True
        else:
            return False
