from collections import deque
import numpy as np

class eight_puzzle:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def misplaced_heuristic(self, current_state):
        mean = np.sum(current_state == self.goal_state)
        return 9-mean

    def manhattan_heuristic(self, current_state):
        print('finish me')


    def A_star(self, heuristic):
        print('finish me')

    def g(self, ):
        print('finish me')

    # Here is what I think this function will do:
    # Make initial state root node,
    # Then make changes to the 'blank' space
    # making those changes the children of root
    # Continue this... for some time?
    # Not exactly sure when to stop making the tree.
    # I assume it'll stop making it once no more children could be made
    # or until the goal state is achieved (if possible)
    def make_tree(self):
        print('finish me')


# Tree Nodes that hold states, where each state has a list of children
# Visually, one list of children acts as a level under the parent
#                          parent
#                           /  \
#                      [child, child]
#                       /   \  /   \
#                  [children]  [children]
class TreeNode:
    def __init__(self, init_state):
        self.init_state = init_state
        self.parent = None
        self.children = []

    # Appends child onto current state
    def add_child(self, state):
        self.children.append(state)

    # Returns parent of current node
    def get_parent(self):
        return self.parent

    # Returns list of children current node has
    def get_children(self):
        return self.children

    # Grab the visual state
    def get_contents(self):
        return self.init_state

# Here is the format of the puzzle states:
init_state = np.array([[3, 2, 1],
                       [0, 8, 4],
                       [7, 5, 6]])

child_state1 = np.array([[2, 3, 1],
                       [0, 8, 4],
                       [7, 5, 6]])

child_state2 = np.array([[2, 3, 4],
                       [0, 8, 1],
                       [7, 5, 6]])


goal = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 0]])

root = TreeNode(init_state)
root_child1 = TreeNode(child_state1)
root_child2 = TreeNode(child_state2)
root.add_child(root_child1)
root.add_child(root_child2)
root_child1.parent = root
root_child2.parent = root

for children in root.get_children():
    print(children.get_contents())
#print(root_child1.get_parent().print_contents())
#print(root.get_children())

puzzle = eight_puzzle(init_state, goal)
#print('heuristic from the current node is', puzzle.misplaced_heuristic(init_state))

#print(init_state)