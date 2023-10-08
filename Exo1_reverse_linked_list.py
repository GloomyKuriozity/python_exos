"""
PROGRAM NAME - reverse_linked_list
PROGRAMMER - Kuriozity
LANGUAGE - Python 
SYSTEM - Windows 11
DATE - Completed 10/08/2023
NDP - None :)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    """
    Reverse a linked list and returns the head of the list.
    
    Args:
        head (int) : pointer head of the list
    
    Returns:
        prev (int): new pointer head of the list
    """

    prev = None
    current = head
    next_node = None

    n=0
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

