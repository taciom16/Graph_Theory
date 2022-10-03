import networkx as nx

def criaDiGraph(diGraph):
    diGraph = nx.DiGraph()

def addNodesDiGraph(nodeList, diGraph):
    diGraph.add_nodes_from(nodeList)

def addEdgesDiGraph(edgeList, diGraph):
    diGraph.add_edges_from(edgeList)

def getNodeInDegree(diGraph, node): #requisito 7

    inDegreeList = diGraph.in_degree()
    for j in inDegreeList:
        if node == j[0]+1:
            inDegree = j[1]
    return inDegree

def getNodeOutDegree(diGraph, node): #requisito 7

    outDegreeList = diGraph.out_degree()
    for j in outDegreeList:
        if node == j[0]+1:
            outDegree = j[1]
    return outDegree

#REQUISITO SURPRESA
def greatInDegree(diGraph): #maior grau de entrada
    inDegreeList = diGraph.in_degree()
    sortDegreeList = sorted(inDegreeList, key = lambda i: i[1], reverse = True)[0]
    return("o vertice com maior grau de entrada é o vertice ", sortDegreeList[0], "com o grau ", sortDegreeList[1])

def greatOutDegree(diGraph): #maior grau de entrada
    outDegreeList = diGraph.in_degree()
    sortDegreeList = sorted(outDegreeList, key = lambda i: i[1], reverse = True)[0]
    return("o vertice com maior grau de saída é o vertice ", sortDegreeList[0], "com o grau ", sortDegreeList[1])

def greatestDegree(diGraph, nodeList): #maior grau total
    inDegreeList = diGraph.in_degree()
    outDegreeList = diGraph.in_degree()
    totalDegree = []
    for tupleIn, tupleOut in zip(inDegreeList, outDegreeList):
        sum = tupleIn[1] + tupleOut[1]
        totalDegree.append(sum)

    maxDegree = max(totalDegree) #achando vertice pelo índice do grau total
    indexDegree = totalDegree.index(maxDegree)
    greatNode = nodeList[indexDegree]
    return("o vértice com maior grau total é o vertice ", greatNode, "com um grau total de ", maxDegree)
