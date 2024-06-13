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
    q = [] #temporary storage queue
    q.append(r)
    c[r] = GREY
    output += str(r) + " "
    #### TODO ####
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
    c = [WHITE] * g.nb_vertices()
    output = "Recursive DFS\n"
    output += str(r) + " "
    output += recursive_dfs(g, r, c)
    return output


def recursive_dfs(g: Graph, i: int, c: list):
    output = ""
    c[i] = GREY #currently visiting i
    #### TODO ####
    c[i] = BLACK #done visiting i
    return output


"""
Compute a Minimal Spanning Tree (MST) of a graph.
@param g  the graph whose MST is produced
@param root  the root of the produced MST
@return a graph representation of an MST of g that starts at vertex root
 """
def computeMinimumSpanningTree(g: Graph, root: int):
    #create an empty copy of g
    graph_type = type(g)
    gRes = graph_type(g.nb_vertices())
    #find a minimum spanning tree of g
    c = [WHITE] * g.nb_vertices()
    stack = [] #temporary storage stack
    #### TODO ####
    return gRes


"""
Compute the connectivity table (transitive closure) of a graph.
The table is obtained with Warshall's algorithm.
@param g  the graph whose connectivity table is produced
@return a graph representation of the connectivity table of g
 """
def computeConnectivity(g: Graph):
    #create a deep copy of g
    import copy
    gRes = copy.deepcopy(g)
    #use Warshall's algorithm to generate the connectivity table of gRes
    #### TODO ####
    return gRes
