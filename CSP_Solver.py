import Functions
import random
import Node
import CSP

def tree_csp_solver(problem, nodeList, matrix):
    Ass = []
    j = random.randrange(0,len(nodeList))
    root = nodeList[j]
    Functions.DAC(problem, nodeList, matrix)
    n = 0
    for u in nodeList:
        d = Node.Node.getDomain(u)
        if (len(d) == 0):
            return False
    mx = matrix
    ts = Functions.TopSort(mx, j)
    NL = []
    print "\n Ordine:"
    for j in ts:
        print ts[j],
    for i in ts:
        k = ts[i]
        node = nodeList[k]
        NL.append(node)
    print "\n", NL
    for u in NL:
        if (u.color == 0):
            kappa = nodeList.index(u)
            CSP.assignment(NL, matrix, u, kappa)
            ass = Node.Node.getColor(u)
            Ass.append(ass)
        else:
            Ass.append(u.color)
    print Ass
    return Ass