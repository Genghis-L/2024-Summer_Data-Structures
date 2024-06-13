from graphADT import Graph

"""
Produce a textual representation of the adjacency matrix of the graph.
@return the string representation of G(V, E)
"""
def adjacency_matrix_str(g):
    s = "(" + g.__class__.__name__ + ") "
    s += str(g.nb_vertices()) + " vertices, "
    s += str(g.nb_edges()) + " edges\n   "
    for i in range(g._nb_vertices):
        s += str(i) + " "
    s += "\n"
    for i in range(g._nb_vertices):
        s += str(i) + ":"
        for j in range(g._nb_vertices):
            if (j in g.out_edges(i)):
                s += " 1"
            else:
                s += " 0"
        s += "\n"
    return s

"""
Produces a plot representation of the graph.
Uses networkx and matplotlib
@return the string representation of G(V, E)
"""
def visualize(g):
    import networkx as nx
    import matplotlib.pyplot as plt
    s = "(" + g.__class__.__name__ + ") "
    s += str(g.nb_vertices()) + " vertices, "
    s += str(g.nb_edges()) + " edges\n   "
    print(s)
    dgv = nx.DiGraph()
    for i in range(g._nb_vertices):
        for j in g.out_edges(i):
            dgv.add_edge(i, j)
    nx.draw_circular(dgv, with_labels=True, font_weight='bold')
    plt.show()
    

