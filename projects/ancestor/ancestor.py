"""
TODO!
To update this, change the add vertex to add a node class
build a node class, that has both a parent and a child property
change the find_end_nodes to include dictionaries instead of nested for loops
check each node to see if it has a parent property, or a child property
if it has no parent, it is a top node
if it has no child, it is a bottom node,
then continue with the program
"""


from collections import deque

def earliest_ancestor(ancestors, starting_node):
    """
    take in the set of ancestors > 
    Have a set of key val pairs > {Node:Child}
    A counter for generations > to cycle how far back
    furthest back wins > if furthest the same, lowest wins
    """
    
    """
    class ListNode:
        def __init__(self, value, child = None, parent = None):
            self.parent = parent
            self.child = child
            self.value = value
        def __repr__(self):
            return f'Value: {self.value} , Parent: {self.parent}, Child: {self.child}'

    """
    class Graph:
        def __init__(self):
            self.vertices = {}
            self.top_endpoints = set()
            self.bottom_endpoints = set()
        
        def __repr__(self):
            return str(self.vertices)

        def add_vertex(self, vertex_id):
            if vertex_id not in self.vertices:
                self.vertices[vertex_id] = set()
                
        def add_edge(self, v1, v2):
            if v1 in self.vertices and v2 in self.vertices:
                self.vertices[v1].add(v2)
                
        """
        def add_child(self,v1,v2):
            if v1 in self.vertices and v2 in self.vertices:
                #self.vertices[v1]child = v2
                pass

        """ 
        def get_vertex(self,vertex_id):
            if vertex_id in self.vertices:
                return self.vertices[vertex_id]       

        def get_neighbors(self, vertex_id):
            return self.vertices[vertex_id] if vertex_id in self.vertices else set()
        
        def dfs(self,starting_vertex,destination_vertex):

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
        
        def dft(self, starting_vertex):
            stack = deque()
            stack.append(starting_vertex)
            visited = set()
            while len(stack) > 0:
                currNode = stack.pop()
                if currNode not in visited:
                    visited.add(currNode)
                    for neighbor in self.vertices[currNode]:
                        stack.append(neighbor)
            return visited
    
        def bft(self, starting_vertex):
            visited = set()
            queue = deque()
            queue.appendleft(starting_vertex)
            while len(queue) > 0:
                currNode = queue.pop()
                if currNode not in visited:
                    visited.add(currNode)
                    for neighbor in self.get_neighbors(currNode):
                        queue.appendleft(neighbor)
            return visited
        """
        Maybe do a BFT for each element, get the end node of that BFT > compare against
        the ancestor graph, if that end element correlates with an empty set, then we know that it is a child and 
        we can disregard or add to a child storage thing, at which point we can start making a set
        so that we have the correct end "parent" for a given node, and just run the comparison there
        """
        


    """
    #with the self.child we need to get the neighbors of a thing
    #if that neighbor is not the current thing's child, we go that way.
    """
    ancestor_graph = Graph()
    finished = False
    for element in ancestors:
        ancestor_graph.add_vertex(element[0])
        ancestor_graph.add_vertex(element[1])
        ancestor_graph.add_edge(element[0],element[1])
        
        #neighbor0 = ancestor_graph.get_neighbors(element[0])
        #neighbor1 = ancestor_graph.get_neighbors(element[1])
        #if neighbor0 not in ancestor_graph.vertices:
        #if neighbor0 or neighbor1 in ancestor_graph:
            #ancestor_graph.add_edge(element[0],neighbor0)
    #print(ancestor_graph.get_vertex(1))
    
        
        #only_children = {}
        parent = 0
        #endpoint = set()
        #child = starting_node
        travel_length = 0
        #node_length = {}
        #possible_parents = set()
    #if child not in ancestor_graph.vertices:
        #return -1

    #for element in ancestor_graph.vertices:
        #print(ancestor_graph.dft(element) )

    #for element in ancestor_graph.vertices:
        #print(ancestor_graph.bft(element))

    while finished != True:
        """
        need to iterate through the new graph, looking for an element that contains
        the target number, once we find it, we iterate again until we don't return anything
        Should change this into a function
        
        """
        for elemento in ancestor_graph.vertices:
            child = elemento

            changed = False
            #child = starting_node
            #print(len(ancestor_graph.vertices))
            #print(ancestor_graph.vertices[1])
            for element in ancestor_graph.vertices:
                if element in ancestor_graph.bottom_endpoints:
                    pass
                else:
                    #print(ancestor_graph.vertices[element])
                
                    if len(ancestor_graph.vertices[element]) == 0:
                        ancestor_graph.bottom_endpoints.add(element)
                
                    if child in ancestor_graph.vertices[element]:
                        #need to get neighbors of this element, and check for possible outcomes,
                        #if len(ancestor_graph.vertices[element]) > 1:
                            #for sub_element in ancestor_graph.vertices[element]:
                                #print(sub_element)
                        parent = element
                        child = parent
                        travel_length += 1
                        changed = True
                    #adds variables for future checks
            if changed == False:
                ancestor_graph.top_endpoints.add(parent)
                ancestor_graph.top_endpoints.add(child)#adds variables for future checks
                #if travel_length == 0:
                    #return -1
                #return parent        
        finished = True    
    #^^^^^^^^^^^Turn the above into a function^^^^^^^^^^^^
    #vvvvvvvvvvvMay not have to reverse sortvvvvvvvvvvv
    sorted_top_endpoints = sorted(ancestor_graph.top_endpoints, reverse = True)
    greatest_element = 0
    greatest_length = 0
    #element = starting_node
    for element in sorted_top_endpoints:
        
        
        if ancestor_graph.dfs(element,starting_node) != None:
            #find the greatest length, compare, if current length bigger, update, else leave the same
            current_length = len(ancestor_graph.dfs(element,starting_node))
            if current_length > 1:
                if current_length >= greatest_length:
                    greatest_length = current_length
                    greatest_element = element
                    if greatest_element > element:
                        greatest_element = element
        #if element in ancestor_graph.top_endpoints:
            #return -1    
                
    if greatest_element != 0:
        return greatest_element
    return -1     




    
    
    
    

    
            
    
