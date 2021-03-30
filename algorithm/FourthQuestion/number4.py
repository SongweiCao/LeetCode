"""
@author 操松伟
@meal m18513123361@163.com
"""

"""
Question

4. 寻找两个正序数组的中位数

给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

示例1：
    输入：nums1 = [1,3], nums2 = [2]
    输出：2.00000
    解释：合并数组 = [1,2,3] ，中位数 2
    
示例2：
    输入：nums1 = [1,2], nums2 = [3,4]
    输出：2.50000
    解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

示例 3：
    输入：nums1 = [0,0], nums2 = [0,0]
    输出：0.00000

示例 4：
    输入：nums1 = [], nums2 = [1]
    输出：1.00000

示例 5：
    输入：nums1 = [2], nums2 = []
    输出：2.00000

提示：
    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106

进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2, ):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 此方法不python中的list处理方法
        # n1 = len(nums1)
        # n2 = len(nums2)
        # # 保证 n1 < n2
        # if n1 > n2:
        #     nums1, nums2 = nums2, nums1
        #     n1, n2, = n2, n1
        #
        # iMin = 0
        # iMax = n1
        # halfLen = (n1 + n2 + 1) // 2
        # while iMin <= iMax:
        #     i = (iMin + iMax) // 2
        #     j = halfLen - i
        #     if i > 0 and j < n2 and nums1[i - 1] > nums2[j]:
        #         iMax = i - 1
        #     elif i < n1 and j > 0 and nums2[j - 1] > nums1[i]:
        #         iMin = i + 1
        #     else:
        #         # 此时已经寻找到了满足条件的i
        #         # 寻找maxLeft
        #         if i == 0:
        #             maxLeft = nums2[j - 1]
        #         elif j == 0:
        #             maxLeft = nums1[i - 1]
        #         else:
        #             maxLeft = max(nums1[i - 1], nums2[j - 1])
        #
        #         # 一定要先判断是奇数要直接返回，因为可能存在 m+n 为1时，这时如果再计算minRigh 就会内存溢出
        #         if (n1 + n2) % 2 == 1:
        #             return maxLeft
        #
        #         # 虚招minRight
        #         if i == n1:
        #             minRight = nums2[j]
        #         elif j == n2:
        #             minRight = nums1[i]
        #         else:
        #             minRight = min(nums1[i], nums2[j])
        #         return (maxLeft + minRight) / 2.0
        self.nums = nums1 + nums2
        self.nums.sort()
        size = len(self.nums)

        if size % 2 == 1:
            return self.nums[size // 2]
        if size % 2 == 0:
            return (self.nums[size // 2 - 1] + self.nums[size // 2]) / 2


a = Solution()
b = [1, 3, 4, 5]
c = [2, 4, 5, 9]
print(a.findMedianSortedArrays(b, c))
