import networkx as nx
from matplotlib import pyplot as plt
import heapq
class GraphCreator:
    def __init__(self, rootData):
        self.rootData = rootData
        self.graph = nx.Graph()

    def parseData(self):
        relations = {}
        with open(self.rootData, 'r', encoding="utf-8") as file:
            data = file.read()
            data = data.split('\n')
            for relation in data:
                relations[relation.split(",")[0]+','+relation.split(",")[1]] = int(relation.split(",")[2][1:])

        return relations

    def createNodes(self):
        relations = self.parseData()
        nodes = []
        for relation in list(relations.keys()):
            relation = relation.split(",")
            nodes.append(relation[0])
            nodes.append(relation[1][1:])
        nodes = set(nodes)
        for node in nodes:
            self.graph.add_node(node)
        return self.graph.nodes()

    def createEdges(self):
        relations = self.parseData()
        edges = list(relations.keys())
        for edge in edges:
            self.graph.add_edge(edge.split(",")[0], edge.split(",")[1][1:], weight=relations[edge])
        return self.graph.edges()

    def createGraph(self):
        self.createNodes()
        self.createEdges()

        return self.graph

    #Algoritmo de grafico utilizando matplotlib obtenido de la documentacion ofical:
    #https://networkx.org/documentation/stable/auto_examples/drawing/plot_weighted_graph.html
    def graphicGraph(self):
        # Draw the graph
        elarge = [(u, v) for (u, v, d) in self.graph.edges(data=True)]
        esmall = [(u, v) for (u, v, d) in self.graph.edges(data=True)]

        pos = nx.spring_layout(self.graph, seed=7)  # positions for all nodes - seed for reproducibility

        # nodes
        nx.draw_networkx_nodes(self.graph, pos, node_size=700)

        # edges
        nx.draw_networkx_edges(self.graph, pos, edgelist=elarge, width=2)
        nx.draw_networkx_edges(self.graph, pos, edgelist=esmall, width=2, alpha=0.5, edge_color="b", style="dashed")

        # node labels
        nx.draw_networkx_labels(self.graph, pos, font_size=15, font_family="sans-serif")
        # edge weight labels
        edge_labels = nx.get_edge_attributes(self.graph, "weight")
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels)

        ax = plt.gca()
        ax.margins(0.01)
        plt.axis("off")
        plt.tight_layout()
        plt.show()
