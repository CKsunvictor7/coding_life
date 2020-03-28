class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ten_flag = 1
        result = []
        for d in digits[::-1]:
            d = d + ten_flag
            if d == 10:
                result.append(0)
                ten_flag = 1
            else:
                result.append(d)
                ten_flag = 0
        
        if ten_flag == 1:
            result.append(1)
            
        return result[::-1]
