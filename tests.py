import numpy as np
import samples
import eight_puzzle
import TreeNode
import copy


# Here is the format of the puzzle states:

goal = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 0]])
tests = samples.samples()
results_from_tests = {}
lists = tests.fill_list()
write_to = open('stat_results.txt', 'w')
for problem in tests.fill_list():
    difficulty = problem[0]
    results_from_tests[difficulty] = {}
    amount_of_nodes = []
    maximum_queue_size = []
    for i in range(3):
        results_from_tests[difficulty][i+1] = ([], [])
        for sample in problem[1]:
            root = TreeNode.TreeNode(sample)
            puzzle = eight_puzzle.eight_puzzle(root, goal, i+1)
            results, depth, amount, max = puzzle.search(root)
            results_from_tests[difficulty][i+1][0].append(amount)
            results_from_tests[difficulty][i+1][1].append(max)

for difficulty in results_from_tests.keys():
    print('Difficulty for this level is', difficulty)
    for search_algo in results_from_tests[difficulty]:
        print(search_algo, 'has node expansion of', results_from_tests[difficulty][search_algo][0])
        print(search_algo, 'has max queue size of', results_from_tests[difficulty][search_algo][1])
        print('The average amount of nodes expanded is',
              sum(results_from_tests[difficulty][search_algo][0]) / len(results_from_tests[difficulty][search_algo][0]))
        print('The average amount of maximum queue size is',
              sum(results_from_tests[difficulty][search_algo][1]) / len(results_from_tests[difficulty][search_algo][1]))

        write_to.write(str(search_algo) + ' has node expansion of ' + str(results_from_tests[difficulty][search_algo][0]) + '\n')
        write_to.write(str(search_algo) + ' has max queue size of ' + str(results_from_tests[difficulty][search_algo][1]) + '\n')
        write_to.write('The average amount of nodes expanded is ' + str(sum(results_from_tests[difficulty][search_algo][0]) / len(results_from_tests[difficulty][search_algo][0])) + '\n')
        write_to.write('The average amount of maximum queue size is ' + str(sum(results_from_tests[difficulty][search_algo][1]) / len(results_from_tests[difficulty][search_algo][1])) + '\n')
write_to.close()