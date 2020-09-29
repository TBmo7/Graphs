from room import Room
from player import Player
from world import World
from collections import deque

import random
from ast import literal_eval


    
class Traversal_graph():

    def __init__(self):
        self.vertices = {}
    
    def __repr__(self):
        return str(self.vertices)

    def add_vertex(self, vertex_id, room_graph):
        #When we first initialize a room, checking for all unknown directions
        #might have to roll in visited rooms, so that we don't overwrite rooms
        #that we have already been to.
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = dict()
        if 'n' in room_graph[vertex_id][1]:
            self.vertices[vertex_id]['n'] = '?'
        if 's' in room_graph[vertex_id][1]:
            self.vertices[vertex_id]['s'] = '?'
        if 'e' in room_graph[vertex_id][1]:
            self.vertices[vertex_id]['e'] = '?'
        if 'w' in room_graph[vertex_id][1]:
            self.vertices[vertex_id]['w'] = '?'
    
    def add_edge(self, v1, v2, stage_exit):
        inverse_stage_exit = ''
        if stage_exit == 'n':
            inverse_stage_exit = 's'
        if stage_exit == 's':
            inverse_stage_exit = 'n'
        if stage_exit == 'e':
            inverse_stage_exit = 'w'
        if stage_exit == 'w':
            inverse_stage_exit = 'e'
        if v1 in self.vertices and v2 in self.vertices:
           self.vertices[v1][stage_exit] = v2
           self.vertices[v2][inverse_stage_exit] = v1
               
    def get_key(self,val,current_room):
        #returns a key for a value in a dict
        for key, value in current_room.items():
            if val == value:
                return key
    
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id] if vertex_id in self.vertices else dict()

    def bft(self, starting_vertex):
        #this is a hybrid traversal/search function
        stack = deque()
        stack.append(starting_vertex)
        visited = set()
        out_arr = []
        #out_path = []
        while len(stack) > 0:
            currNode = stack.pop()
            curr_exits = self.vertices[currNode]
            
            if len(tgraph.get_unvisited_exits(curr_exits)) > 0:
                #this checks if there are unvisited rooms, if there are, we have found our room
                # and it returns a path for us to get to it
                #we convert the numbers into directions
                out_arr.append(currNode)
                return out_arr
            elif currNode not in visited:
            #here we need to check the current node if any of the exits have "?"
            #if they do, we now have a traversal path to the room we need
            
                visited.add(currNode)
                out_arr.append(currNode)
                for neighbor in self.vertices[currNode]:
                    #here neighbor is a bunch of cardinal directions,
                    #we need to translate into room numbers and append the numbers
                    room_number = self.vertices[currNode][neighbor]
                    #out_path.append(neighbor)
                    stack.append(room_number)
        return out_arr
        #this should traverse the known map and then return the paths taken


    def bfs(self, starting_vertex,destination_vertex):
        #going to change this to a BFS for the closest room with an unvisited exit
        visited = set()
        stack = deque()
        stack.append([starting_vertex])
        #need to look through nodes for the closest one with an unvisited exit
        #for some reason this function sometimes receives a '?' as a key, can't explain it, adding workaround
        while len(stack) > 0:
            currPath = stack.popleft()
            currNode = currPath[-1]
            print(currNode)
            if currNode == '?':
                print('triggered')
                #This is to bypass the '?' key error
                currPath = stack.popleft()
                currNode = currPath[-1]
            if currNode == destination_vertex:
                return currPath
            if currNode not in visited:
                visited.add(currNode)
                for neighbor in self.vertices[currNode]:
                    room_number = self.vertices[currNode][neighbor]
                    newPath = list(currPath)
                    newPath.append(room_number)
                    stack.append(newPath)
    #BFS is good for finding A way to a room, but it is not working the way it needs to
    #SO this is wrong, because it's a BFT, and not a BFS, but it does give us what we need to know for  

    def get_random_direction(self,exits):
    #returns a random direction
    #use this when there are multiple ? exits
    #exits = self.exits
        return random.choice(exits)
    
    def backtrack(self, path):
        out_map = []
        count = 0
        while count < len(path)-1:
            current = path[count]
            next_room = path[count+1]
            curr_room = self.vertices[current]
            out_map.append(tgraph.get_key(next_room, curr_room))
            count += 1
        return out_map
        


    def get_unvisited_exits(self,exits):
        # checks a room for all unvisited exits
        #exits = self.exits
        #WORKS!
        #count = 0
        out_list = []
        if 'n' in exits:
            if exits['n'] == '?':
                out_list.append('n')
        if 'e' in exits:
            if exits['e'] == '?': 
                out_list.append('e')
        if 'w' in exits:
            if exits['w'] == '?':
                out_list.append('w')
        if 's' in exits:
            if exits['s'] == '?':
                out_list.append('s')
                
        return out_list
    
    
            

# Load world
world = World()
"""
First thing we need to do is get the exits of the room that we're currently in
if there are unexplored exits in the room . add room to unexplored options
if we explore all locations, there are no ? in the room, we remove from unexplored rooms
when we first explore a room > we log the room ID and the exits. 
when we move, we add out direction to the traversal path

We keep moving through rooms so long as we don't find ourselves in a room with 
all exits mapped, at that point look for a room that has "?" for an exit
"""

# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "projects/adventure/maps/test_line.txt"
#map_file = "projects/adventure/maps/test_cross.txt"
#map_file = "projects/adventure/maps/test_loop.txt"
#map_file = "projects/adventure/maps/test_loop_fork.txt"
map_file = "projects/adventure/maps/main_maze.txt" #>MAIN FOR A REASON

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
tgraph = Traversal_graph()
visited_rooms = {}
for element in room_graph:
    tgraph.add_vertex(element, room_graph)
bypass_error = False
bypass_helper = False

while bypass_error == False:
    try:



        while len(visited_rooms) < len(room_graph): #3 is for line
            #we need to set a variable for the path that we're taking out of here
            stage_exit = ''
            #get out current room id
            current_room = player.current_room.id
            #get all the exits for this room
            current_exits = player.current_room.get_exits()
            #add this room to the graph and visited_rooms
            visited_rooms[current_room] = [current_room]
            if len(visited_rooms) != len(room_graph):

                #tgraph.add_vertex(current_room, current_exits, visited_rooms)
                
                #get all the unvisited exits
                unvisted_exits = tgraph.get_unvisited_exits(tgraph.vertices[current_room])
                #check if we have visited all the exits in this room
                
                #if we haven't our way out is a random exit
                if len(unvisted_exits) > 0:
                    stage_exit = tgraph.get_random_direction(unvisted_exits)
                    #print(stage_exit)
                else:
                    #Here we have to find the closest room with an exit that we haven't used
                    known_paths = tgraph.bft(current_room)
                    #the BFT for the back_map is not always the shortest path
                    #adding a function to get the shortest path
                    target_room = known_paths[-1]
                    streamlined_paths = tgraph.bfs(current_room, target_room)
                    #streamlined_map = tgraph.backtrack(streamlined_paths)

                    back_map = tgraph.backtrack( streamlined_paths)
                    #print(target_room)
                    #we have a path to the nearest room with an unvisited exit
                    #now we head back on that path, and record our journey
                    for element in back_map:
                        traversal_path.append(element)
                        player.travel(element)
                    #now we're back to a room that we know has an unvisited exit
                    #time to get the room's information, and the unvisited exit
                    current_room = player.current_room.id
                    unvisted_exits = tgraph.get_unvisited_exits(tgraph.vertices[current_room])
                    stage_exit = tgraph.get_random_direction(unvisted_exits)

                    #get the known graph
                #add our chosen direction to the path
                #we need to add an edge here, get the neighbors,
                next_room_id = room_graph[current_room][1][stage_exit]
                tgraph.add_edge(current_room, next_room_id,stage_exit)    
                traversal_path.append(stage_exit)
                #move 
                player.travel(stage_exit)
    except:
        print('keep going')
        bypass_helper = False
    if bypass_helper == False:
        bypass_error = False
    else:
        bypass_error = True
    #bypass_error = True
        
    
    

    



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
"""
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
"""