"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        mapping = {}

        def dfs(node):
            clone = Node(node.val)
            mapping[node] = clone
            for neighbor in node.neighbors:
                if mapping.get(neighbor):
                    mapping[node].neighbors.append(mapping[neighbor])
                else:
                    dfs(neighbor)
                    mapping[node].neighbors.append(mapping[neighbor])

        dfs(node)
        return mapping[node]