from collections import deque

class Graph:
    def __init__(self):
        self.vertices = {}
    def __repr__(self):
        return str(self.vertices)
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
    def add_edge(self, v1,v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id] if vertex_id in self.vertices else set()

    def dft(self, starting_vertex):
        stack = deque()
        stack.append(starting_vertex)
        visited = set()
        while len(stack) > 0:
            currNode = stack.pop
            if currNode  not in visited:
                visited.add(currNode)
                print(currNode)
                for neighbor in self.vertices[currNode]:
                    stack.append(neighbor)

    def dfs(self,starting_vertex, destination_vertex):
        stack = deque()

        stack.append([starting_vertex])
        visited = set()
        while len(stack) > 0:
            currPath = stack.pop()
            currNode = currPath[-1]
            if currNode == destination_vertex:
                return currPath
            if currNode not in visited:
                visited.add(currNode)
                for neighbor in self.get_neighbors(currNode):
                    newPath = list(currPath)
                    newPath.append(neighbor)
                    stack.append(newPath)

    def bft(self, starting_vertex):
        visited = set()
        queue = deque()
        queue.append(starting_vertex)
        while len(queue) > 0:
            currNode = queue.popleft()
            if currNode not visited:
                visited.add(currNode)
                print(currNode)
                for neighbor in self.get_neighbors(neighbor):
                    queue.append(neighbor)

g = Graph()

g.add_vertex(1)        
g.add_vertex(2)
g.add_vertex(3)

print(g)


"""

ISLAND LECTURE PROBLEM

create an island class, with a topedge,botedge, rightedge, left edge
create a list of island classes
iterate through the grid, [0][0] if that is a one then all props are that coord
iterate check the grid up,down,left,right, if any are ones, update
continue until you have defined the shape of the island,

"""

"""
Generate Users and Friendships
"""

visited = {}
queue = deque()
queue.append([user_id])
while len(queue) >0 :
    currPath = queue.popleft()
    currNode = currPath[-1]
    visited[currNode] = currPath
    for friend in self.Friendships[currNode]:
        if friend not in visited:
            newPath = currPath.copy()
            newPath.append(friend)
            