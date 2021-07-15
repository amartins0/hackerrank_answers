

#
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts INTEGER_DOUBLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def reverse(head):
    if not head:
        return
    
    else:
            
        temp = None
        current = head
        
        while current:
            temp = current.prev            
            current.prev = current.next 
            current.next = temp
            current = current.prev           
           
            if temp:
                head = temp.prev
                
    return head 
        
        