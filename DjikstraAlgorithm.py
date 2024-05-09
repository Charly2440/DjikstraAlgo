
class DjikstraAlgorithm:
    #Constructor de algoritmo a partir del grafo dado
    def __init__(self, graph):
        self.graph = graph
        self.visited = {}
        for node in self.graph.nodes():
            self.visited[node] = False
        self.distances = {}
        for node in self.graph.nodes():
            self.distances[node] = float('inf')
        self.previous = {}
        for node in self.graph.nodes():
            self.previous[node] = None

    #Metodo para la implementacion del algoritmo
    def distanceDjikstra(self, start, end):
        self.distances[start] = 0

        while True:
            min_distance = float('inf')
            min_node = None

            for node in self.graph.nodes():
                if not self.visited[node] and self.distances[node] < min_distance:
                    min_distance = self.distances[node]
                    min_node = node

            if min_node is None:
                break

            self.visited[min_node] = True

            for neighbor, weight in self.graph[min_node].items():
                distance = self.distances[min_node] + weight['weight']
                if distance < self.distances[neighbor]:
                    self.distances[neighbor] = distance
                    self.previous[neighbor] = min_node

        path = []
        current = end
        while current is not None:
            path.insert(0, current)
            current = self.previous[current]

        return self.distances[end], path
