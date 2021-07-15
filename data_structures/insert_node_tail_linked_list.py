

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    if not head:
        return SinglyLinkedListNode(data)
    
    else:
        cur = head
        new_node = SinglyLinkedListNode(data)
        
        while cur.next:
            cur = cur.next
        
        cur.next = new_node
        
        
    return head
