import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_solution, calculate_happiness, calculate_happiness_for_room, calculate_stress_for_room
import sys
from queue import PriorityQueue


def solve(G, s):
    """
    Args:
        G: networkx.Graph
        s: stress_budget
    Returns:
        D: Dictionary mapping for student to breakout room r e.g. {0:2, 1:0, 2:1, 3:2}
        k: Number of breakout rooms
    """

    # TODO: your code here!
    n = len(G)
    D = {}
    k = 0
    bestH = 0

    V = G.nodes()
    E = G.edges()
    totalStress = 0
    S = [] # list of edges sorted by heuristic
    pq = PriorityQueue()
    for e in E:
        #print(G.get_edge_data(e[0], e[1]))
        totalStress += G.get_edge_data(e[0], e[1])['stress']
        heuristic = G.get_edge_data(e[0], e[1])['happiness'] / G.get_edge_data(e[0], e[1])['stress']
        pq.put((heuristic, e))

    while not pq.empty():
            S.append(pq.poll)

        
    avgStress = totalStress / G.size()
    avgNumBreakoutSize = s/avgStress
    numBreakoutRooms = G.number_of_nodes()/avgNumBreakoutSize
        
    S = {} # dictionary of edges sorted by happiness/stress

    # TODO: make sorted list of edges based on happiness/stress

    

    # TODO: solve using sort_into_n_rooms with varying n



    for e in D:
        print(e, D[e])
    return D, k

def sort_into_n_rooms(G, s, n):
    """Returns a dict of student mapping to breakout room"""
    D = {}

    return D


def sorted_k_partitions(seq, k):
    """Returns a list of all unique k-partitions of `seq`.

    Each partition is a list of parts, and each part is a tuple.

    The parts in each individual partition will be sorted in shortlex
    order (i.e., by length first, then lexicographically).

    The overall list of partitions will then be sorted by the length
    of their first part, the length of their second part, ...,
    the length of their last part, and then lexicographically.
    https://stackoverflow.com/questions/39192777/how-to-split-a-list-into-n-groups-in-all-possible-combinations-of-group-length-a
    """
    n = len(seq)
    groups = []  # a list of lists, currently empty

    def generate_partitions(i):
        if i >= n:
            yield list(map(tuple, groups))
        else:
            if n - i > k - len(groups):
                for group in groups:
                    group.append(seq[i])
                    yield from generate_partitions(i + 1)
                    group.pop()

            if len(groups) < k:
                groups.append([seq[i]])
                yield from generate_partitions(i + 1)
                groups.pop()

    result = generate_partitions(0)

    return result


# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in

if __name__ == '__main__':
     assert len(sys.argv) == 2
     path = sys.argv[1]
     G, s = read_input_file(path)
     D, k = solve(G, s)
     #assert is_valid_solution(D, G, s, k)
     #print("Total Happiness: {}".format(calculate_happiness(D, G)))
     #write_output_file(D, '20.out')


# For testing a folder of inputs to create a folder of outputs, you can use glob (need to import it)
# if __name__ == '__main__':
#     inputs = glob.glob('file_path/inputs/*')
#     for input_path in inputs:
#         output_path = 'file_path/outputs/' + basename(normpath(input_path))[:-3] + '.out'
#         G, s = read_input_file(input_path, 100)
#         D, k = solve(G, s)
#         assert is_valid_solution(D, G, s, k)
#         cost_t = calculate_happiness(T)
#         write_output_file(D, output_path)
