class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result


if __name__ == "__main__":
    l1_values = list(map(int, input().rstrip().split()))
    l2_values = list(map(int, input().rstrip().split()))

    l1 = ListNode(l1_values[0])
    current = l1
    for val in l1_values[1:]:
        current.next = ListNode(val)
        current = current.next

    l2 = ListNode(l2_values[0])
    current = l2
    for val in l2_values[1:]:
        current.next = ListNode(val)
        current = current.next

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    while result:
        print(result.val, end=" ")
        result = result.next
