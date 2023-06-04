import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import collections

header_list = ["a", "b", "w"]
E = pd.read_csv('data/rt_uae.edges', sep=" ",
                header=None, names=header_list)

G = nx.from_pandas_edgelist(E, "a", "b", ["w"])
nx.draw(G)
plt.show()

numNodes = nx.number_of_nodes(G)
numEdges = nx.number_of_edges(G)

averageDegree = sum([d for (n, d) in nx.degree(G)]) / \
    float(G.number_of_nodes())

density = (2*float(G.number_of_edges())) / \
    (float(G.number_of_nodes())*float(G.number_of_nodes()-1))


def getClusteringCoeff(G):
    clusters = []
    for node in G.nodes():
        neighbors = [neighbor for neighbor in G.neighbors(node)]
        ki = len(neighbors)
        subgraph = nx.subgraph(G, neighbors)
        ei = subgraph.number_of_edges()

        if ki != 0 and ki != 1:
            ci = (2 * ei) / (ki * (ki - 1))
        else:
            ci = 0
        clusters.append(ci)

    clusteringCoeff = sum(clusters) / len(clusters)
    return clusteringCoeff


clustCoeff = getClusteringCoeff(G)

# Degree Distribution Histogram
degree_sequence = sorted([d for n, d in G.degree()],
                         reverse=True)
degreeCount = collections.Counter(degree_sequence)
deg, count = zip(*degreeCount.items())

fig, ax = plt.subplots()
plt.bar(deg, count)

plt.title("Histogram of the graph")
plt.ylabel("Count")
plt.xlabel("Degree")
ax.set_xticks([d + 0.4 for d in deg])
ax.set_xticklabels(deg)

plt.show()


print("The number of nodes in the graph is ", numNodes)
print("The number of edges in the graph is ", numEdges)
print("The average degree of the graph is ", averageDegree)
print("The density of the graph is ", density)

if nx.is_connected(G) == True:
    diameter = nx.diameter(G)
    print("The diameter of the graph is ", diameter)

print("The clustering coefficient of the graph is ", clustCoeff)
