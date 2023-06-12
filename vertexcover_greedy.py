import timeit

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_matrix = [[0] * vertices for _ in range(vertices)]
        
    def add_edge(self, u, v):
        self.adjacency_matrix[u][v] = 1
        self.adjacency_matrix[v][u] = 1
    
    def vertex_cover_greedy(self):
        vertex_cover = []
        visited = [False] * self.vertices
        
        while True:
            max_degree = -1
            max_vertex = -1
            
            # Mencari simpul dengan derajat tertinggi yang belum dikunjungi
            for u in range(self.vertices):
                if not visited[u]:
                    degree = self.calculate_degree(u)
                    if degree > max_degree:
                        max_degree = degree
                        max_vertex = u
            
            # Jika tidak ada simpul yang tersisa, keluar dari perulangan
            if max_vertex == -1:
                break
            
            # Tambahkan simpul dengan derajat tertinggi ke dalam vertex cover
            vertex_cover.append(max_vertex)
            visited[max_vertex] = True
            
            # Tandai sisi yang terhubung dengan simpul tersebut sebagai tercakup
            for v in range(self.vertices):
                if self.adjacency_matrix[max_vertex][v] == 1:
                    visited[v] = True
        
        return vertex_cover
    
    def calculate_degree(self, u):
        degree = 0
        for v in range(self.vertices):
            if self.adjacency_matrix[u][v] == 1:
                degree += 1
        return degree


# Contoh penggunaan
g = Graph(8)
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 5)
g.add_edge(1, 2)
g.add_edge(2, 6)
g.add_edge(5, 6)
g.add_edge(2, 3)
g.add_edge(2, 7)

start = timeit.default_timer()
vertex_cover = g.vertex_cover_greedy()
stop = timeit.default_timer()
lama_eksekusi = stop - start
print("Vertex Cover: ", vertex_cover)
print("Lama eksekusi: ",lama_eksekusi,"detik")
