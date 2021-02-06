class Solution:
    def plusOne(self, digits):
       
        j = len(digits) -1
        while j>=0:
            if digits[j] +1 <10:
                digits[j] += 1
                break
            else:
                digits[j] =0
                if j ==0:
                    digits.insert(0,1)
            j -=1
        print(digits)
        return digits

if __name__ == "__main__":
    sol = Solution()
    assert sol.plusOne([4,2,1]) == [4,2,2]
    assert sol.plusOne([9]) == [1,0]