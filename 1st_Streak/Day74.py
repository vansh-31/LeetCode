
# Problem : Check Completeness of a Binary Tree
# Problem Statement : Given the root of a binary tree, determine if it is a complete binary tree.
# In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
from collections import deque
class Solution:
    def isCompleteTree(self, root ) -> bool:
                
        traversal_queue = deque( [ root ] )
        prev_node = root

        while traversal_queue:        
            cur_node = traversal_queue.popleft()
            if cur_node:

                if not prev_node:
                    return False
                
                traversal_queue.append( cur_node.left )
                traversal_queue.append( cur_node.right )
                
            prev_node = cur_node
            
        return True