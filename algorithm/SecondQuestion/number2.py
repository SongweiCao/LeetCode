"""
@author 操松伟
@meal m18513123361@163.com
"""

"""
Question

给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0开头。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 解答：
class ListNode(object):
    """
    定义链表
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListNode_handle(object):
    def __init__(self):
        self.cur_node = None

    def add(self, data):
        """
        add a new node pointed to previous node
        :param data:
        :return:
        """
        node = ListNode()
        node.val = data
        node.next = self.cur_node
        self.cur_node = node
        return node

    def print_ListNode(self, node):
        while node:
            print('node:', node, 'value', node.val, 'next', node.next)
            print(node.val)
            node = node.next

    def _reverse(self, nodelist):
        list = []
        while nodelist:
            list.append(nodelist.val)
            nodelist = nodelist.next
        result = ListNode()
        result_handle = ListNode_handle()
        for i in list:
            result = result_handle.add(i)
        return result

    def get_list(self, nodelist):
        list = []
        while nodelist:
            list.append(nodelist.val)
            nodelist = nodelist.next
        return list


class Solution(object):
    def addTowNumbers(self, l1, l2):
        if l1 == None:
            return l2

        if l2 == None:
            return l1

        carry = 0
        dummy = ListNode(0)
        p = dummy

        while l1 and l2:
            p.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
            p = p.next

        if l2:
            while l2:
                p.next = ListNode((l2.val + carry) % 10)
                carry = (l2.val + carry) // 10
                l2 = l2.next
                p = p.next

        if l1:
            while l1:
                p.next = ListNode((l1.val + carry) % 10)
                carry = (l1.val + carry) // 10
                l1 = l1.next
                p = p.next

        if carry == 1:
            p.next = ListNode(1)
        return dummy.next


ListNode_1 = ListNode_handle()
l1 = ListNode()
l1_list = [2, 4, 3]
for i in l1_list:
    l1 = ListNode_1.add(i)

ListNode_2 = ListNode_handle()
l2 = ListNode()
l2_list = [5, 6, 4]
for i in l2_list:
    l2 = ListNode_2.add(i)

l1 = ListNode_1._reverse(l1)
l2 = ListNode_2._reverse(l2)
result = Solution().addTowNumbers(l1, l2)
result_node = ListNode_handle().print_ListNode(result)
print(result_node)

a = "a1234"
print(isinstance(a, str))
