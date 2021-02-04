from collections import defaultdict
class Graph:
    def __init__(self,nodesCount):
        self.nodesCount=nodesCount
        self.graph=defaultdict(list)
    def addNewEdge(self,nodeA,nodeB):
        self.graph[nodeA].append(nodeB)
    def returnGraph(self):
        return self.graph
