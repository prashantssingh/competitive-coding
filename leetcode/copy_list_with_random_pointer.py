# PROBLEM DESCRIPTION:
# A linked list is given such that each node contains an additional random pointer which could point 
# to any node in the list or null.
#
# Return a deep copy of the list.
#
# The Linked List is represented in the input/output as a list of n nodes. Each node is represented 
# as a pair of [val, random_index] where:
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
#
# Refer Link: https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        nodesSeen, ptr1 = dict(), head
        copyHead = Node(ptr1.val, None, None)
        ptr2 = copyHead
        nodesSeen[ptr1] = ptr2
        ptr1 = ptr1.next
        while ptr1:
            ptr2.next = Node(ptr1.val, None, None)
            ptr2 = ptr2.next
            nodesSeen[ptr1] = ptr2
            ptr1 = ptr1.next
        
        ptr1, ptr2 = head, copyHead
        while ptr1:
            if ptr1.random:
                ptr2.random = nodesSeen[ptr1.random]
            ptr1, ptr2 = ptr1.next, ptr2.next
        
        return copyHead