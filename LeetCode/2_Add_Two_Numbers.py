# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @classmethod
    def arrToDigits(cls, arr):
        length = len(arr)
        res = 0
        number = 0
        while length:
            res += arr[length - 1] * 10 ** number
            length -= 1
            number += 1
        return res

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1, arr2 = [], []

        # extract node.value, stored each value in the list, reverse the order
        while l1.next != None:
            arr1.append(l1.val)
            l1 = l1.next
        arr1.append(l1.val)
        arr1.reverse()

        # extract node.value, stored each value in the list, reverse the order
        while l2.next != None:
            arr2.append(l2.val)
            l2 = l2.next
        arr2.append(l2.val)
        arr2.reverse()

        twoSum = Solution.arrToDigits(arr1) + Solution.arrToDigits(arr2)
        res = list(map(int, ''.join(reversed(str(twoSum)))))

        cnt = len(res)
        print(res)
        if cnt == 1:
            return ListNode(res[0], None)
        else:
            node = ListNode(res[0], ListNode(res[1]))
            cur_node = node
            node = node.next
            for i in range(2, cnt):
                if i == cnt - 1:
                    node.next = ListNode(res[i], None)
                else:
                    node.next = ListNode(res[i], ListNode(res[i + 1]))
                node = node.next
            return cur_node


