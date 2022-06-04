class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        s = [str(i) for i in digits]
        num = int("".join(s))
        num = num + 1
        
        return [int(i) for i in str(num)]

      
      
 #other solution
   def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        k = 0
    
        while(digits[n] == 9 and n >= 0):
            digits[n] = 0
            n = n - 1

        if(n==-1):
            digits.insert(0,1)
        else:
            digits[n] += 1 
        
        return digits
