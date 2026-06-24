"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        start=node
        mapping={}
        stack=[start]
        seen=set()
        seen.add(start)

        while stack:
            node=stack.pop()
            mapping[node]= Node(val=node.val)

            for nei in node.neighbors:
                if nei not in seen:
                    stack.append(nei)
                    seen.add(nei)

        for old,new in mapping.items():
            for nei in old.neighbors:
                new_nei=mapping[nei]
                new.neighbors.append(new_nei)
        return mapping[start]