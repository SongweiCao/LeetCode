"""
@author 操松伟
@meal m18513123361@163.com
"""

"""
Question

3. 无重复字符的最长子串

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 解答
class Solution:
    def lengthOfLongestSubstring(self, s):
        occ = set()
        n = len(s)
        rk, ans = -1, 0
        for i in range(n):
            print("i: {0}".format(i))
            if i != 0:
                print("occ.remove(s[i - 1]): {0}".format(s[i - 1]))
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                print("rk: {0}".format(rk))
                print('n: {0}'.format(n))
                print('s[rk + 1]: {0}'.format(s[rk + 1]))
                print("occ: {0}".format(occ))
                occ.add(s[rk + 1])
                rk += 1
            ans = max(ans, rk - i + 1)
        return ans


s = "abcabcbb"
S = Solution().lengthOfLongestSubstring(s)
print(S)