import numpy as np
import samples
import eight_puzzle
import TreeNode


# Here is the format of the puzzle states:

goal = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 0]])
tests = samples.samples()
results_from_tests = {}
for difficulty, sample_list in tests.fill_list():
    results_from_tests[difficulty] = {}
    for sample in sample_list:
        for i in range(3):
            root = TreeNode.TreeNode(sample)
            puzzle = eight_puzzle.eight_puzzle(root, goal, i+1)
            results, amount, max = puzzle.search(root)
            results_from_tests[difficulty][i+1] = [amount, max, 0]




