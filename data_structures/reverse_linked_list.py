

#
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#


def reverse(head):

    
    prev = None
    current = head
        
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    head = prev
    
    
    return head
    