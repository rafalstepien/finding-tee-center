import networkx as nx
import matplotlib.pyplot as plt

class Tree:
        
	def __init__(self, vertices_list):
		self.vertices_list = vertices_list

	def cut_degree(self):
		"""
		Odcina wszystkie wierzcholki ktore aktualnie maja stopien pierwszy
		"""
		to_remove = [vertex.id for vertex in self.vertices_list if vertex.degree == 1]
		self.vertices_list = [vertex for vertex in self.vertices_list if vertex.id not in to_remove]
		for vertex in self.vertices_list:
			vertex.neighbours = [neighbour for neighbour in vertex.neighbours if neighbour not in to_remove]
			vertex.degree = len(vertex.neighbours)

	def find_center(self):
		"""
		Odcina rekurencyjnie wszystkie wierzchołki, ktore maja stan jeden, dopoki nie zostana ich tylko dwa lub jeden
		"""
		while len(self.vertices_list) > 2:
			self.cut_degree()
		return self.vertices_list

	def add_vertex(self, id, neighbours):
		"""
		Dodaje wierzcholek
		"""
		self.vertices_list.append(Vertex(id, neighbours))

	def list_vertices(self):
		"""
		Wyswietla liste wszystkich wierzcholkow i polaczonych z nimi sasiednich wierzcholkow
		"""
		for vertex in self.vertices_list:
			print("ID: {}, SASIEDZI: {}".format(vertex.id, sorted(vertex.neighbours)))

	def print_graph(self):
		"""
		Wizualizuje graf
		"""
		G = nx.Graph()
		for vertex in self.vertices_list:
			G.add_node(vertex.id)
			for neighbour in vertex.neighbours:
				G.add_edge(vertex.id, neighbour)
		plt.subplot(121)
		nx.draw(G, with_labels=True, font_weight='bold')
		plt.show()


class Vertex:
	def __init__(self, id, neighbours):
		self.id = id
		self.neighbours = neighbours
		self.degree = len(neighbours)

	def __repr__(self):
		return "Vertex({})".format(self.id)

# # -------------------------------------------------
# g1 = Vertex('a', ['b'])
# g2 = Vertex('b', ['a', 'c'])
# g3 = Vertex('c', ['b', 'f', 'd', 'g'])
# g4 = Vertex('d', ['c', 'e'])
# g5 = Vertex('e', ['d'])
# g6 = Vertex('f', ['c'])
# g7 = Vertex('g', ['c'])
# tree1 = Tree([g1, g2, g3, g4, g5, g6, g7])
# -------------------------------------------------

# -------------------------------------------------
# a1 = Vertex('8', ['2'])
# a2 = Vertex('7', ['2'])
# a3 = Vertex('6', ['2'])
# a4 = Vertex('2', ['6', '7', '8'])
# a5 = Vertex('1', ['3', '4', '5'])
# a6 = Vertex('3', ['1'])
# a7 = Vertex('4', ['1'])
# a8 = Vertex('5', ['1'])
# tree2 = Tree([a1, a2, a3, a4, a5, a6, a7, a8])
# -------------------------------------------------

# -------------------------------------------------
b1 = Vertex('1', ['2'])
b2 = Vertex('2', ['1', '4', '3'])
b3 = Vertex('3', ['2', '6'])
b4 = Vertex('4', ['2', '5'])
b5 = Vertex('5', ['9', '4'])
b6 = Vertex('6', ['8', '7', '3'])
b7 = Vertex('7', ['6'])
b8 = Vertex('8', ['6'])
b9 = Vertex('9', ['5'])
tree3 = Tree([b1, b2, b3, b4, b5, b6, b7, b8, b9])
# -------------------------------------------------

tree3.add_vertex('10', ['7'])
tree3.add_vertex('11', ['7'])
tree3.print_graph()
print(tree3.find_center())
