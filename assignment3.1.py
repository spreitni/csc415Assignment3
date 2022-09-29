from collections import deque

class Graph:
    # example of adjacency list (or rather map)
    # adjacency_list = {
    # 'A': [('B', 1), ('C', 3), ('D', 7)],
    # 'B': [('D', 5)],
    # 'C': [('D', 12)]
    # }

            
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # heuristic function with equal values for all nodes
    def h(self, n):
        H = {
    'S41A8': 1,
    'S42A8': 1,
    'S43A8': 1,
    'S44A8': 1,
    'S45A8': 1,
    'S46A8': 1,
    'S47A8': 1,
    'S48A8': 1,
    'S41A9': 1,
    'S42A9': 1,
    'S43A9': 1,
    'S44A9': 1,
    'S45A9': 1,
    'S46A9': 1,
    'S47A9': 1,
    'S48A9': 1,
    'S41A10': 1,
    'S42A10': 1,
    'S43A10': 1,
    'S44A10': 1,
    'S45A10': 1,
    'S46A10': 1,
    'S47A10': 1,
    'S48A10': 1,
    'S41A11': 1,
    'S42A11': 1,
    'S43A11': 1,
    'S44A11': 1,
    'S45A11': 1,
    'S46A11': 1,
    'S47A11': 1,
    'S48A11': 1,
    'S41A12': 1,
    'S42A12': 1,
    'S43A12': 1,
    'S44A12': 1,
    'S45A12': 1,
    'S46A12': 1,
    'S47A12': 1,
    'S48A12': 1

        }

        return H[n]

    def a_star_algorithm(self, start_node, stop_node):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        weightTotal = 0
        open_list = set([start_node])
        closed_list = set([])

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None
adjacency_list = {
    'A': [('B', 1), ('C', 3), ('D', 4)],
    'B': [('D', 5),('F', 12)],
    'C': [('D', 12)],
    'D': [('F', 2)],
    'E': [('A', 3)]
    
}
adjacency_listnot2to7PM = {
    'S41A8': [('S42A8', 1),('S41A9', 3.5)],
    'S42A8': [('S43A8', 1),('S42A9', 3.5)],
    'S43A8': [('S44A8', 2),('S43A9', 3.5)],
    'S44A8': [('S45A8', 2),('S44A9', 3.5)],
    'S45A8': [('S46A8', 2),('S45A9', 3.5)],
    'S46A8': [('S47A8', 2),('S46A9', 3.5)],
    'S47A8': [('S48A8', 1),('S47A9', 3.5)],
    'S48A8': [('S47A8', 1),('S48A9', 3.5)], #good
    'S41A9': [('S42A9', 1),('S41A10', 3.5)],
    'S42A9': [('S43A9', 1),('S42A10', 3.5)],
    'S43A9': [('S44A9', 2),('S43A10', 3.5)],
    'S44A9': [('S45A9', 2),('S44A10', 3.5)],
    'S45A9': [('S46A9', 2),('S45A10', 3.5)],
    'S46A9': [('S47A9', 2),('S46A10', 3.5)],
    'S47A9': [('S48A9', 1),('S47A10', 3.5)],
    'S48A9': [('S47A9', 1),('S48A10', 3.5)], #good
    'S41A10': [('S42A10', 1),('S41A11', 3.5)],
    'S42A10': [('S43A10', 1),('S42A11', 3.5)],
    'S43A10': [('S44A10', 2),('S43A11', 3.5)],
    'S44A10': [('S45A10', 2),('S44A11', 3.5)],
    'S45A10': [('S46A10', 2),('S45A11', 3.5)],
    'S46A10': [('S47A10', 2),('S46A11', 3.5)],
    'S47A10': [('S48A10', 1),('S47A11', 3.5)],
    'S48A10': [('S47A10', 1),('S48A11', 3.5)],
    'S41A11': [('S42A11', 1),('S41A12', 3.5)],
    'S42A11': [('S43A11', 1),('S42A12', 3.5)],
    'S43A11': [('S44A11', 2),('S43A12', 3.5)],
    'S44A11': [('S45A11', 2),('S44A12', 3.5)],
    'S45A11': [('S46A11', 2),('S45A12', 3.5)],
    'S46A11': [('S47A11', 2),('S46A12', 3.5)],
    'S47A11': [('S48A11', 1),('S47A12', 3.5)],
    'S48A11': [('S47A11', 1),('S48A12', 3.5)],
    'S41A12': [('S42A12', 1)],
    'S42A12': [('S43A12', 1)],
    'S43A12': [('S44A12', 2)],
    'S44A12': [('S45A12', 2)],
    'S45A12': [('S46A12', 2)],
    'S46A12': [('S47A12', 2)],
    'S47A12': [('S48A12', 1)],
    'S48A12': [('S47A12', 1)]
}
adjacency_list2to7PM = {
    'S41A8': [('S42A8', 6),('S41A9', 3.5)],
    'S42A8': [('S43A8', 6),('S42A9', 6)],
    'S43A8': [('S44A8', 6),('S43A9', 3.5)],
    'S44A8': [('S45A8', 6),('S44A9', 3.5)],
    'S45A8': [('S46A8', 6),('S45A9', 3.5)],
    'S46A8': [('S47A8', 6),('S46A9', 3.5)],
    'S47A8': [('S48A8', 6),('S47A9', 3.5)],
    'S48A8': [('S47A8', 6),('S48A9', 3.5)], #good
    'S41A9': [('S42A9', 6),('S41A10', 3.5)],
    'S42A9': [('S43A9', 6),('S42A10', 6)],
    'S43A9': [('S44A9', 6),('S43A10', 3.5)],
    'S44A9': [('S45A9', 6),('S44A10', 3.5)],
    'S45A9': [('S46A9', 6),('S45A10', 3.5)],
    'S46A9': [('S47A9', 6),('S46A10', 3.5)],
    'S47A9': [('S48A9', 6),('S47A10', 3.5)],
    'S48A9': [('S47A9', 6),('S48A10', 3.5)], #good
    'S41A10': [('S42A10', 6),('S41A11', 3.5)],
    'S42A10': [('S43A10', 6),('S42A11', 6)],
    'S43A10': [('S44A10', 6),('S43A11', 3.5)],
    'S44A10': [('S45A10', 6),('S44A11', 3.5)],
    'S45A10': [('S46A10', 6),('S45A11', 3.5)],
    'S46A10': [('S47A10', 6),('S46A11', 3.5)],
    'S47A10': [('S48A10', 6),('S47A11', 3.5)],
    'S48A10': [('S47A10', 6),('S48A11', 3.5)],
    'S41A11': [('S42A11', 6),('S41A12', 3.5)],
    'S42A11': [('S43A11', 6),('S42A12', 6)],
    'S43A11': [('S44A11', 6),('S43A12', 3.5)],
    'S44A11': [('S45A11', 6),('S44A12', 3.5)],
    'S45A11': [('S46A11', 6),('S45A12', 3.5)],
    'S46A11': [('S47A11', 6),('S46A12', 3.5)],
    'S47A11': [('S48A11', 6),('S47A12', 3.5)],
    'S48A11': [('S47A11', 6),('S48A12', 3.5)],
    'S41A12': [('S42A12', 8)],
    'S42A12': [('S43A12', 8)],
    'S43A12': [('S44A12', 8)],
    'S44A12': [('S45A12', 8)],
    'S45A12': [('S46A12', 8)],
    'S46A12': [('S47A12', 8)],
    'S47A12': [('S48A12', 8)],
    'S48A12': [('S47A12', 8)]
}


question = input("is the time between 2PM and 7PM answer Y or N: ")
if(question == "Y"):
    graph1 = Graph(adjacency_list2to7PM)
    graph1.a_star_algorithm('S42A8', 'S46A12')
else:
    graph1 = Graph(adjacency_listnot2to7PM)
    graph1.a_star_algorithm('S42A8', 'S46A12')
