
from collections import deque

def earliest_ancestor(ancestors, starting_node):
    """
    take in the set of ancestors > 
    Have a set of key val pairs > {Node:Child}
    A counter for generations > to cycle how far back
    furthest back wins > if furthest the same, lowest wins
    """
    
    
    class Graph:
        def __init__(self):
            self.vertices = {}
        
        def __repr__(self):
            return str(self.vertices)

        def add_vertex(self, vertex_id):
            if vertex_id not in self.vertices:
                self.vertices[vertex_id] = set()
        def add_edge(self, v1, v2):
            if v1 in self.vertices and v2 in self.vertices:
                self.vertices[v1].add(v2)
        def get_neighbors(self, vertex_id):
            return self.vertices[vertex_id] if vertex_id in self.vertices else set()

        


    ancestor_graph = Graph()

    for element in ancestors:
        ancestor_graph.add_vertex(element[0])
        ancestor_graph.add_vertex(element[1])
        ancestor_graph.add_edge(element[0],element[1])
    
    

    
