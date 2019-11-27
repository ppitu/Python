
class Graph:
	def __init__(self, graph_dict = None):
		if graph_dict == None:
			graph_dict = {}
		self.graph_dict = graph_dict
		self.nodes = 0;
		self.edges = 0;

	def list_node(self):
		return list(self.graph_dict.keys())	

	def list_edges(self):
		return self.generate_edges()
			
	def count_node(self):
		return self.nodes
	
	def count_edges(self):
		return self.edges

	def add_node(self, node):
		if node not in self.graph_dict:
			self.graph_dict[node] = []
		self.nodes = self.nodes + 1

	def add_edge(self, edge):
		edge = set(edge)
		(node1, node2) = tuple(edge)

		if node1 in self.graph_dict:
			self.graph_dict[node1].append(node2)
		else:
			self.graph_dict[node1] = [node2]

		self.edges = self.edges + 1

	def generate_edges(self):
		edges = []

		for node in self.graph_dict:
			for x in self.graph_dict[node]:
				if{x, node} not in edges:
					edges.append({node, x})

		return edges


'''Test funckji '''

graph = Graph()

graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
print(graph.list_node())
graph.add_edge({"A", "B"})
graph.add_edge({"C", "A"})
print(graph.list_edges())
print(graph.count_node())
print(graph.count_edges())
