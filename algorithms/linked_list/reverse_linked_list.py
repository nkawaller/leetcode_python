"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Leetcode solution
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            head.next, prev, head = prev, head, head.next
        return prev


# Fully implemented linked list with reverse function

class LinkedList:

    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def getSize(self):
        return self.size

    def addNode(self, val):
        newNode = ListNode(val, self.head)
        self.head = newNode
        self.size += 1

    def reverse(self):
        curr = self.head
        prev = None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        self.head = prev

    def printList(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next


if __name__ == '__main__':

    l = LinkedList()
    for i in range(1, 6):
        l.addNode(i)
    l.printList()
    print('--------------')
    l.reverse()
    l.printList()
