class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        MIN = 999999999
        for i in range(len(nums)-2):
            begin = i + 1
            end = len(nums) - 1
            while begin<end:
                sum = nums[i] + nums[begin] + nums[end]
                if abs(sum-target)<abs(MIN):
                    MIN = sum-target
                if sum == target:
                    return sum
                if sum > target:
                    end -=1
                else:
                    begin += 1
        return MIN+target

