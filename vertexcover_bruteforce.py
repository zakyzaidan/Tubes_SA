import timeit

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_matrix = [[0] * vertices for _ in range(vertices)]
        
    def add_edge(self, u, v):
        self.adjacency_matrix[u][v] = 1
        self.adjacency_matrix[v][u] = 1
    
    def vertex_cover_brute_force(self):
        min_vertex_cover = None
        min_cover_size = float('inf')
        
        for i in range(1 << self.vertices):
            current_cover = []
            
            for j in range(self.vertices):
                if i & (1 << j):
                    current_cover.append(j)
            
            #Jika simpul curr cover kurang dari min vertex cover sebelumnya, maka curr cover menjadi min vertex cover
            if self.is_vertex_cover(current_cover) and len(current_cover) < min_cover_size:
                min_vertex_cover = current_cover
                min_cover_size = len(current_cover)
        
        return min_vertex_cover
    
    # Akan dicek simpul yang dipilih, apakah vertex cover atau bukan
    def is_vertex_cover(self, cover):
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.adjacency_matrix[i][j] == 1 and i not in cover and j not in cover:
                    return False
        return True


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
vertex_cover = g.vertex_cover_brute_force()
stop = timeit.default_timer()
lama_eksekusi = stop - start
print("Vertex Cover: ", vertex_cover)
print("Lama eksekusi: ",lama_eksekusi,"detik")
