import numpy as np
import samples
import eight_puzzle
import TreeNode
import copy
import matplotlib.pyplot as plt

trivial_nodes = {'Uniform Cost Search' : [1], 'Misplaced Tiles Heuristic' : [1], 'Manhattan Heuristic' : [1]}
trivial_queue = {'Uniform Cost Search' : [1], 'Misplaced Tiles Heuristic' : [1], 'Manhattan Heuristic' : [1]}
very_easy_nodes = {'Uniform Cost Search' : [3, 4], 'Misplaced Tiles Heuristic' : [2, 2], 'Manhattan Heuristic' : [2, 2]}
very_easy_queue = {'Uniform Cost Search' : [3, 5], 'Misplaced Tiles Heuristic' : [3, 3], 'Manhattan Heuristic' : [3, 3]}
easy_nodes = {'Uniform Cost Search' : [4, 37, 10, 12, 11], 'Misplaced Tiles Heuristic' : [3, 7, 3, 4, 4], 'Manhattan Heuristic' : [3, 6, 3, 4, 4]}
easy_queue = {'Uniform Cost Search' : [4, 28, 8, 10, 10], 'Misplaced Tiles Heuristic' : [3, 7, 5, 4, 4], 'Manhattan Heuristic' : [3, 7, 5, 4, 4]}
doable_nodes = {'Uniform Cost Search' : [29, 16, 6236, 538, 189], 'Misplaced Tiles Heuristic' : [5, 5, 312, 28, 10], 'Manhattan Heuristic' : [5, 5, 58, 13, 9]}
doable_queue = {'Uniform Cost Search' : [18, 16, 4169, 361, 132], 'Misplaced Tiles Heuristic' : [4, 4, 198, 21, 8], 'Manhattan Heuristic' : [4, 4, 37, 12, 8]}
oh_boy_nodes = {'Uniform Cost Search' : [142021, 11026, 519141, 519140, 52123], 'Misplaced Tiles Heuristic' : [6761, 649, 178511, 178889, 2639], 'Manhattan Heuristic' : [591, 128, 7426, 7478, 320]}
oh_boy_queue = {'Uniform Cost Search' : [59838, 7236, 73069, 73069, 25122], 'Misplaced Tiles Heuristic' : [3845, 403, 42513, 42526, 1579], 'Manhattan Heuristic' : [367, 85, 3921, 3969, 202]}

"""plt.plot(oh_boy_queue['Uniform Cost Search'])
plt.plot(oh_boy_queue['Misplaced Tiles Heuristic'])
plt.plot(oh_boy_queue['Manhattan Heuristic'])
plt.ylabel('Maximum Queue Size')
plt.xlabel('Problem')
plt.title('Maximum Queue Size with \'Oh Boy\' Difficulty')
plt.xticks(np.arange(5), ('Problem 1', 'Problem 2', 'Problem 3', 'Problem 4', 'Problem 5'))
plt.legend(('Uniform Cost Search', 'Misplaced Tiles Heuristic', 'Manhattan Heuristic'))
plt.grid(True)
"""
labels = ['Problem 1', 'Problem 2', 'Problem 3', 'Problem 4', 'Problem 5']
x = np.arange(2)
width = 0.35
fig, ax = plt.subplots()
rects1 = ax.bar(x, very_easy_nodes['Uniform Cost Search'], width, label='Uniform Cost Search')
rects2 = ax.bar(x, very_easy_nodes['Misplaced Tiles Heuristic'], width, label='Misplaced Tile Heuristic')
rects3 = ax.bar(x, very_easy_nodes['Manhattan Heuristic'], width, label='Manhattan Heuristic')
ax.set_ylabel('Nodes Expanded')
ax.set_title('Nodes Expanded at \'Very Easy\' Difficulty')
ax.set_xticks(x)
ax.set_xticklabels(labels[0:2])
ax.legend()
ax.locator_params(nbins=10, axis='y')
ax.grid(True)
plt.savefig('charts/very-easy-bar-nodes.png', bbox_inches='tight')

