import numpy as np

# Tree Nodes that hold states, where each state has a list of children
# Visually, one list of children acts as a level under the parent
#                          parent
#                           /  \
#                      [child, child]
#                       /   |  |   \
#                  [children]  [children]
# _____________________________________________________________________
class TreeNode:
    def __init__(self, state):
        self.state = state
        self.cost = 0
        self.heuristic = 0
        self.parent = None
        self.children = []

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.cost + self.heuristic == other.cost + other.heuristic
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.cost + self.heuristic < other.cost + other.heuristic
        return NotImplemented

    def __hash__(self):
        return hash(np.array2string(self.state))
