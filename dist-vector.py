from collections import defaultdict
# from typing import DefaultDict
import math

class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
        # self.pc = defaultdict(list)

    # def vertexList(self):
        for i in range(self.vertices):
            self.graph[i]=[]
            for j in range(self.vertices):
                if i==j:
                    self.graph[i].append(0)
                else:
                    self.graph[i].append(1000)
    
    def addEdge(self,u,v,pc):
        self.graph[u][v]=self.graph[v][u]=pc
    
    def distVector(self):
        l=1
        while l<3:
            # For each vertex
            for i in range(0,self.vertices):
                # To find its neighbour
                for j in range(0,self.vertices):
                    # If it is a neighbour
                    if self.graph[i][j]!=1000:
                        x=self.graph[i][j]
                        # Loop through its table
                        for k in range(0,self.vertices):
                            self.graph[i][k]=min(self.graph[i][k],self.graph[j][k]+x)
            l+=1
        # print(self.graph)

g=Graph(7)
g.addEdge(0,1,2)
g.addEdge(0,3,3)
g.addEdge(1,4,4)
g.addEdge(1,2,5)
g.addEdge(2,5,4)
g.addEdge(2,6,3)
g.addEdge(4,3,5)
g.addEdge(4,5,2)
g.addEdge(5,6,1) 

print("Before applying distance vector:")
for i in g.graph:
    print(str(i)+":"+str(g.graph[i]))

g.distVector()
print("After applying distance vector:")
for i in g.graph:
    print(str(i)+":"+str(g.graph[i]))
  
