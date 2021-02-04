import graph
def DLS(graph,currentNode,goal,limit):
    print(currentNode)
    if currentNode == goal : return True

    if limit <= 0: return False

    for n in graph[currentNode]:
        if DLS(graph,n,goal,limit-1) == True : return True
    return False

def IDS(graph, currentNode,goal,maxDepth):
    for depth in range(maxDepth):
        print('===',depth)
        if DLS(graph,currentNode,goal,depth) == True : return True
    return False

myGraph=graph.Graph(15)
myGraph.addNewEdge(0,1)
myGraph.addNewEdge(0,2)

myGraph.addNewEdge(1,3)
myGraph.addNewEdge(1,4)

myGraph.addNewEdge(2,5)
myGraph.addNewEdge(2,6)

myGraph.addNewEdge(3,7)
myGraph.addNewEdge(3,8)

myGraph.addNewEdge(4,9)
myGraph.addNewEdge(4,10)

myGraph.addNewEdge(5,11)
myGraph.addNewEdge(5,12)

myGraph.addNewEdge(6,13)
myGraph.addNewEdge(6,14)

if IDS(myGraph.returnGraph(),0,5,4) ==True : print('Found')
else: print('Not Found')