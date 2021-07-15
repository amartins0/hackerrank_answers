

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def levelOrder(root):
    if not root:
        return
    
    answer = []
    queue =  []
    queue.append(root) 
    answer.append(root)
    
    while queue:
        temp = queue[0] 
        
        if temp.left:
            queue.append(temp.left)
            answer.append(temp.left) 
        
        if temp.right:        
            queue.append(temp.right)    
            answer.append(temp.right)
        
        queue.pop(0)
    print( *answer)    