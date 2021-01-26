"""
@author 操松伟
@meal m18513123361@163.com
"""

"""
Question

给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 的那两个整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

你可以按任意顺序返回答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 解答：
class Solution(object):
    def __init__(self):
        pass

    def twoSum(self, nums, target):
        """
        :param nums: list[int]
        :param target: int
        :return: List[int]
        """
        # for i in nums:
        #     j = target - i
        #     start_index = nums.index(i)
        #     next_index = start_index + 1
        #     temp_nums = nums[next_index:]
        #     if j in temp_nums:
        #         return [nums.index(i), next_index + temp_nums.index(j)]

        # 优化后
        dict = {}

        for i in range(len(nums)):
            if target - nums[i] not in dict:
                dict[nums[i]] = i
            else:
                return [dict[target - nums[i]], i]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution().twoSum(nums, target)
    print(solution)
