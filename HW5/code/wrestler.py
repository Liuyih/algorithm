import sys
import math
#vertex class is used to build the vertex struture of the input data, treat each
#wrestler as a single vertex.
class Vertex:
    def __init__(self, wrestler):
        # assign wrestler's name as each vertex's name
        self.name = wrestler
        # initialize a empty list of neighbors 
        self.neighbors = list()
        # initialize the distance to be infinity 
        self.distance = math.inf
        # unvisited color is black
        self.color = 'black'
        # initialize the type to not applicable 
        self.type = 'NA'

    # add other adjacent Vertex to neighbor list 
    def add_neighbor(self, vertex):
        # make sure the vertex is not in the neighbor list already
        if vertex not in self.neighbors:
            self.neighbors.append(vertex)
            self.neighbors.sort()

# Graph class is used to build graph using wrestlers and pairs of rivalries
# if the graph of input file can be created, then there is possible to assign
class Graph:
    #initialize a empty list to contain all the wrestlers
    vertices = {}

    # add vertex (wrestler) to graph
    def add_vertex(self, vertex):
        # check if vertex already in vertices dictionary
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex

    # add edges (rivalries) to graph, u v are the wrestlers in the same pair
    def add_edge(self, u, v):
        # u and v are vertex, check if they are in vertices dictionary
        if u in self.vertices and v in self.vertices:
            # add neighbours for u and v
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)

    # Breadth first search to check if it is possible to designate
    def bfs(self, vertex):
        # initialize the empty queue
        q = list()
        vertex.distance = 0
        # color red represent visited node
        vertex.color = 'red'
        # initialize the start vertex type is Babyfaces, you can also initialize it as heels 
        # doesn't matter
        vertex.type = 'Babyface'

        for v in vertex.neighbors:
            self.vertices[v].distance = vertex.distance + 1
            # the neighbor of 'Babyface' is 'Heel' with 1 distance
            self.vertices[v].type = 'Heel'
            q.append(v)

        # loop through neighbors to BFS
        while len(q) > 0:
            # Dequeue a vertex from queue
            u = q.pop(0)
            node_u = self.vertices[u]
            # mark visited node is red
            node_u.color = 'red'

            for v in node_u.neighbors:
                node_v = self.vertices[v]
                # if the node is unvisited, enqueue the v to the queue
                if node_v.color == 'black':
                    q.append(v)
                    # if the distance is bigger than previous node, increase distance by 1
                    if node_v.distance > node_u.distance + 1:
                        node_v.distance = node_u.distance + 1
                    # sine the start node is Babyfaces 0, if the distance is even, the type of
                    # that vertex should be Babyfaces
                    if node_v.distance % 2 == 0:
                        node_v.type = 'Babyface'
                    else:
                        node_v.type = 'Heel'
                    # when u and v have the same type, just quit the program.
                    if node_v.type == node_u.type:
                        print("Impossible")
                        quit()

        # loop through unvisited vertices to build the graph
        for v in self.vertices:
            if self.vertices[v].color == 'black':
                self.bfs(self.vertices[v])

    # this function is used to print the result
    def printResult(self):
        print("Yes Possible")
        result1 = 'Babyfaces: '
        result2 = 'Heels: '
        #create list to hold for possible babyfaces and heels
        BF_list = []
        HE_list = []
        # print the result based on two different types
        for v in self.vertices:
            if self.vertices[v].type == "Babyface":
                BF_list.append(self.vertices[v].name)
        # sort their name, not very necessary
        BF_list.sort()
        for item in BF_list:
            result1 = result1 + item + ' '

        for v in self.vertices:
            if self.vertices[v].type == "Heel":
                HE_list.append(self.vertices[v].name)
        HE_list.sort()
        for item in HE_list:
            result2 = result2 + item + ' '

        print(result1)
        print(result2)


# Input is read in from a file specified in the command line at run time
def main():
    with open(sys.argv[1], "r") as inputFile:
        # split the input line by line
        lines = inputFile.read().splitlines()
       
        #close the inputFile
        inputFile.close()
        
        # first line of data is number of wrestlers
        num_w = int(lines[0])
        
       
        # the number of pairs is located in the position of lines[num_w+1]
        # such as num_w is 6, then the position of num_r is at lines[7].
        num_r = int(lines[num_w + 1])
        
       
        g = Graph()
        pairs = []
        # add wrestlers to vertices of graph start from the line[1] becasue the second 
        #input from the input file is the first wrestler's name till line[num_w+1] the last
        #wrestler's name
        for i in range(1, num_w + 1):
            g.add_vertex(Vertex(lines[i]))

        # add neighbours of vertices, same as wrestler, num_w + 2 is the position of the 
        #first pair line[num_w + 2 + num+r] is the position of the last pair
        # you can also use len(liens) if there is no comments after pairs, which the position of the last element
        # is just the lines [len(lines)]
        for j in range(num_w + 2, num_w + 2 + num_r):
            # get pairs and insert into empty list
            pairs.append(lines[j])
        for pair in pairs:
        #create a tuple to hold the pairs
            pair_tuple = pair.split()
            #pass the wrestlers  in each pair as u and v
            g.add_edge(pair_tuple[0], pair_tuple[1])
           
        # call the bfs to build the graph, pass the first wrestler as start vertex
        g.bfs(g.vertices[lines[1]])
        # if it successfully build the graph, we can print the result
        g.printResult()
        
main()