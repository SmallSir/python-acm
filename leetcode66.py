class Solution:
    def plusOne(self, digits):
        nums = [0 for i in range(len(digits) + 1)]
        for i in range(len(digits)-1,-1,-1):
            if i == len(digits) - 1:
                digits[i] = int(digits[i]) + 1
            if int(digits[i]) + nums[i + 1] >= 10:
                nums[i + 1] = 0
                nums[i] = 1
            else:
                nums[i + 1] += int(digits[i])
        if nums[0] == 0:
            return nums[1:]
        else:
            return nums
test = Solution()
print(test.plusOne([1,9]))
