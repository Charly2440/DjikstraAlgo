import networkx as nx
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
        self.parseData()
        self.createNodes()
        self.createEdges()

        return self.graph