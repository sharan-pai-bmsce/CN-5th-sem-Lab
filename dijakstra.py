from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
        self.dist = []
        for i in range(0,vertices):
            self.dist.append(1000)
        
    
    def addEdge(self,u,v,pc):
        self.graph[u].append([v,pc])
        self.graph[v].append([u,pc])
    
    def dijakstra(self,root):
        visited=[root]
        self.dist[root]=0
        while len(visited)<self.vertices:
            ver=None
            dist=1000
            for i in visited:
                for j in self.graph[i]:
                    if j[0] not in visited:
                        if self.dist[i]+j[1]<dist:
                            ver=j[0]
                            dist=self.dist[i]+j[1]
                            
            visited.append(ver)
            self.dist[ver]=dist
        for i in visited:
            print(str(i)+"  Path cost:"+str(self.dist[i]))

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
g.dijakstra(1)