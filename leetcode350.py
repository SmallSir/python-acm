class Solution:
    def intersect(self, nums1, nums2):
        a = set()
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums2[j] == nums1[i] and j not in a:
                    a.add(j)
                    break
        qua = []
        for i in a:
            qua.append(nums2[i])
        return qua
test = Solution()
print(test.intersect([1,2],[2,1]))
