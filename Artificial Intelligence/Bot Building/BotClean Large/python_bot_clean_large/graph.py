from __future__ import print_function, division
class Graph:
    def __init__( self, mat ):
        self.mat        = mat
        self.vertices   = self.mat_to_list( self.mat )

        # Used for calculating the min path to hit all nodes.
        self.path       = list()
        self.temp_path  = list()
        self.total      = 0
        self.prev_total = 0

    def get_shorted_path( self ):
        path       = [ self.vertices[0] ]
        temp_path  = [ self.vertices[0] ]
        total      = 0
        temp_total = 0

        source = self.vertices[0].visited = True
        for i in range(len(source.edge_list)):
            while
            temp_path.append( self.vertices[i] )


        self.printGraph()

    def mat_to_list( self, mat ):
        vertices = list()

        for n in range(len(mat)):
            vertices.append(Vertex(n))

        for r in range(len(mat)):
            for c in range(r+1, len(mat[r])):
                if mat[r][c] != 0:
                    # print("{}: {}\t{}: {}".format(r, vertices[r].id, c, vertices[c].id))
                    edge = Edge(vertices[r], vertices[c], mat[r][c])
                    vertices[r].edge_list.append(edge)
                    vertices[c].edge_list.append(edge)

        return vertices

    def printGraph( self ):
        for vert in self.vertices:
            print('## {} ##'.format(vert.id))
            for edge in vert.edge_list:
                print('\t{} -> {}: {}'.format(edge.a.id, edge.b.id, edge.val))
            print()

class Vertex:
    def __init__( self, myid ):
        self.id = myid
        self.visited = False
        self.edge_list = list()

    def is_visited( self, val=True ):
        return self.visited

class Edge:
    def __init__( self, a, b, val ):
        # The two vertices.
        self.a   = a
        self.b   = b

        # The weight of the edge between the two vertices.
        self.val = val
