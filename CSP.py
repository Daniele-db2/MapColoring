import Node

def assignment(nodeList, matrix, u, kappa):
    Dmn = Node.Node.getDomain(u)
    for z in range (0,len(matrix)):
        if (z != kappa):
            zeta = matrix[kappa][z]
            nd = nodeList[z]
            if (zeta == 1):
                if (nd.color != 0):
                    if (nd.color in Dmn):
                        i = Dmn.index(nd.color)
                        Dmn = eliminate(Dmn,i)
                        print "colore eliminato: ", nd.color, "nodo: ", kappa
    #print "dominio: ", Dmn
    Node.Node.setColor(u, Dmn)

def eliminate(Dmn, i):
    for z in range (i, len(Dmn)-1):
        Dmn[z] = Dmn[z+1]
    del Dmn[len(Dmn)-1]
    return Dmn

def assignment_cycle(nodeList, cycle, u, i):
    Dmn = Node.Node.getDomain(u)
    for z in range (0,len(cycle)):
        if (z != i):
            zeta = cycle[z]
            nd = nodeList[zeta]
            if ((nd.color != 0) and (nd.color in Dmn)):
                i = Dmn.index(nd.color)
                Dmn = eliminate(Dmn,i)
                #print "colore eliminato: ", nd.color
    #print "dominio: ", Dmn
    Node.Node.setColor(u, Dmn)

