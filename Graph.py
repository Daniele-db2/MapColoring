import Node
import AdjacencyMatrix

def createGraph(vertices, P):
    nodeList=[]
    for i in range(0,vertices):
        nodeList.append(Node.Node())
    adjMatrix=AdjacencyMatrix.createMatrix(vertices,P)
    for i in range(0, vertices):
        for j in range(0,vertices):
            if adjMatrix[i][j]==1:
                nodeList[i].addSon(nodeList[j])
    returnList=[adjMatrix,nodeList]
    return returnList


