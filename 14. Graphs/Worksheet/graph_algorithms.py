from graphADT import Graph

"""
Use the constants below to mark vertices as DFS/BFS explorations progress.
WHITE vertex => unvisited
GREY vertex => visiting: exploring outgoing edges
BLACK vertex => visited: outgoing edges explored
"""
WHITE = 0
GREY = 1
BLACK = 2

"""
Perform a breadth-first search (BFS) of a graph.
The exploration leads to displaying the order in which every vertex 
gets visited. Use a queue to store vertices that are yet to be visited. 
Upon visiting a vertex, its label is displayed.
@param g  the graph to explore via BFS
@param r  the starting point (root) of the BFS exploration
@return the string representation of the output of the search
"""


def bfs(g: Graph, r: int):
    output = "BFS\n"
    c = [WHITE] * g.nb_vertices()
    queue = []  # temporary storage queue
    queue.append(r)
    c[r] = GREY
    output += str(r) + " "

    #### TODO ####
    while queue != []:
        node = queue.pop(0)
        for nbr in g.out_edges(node):
            # Check its neighborhood
            if c[nbr] == WHITE:
                # If the neighbor has not been visited, append to q, set to Grey
                queue.append(nbr)
                output += str(nbr) + " "
                c[nbr] = GREY

        # When all the neighbors of node is checked, mark node to Black
        c[node] = BLACK

    return output


"""
Perform a depth-first search (DFS) of a graph.
The exploration leads to displaying the order in which every vertex 
gets visited: upon visiting a vertex, its label is displayed.
This particular implementation of DFS must be recursive.
@param g  the explored graph
@param r  the node (root) where DFS starts
@return the string representation of the output of the search
"""


def recursiveDFS(g: Graph, r):
    output = "Recursive DFS\n"

    # Initialize a state machine
    state = [WHITE] * g.nb_vertices()

    output += str(r) + " "
    output += recursive_dfs(g, r, state)
    return output


def recursive_dfs(g: Graph, i: int, state: list):
    output = ""
    state[i] = GREY  # currently visiting i

    #### TODO ####
    for node in g.out_edges(i):
        if state[node] == WHITE:
            output += str(node) + " "
            output += recursive_dfs(g, node, state)

    state[i] = BLACK  # done visiting i
    return output


"""
Perform a depth-first search (DFS) of graph.
The exploration leads to displaying the order in which every vertex 
gets visited: upon visiting a vertex, its label is displayed.
This particular implementation of DFS must be non-recursive.
Use a stack to store vertices that are yet to be visited. 
@param g  the graph to explore
@param r  the starting point (root) of the DFS exploration
@return the string representation of the output of the search
Note: this may produce a different output than recursiveDFS(g,r)
 """


def iterativeDFS(g: Graph, r: int):
    output = "Iterative DFS\n"

    # Initialize a state machine and a stack
    state = [WHITE] * g.nb_vertices()
    stack = []
    stack.append(r)

    while stack != []:
        node = stack.pop()
        if state[node] == WHITE:
            output += str(node) + " "
            state[node] = GREY
            for j in g.out_edges(node):
                stack.append(j)
            state[node] = BLACK

    return output


"""
Compute a Minimal Spanning Tree (MST) of a graph.
@param g  the graph whose MST is produced
@param root  the root of the produced MST
@return a graph representation of an MST of g that starts at vertex root
 """


def computeMinimumSpanningTree(g: Graph, root: int):
    # create an empty copy of g
    graph_type = type(g)
    gRes = graph_type(g.nb_vertices())

    # Initialize a state machine and a stack
    state = [WHITE] * g.nb_vertices()
    stack = []

    #### TODO ####
    # Instead of DFS or BFS, here we use a level-order DFS where for each exploration, we explore the whole next level
    # The advantage of it is that we will form a relatively balanced BST compared to purely BST
    # Example: for a strongly-connected graph of 0,1,2,3,4 that connects every vertex v to vertices v+1 and v+2
    # BST:
    #     0
    #    / \
    #   1   2
    #      / \
    #     3   4
    stack.append(root)
    while stack != []:
        node = stack.pop()
        if state[node] != BLACK:
            state[node] = GREY
            for nbr in g.out_edges(node):
                if state[nbr] == WHITE:
                    state[nbr] = GREY
                    gRes.add_edge(node, nbr)
                    stack.append(nbr)
            state[node] = BLACK

    return gRes


"""
Compute the connectivity table (transitive closure) of a graph.
The table is obtained with Warshall's algorithm.
@param g  the graph whose connectivity table is produced
@return a graph representation of the connectivity table of g
 """


def computeConnectivity(g: Graph):
    # create a deep copy of g
    import copy

    gRes = copy.deepcopy(g)

    # use Warshall's algorithm to generate the connectivity table of gRes
    nb_vert = g.nb_vertices()
    #### TODO ####
    for k in range(nb_vert):
        for i in range(nb_vert):
            for j in range(nb_vert):
                if i != j and gRes.has_edge(i, k) and gRes.has_edge(k, j):
                    gRes.add_edge(i, j)

    return gRes
