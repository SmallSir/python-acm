class Solution(object):
    def sortColors(self, nums):
        one = two = three = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                one += 1
            elif nums[i] == 1:
                two += 1
            else:
                three += 1
        for i in range(len(nums)):
            if i <one:
                nums[i] = 0
            elif i >=one and i < one + two:
                nums[i] = 1
            else:
                nums[i] = 2
        return nums
