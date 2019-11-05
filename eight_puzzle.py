from queue import PriorityQueue
import numpy as np
import copy
import time

class eight_puzzle:
    def __init__(self, initial_state, goal_state, choice):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.choice = choice

    def misplaced_heuristic(self, current_state):
        mean = np.sum(current_state == self.goal_state)
        return (9-mean)

    # https://stackoverflow.com/questions/39759721/calculating-the-manhattan-distance-in-the-eight-puzzle
    def manhattan_heuristic(self, current_state):
        copy_state = np.copy(current_state).flatten()
        return sum(abs((value - 1) % 3 - i % 3) + abs((value - 1)//3 - i//3) for i, value in enumerate(copy_state) if value)

    def heuristic(self, current_state):
        if self.choice == 1:
            return 0
        elif self.choice == 2:
            return self.misplaced_heuristic(current_state)
        elif self.choice == 3:
            return self.manhattan_heuristic(current_state)
        else:
            return 0

    # https://dbader.org/blog/priority-queues-in-python
    def search(self, initial_node):
        frontier = PriorityQueue()
        initial_node.heuristic = self.heuristic(initial_node.state)
        frontier.put((initial_node.heuristic, initial_node))
        max = frontier.qsize()
        amount_of_nodes = 1
        seen = set()
        while not frontier.empty():
            if max < frontier.qsize():
                max = frontier.qsize()
            parent_node = frontier.get()
            print('best state to expand: g(n):', parent_node[1].cost, 'h(n):', parent_node[1].heuristic)
            print(parent_node[1].state)
            if np.array_equal(parent_node[1].state, self.goal_state):
                return 'Goal Reached!', amount_of_nodes, max
            seen.add(str(parent_node[1].state))
            amount_of_nodes += 1
            for child_node in self.make_children(parent_node[1], self.find_blank(parent_node[1])):
                if (str(child_node.state)) not in seen:
                    frontier.put((child_node.heuristic + child_node.cost, child_node))

# child_node.heuristic + child_node.cost,

    # https://math.stackexchange.com/questions/293527/how-to-check-if-a-8-puzzle-is-solvable
    def is_solveable(self, current_state):
        inverse_count = 0
        check_state = current_state.flatten()
        for i in range(len(check_state)-1):
            for j in range(i+1, len(check_state)):
                if check_state[j] > check_state[i]:
                    inverse_count += 1
        return not (inverse_count % 2)

    # https://thispointer.com/find-the-index-of-a-value-in-numpy-array/
    def find_blank(self, current_state):
        blank = np.where(current_state.state == 0)
        return blank[0][0], blank[1][0]

    def make_children(self, current_state, position):
        children = [self.move_up(current_state, position), self.move_down(current_state, position), self.move_left(current_state, position), self.move_right(current_state, position)]
        return [i for i in children if i]

    def move_up(self, current_state, position):
        update_state = copy.deepcopy(current_state.state)
        new_node = TreeNode(update_state)
        new_node.cost = copy.copy(current_state.cost)

        if position[0] == 0:
            return None

        element_above = update_state[position[0]-1][position[1]]
        update_state[position[0]][position[1]] = element_above
        update_state[position[0] - 1][position[1]] = 0

        # update node cargo
        new_node.cost += 1
        new_node.heuristic = self.heuristic(update_state)
        new_node.parent = current_state

        return new_node

    def move_down(self, current_state, position):
        update_state = copy.deepcopy(current_state.state)
        new_node = TreeNode(update_state)
        new_node.cost = copy.copy(current_state.cost)

        if position[0] == 2:
            return None

        element_below = update_state[position[0] + 1][position[1]]
        update_state[position[0]][position[1]] = element_below
        update_state[position[0] + 1][position[1]] = 0

        # update node cargo
        new_node.cost += 1
        new_node.heuristic = self.heuristic(update_state)
        new_node.parent = current_state
        return new_node

    def move_left(self, current_state, position):
        update_state = copy.deepcopy(current_state.state)
        new_node = TreeNode(update_state)
        new_node.cost = copy.copy(current_state.cost)

        if position[1] == 0:
            return None

        element_left = update_state[position[0]][position[1] - 1]
        update_state[position[0]][position[1]] = element_left
        update_state[position[0]][position[1] - 1] = 0

        # update node cargo
        new_node.cost += 1
        new_node.heuristic = self.heuristic(update_state)
        new_node.parent = current_state

        return new_node

    def move_right(self, current_state, position):
        update_state = copy.deepcopy(current_state.state)
        new_node = TreeNode(update_state)
        new_node.cost = copy.copy(current_state.cost)

        if position[1] == 2:
            return None

        element_right = update_state[position[0]][position[1] + 1]
        update_state[position[0]][position[1]] = element_right
        update_state[position[0]][position[1] + 1] = 0

        # update node cargo
        new_node.cost += 1
        new_node.heuristic = self.heuristic(update_state)
        new_node.parent = current_state
        return new_node


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


# Here is the format of the puzzle states:
init_state = np.array([[8, 7, 1],
                       [6, 0, 2],
                       [5, 4, 3]])

"""init_state = np.array([[0, 1, 2],
                       [4, 5, 3],
                       [7, 8, 6]])
"""
"""init_state = np.array([[1, 7, 3],
                       [8, 0, 5],
                       [4, 6, 2]])
"""
"""init_state = np.array([[3, 2, 8],
                       [4, 5, 6],
                       [7, 1, 0]])
"""
"""goal = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 0]])
t0 = time.time()
root = TreeNode(init_state)
puzzle = eight_puzzle(root, goal, 3)
#print(puzzle.misplaced_heuristic(init_state))
results, amount, max = puzzle.search(root)
t1 = time.time()
total = t1-t0
print(results)
print('total amount of time in seconds', total)
print('amount of nodes is', amount)
print('max is', max)"""

# What to do next:
# Finally solved oh boy problem, but takes 11 minutes.
# Maybe try optimizing.
# Next thing to do, is make this so that any state can be entered
# and print out every state

if __name__ == '__main__':
    print('Enter the heuristic you would like to play with:')
    print('1. No heuristic (Uniform Cost Search)')
    print('2. Misplaced Tile Heuristic')
    print('3. Manhattan Heuristic')
    heuristic_choice = input()
    goal_state = np.array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 0]])
    print('Enter the initial state you would like played')
    print('Please enter first row: \nFor example: 3, 2, 8')
    initial_state = np.array(input())
    print('Please enter second row:')
    input_array = np.array(input())
    initial_state = np.vstack((initial_state, input_array))
    print('Please enter third row:')
    input_array = np.array(input())
    initial_state = np.vstack((initial_state, input_array))
    
    root = TreeNode(initial_state)
    puzzle = eight_puzzle(root, goal_state, heuristic_choice)
    if not puzzle.is_solveable(initial_state):
        print('This problem\n', initial_state, '\nis unsolvable. \nTry again.')
    else:
        results, node_amount, max_queue = puzzle.search(root)
        print(results)
        print('Amount of nodes expanded:', node_amount)
        print('Maximum size of queue:', max_queue)