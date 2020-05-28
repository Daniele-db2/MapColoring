from constraint import *
import random
import Graph
import Node
import TreeDecision
import CSP_Solver
import sys
import CSP
import Functions


def rmv(D):
    final_list = []
    for num in D:
        if num not in final_list:
            final_list.append(num)
    return final_list

dim = random.randint(5,100)
D = []
for i in range (1,dim):
    D.append(random.randint(5,1000))
D = rmv(D)
dim = len(D)

problem = Problem()
vals = Graph.createGraph(100, 0.5)
matrix = vals[0]
print "Matrice di adiacenza: \n", matrix
nodeList = vals[1]
for i in range (0,len(matrix)):
    u = nodeList[i]
    Node.Node.setDomain(u,D)
    Du = Node.Node.getDomain(u)
    problem.addVariable(u,Du)
    for j in range (0,len(matrix)):
        if (i != j):
            if (matrix[i][j] == 1):
                v = nodeList[j]
                Node.Node.setDomain(v,D)
                Dv = Node.Node.getDomain(v)
                if (isinstance(v,Problem)):
                    problem.addVariable(v, Dv)
                problem.addConstraint(AllDifferentConstraint())

#modificare grafo in albero, CSP.cutset_decomposition()
order = [0,len(nodeList),1]
[cycle,matrix] = TreeDecision.cutset_decomposition(matrix,order,0)
print "\nNuova matrice di adiacenza, nodi all'interno del ciclo eliminati\n",matrix

for i in range (0,len(cycle)):
    kappa = cycle[i]
    node = nodeList[kappa]
    CSP.assignment_cycle(nodeList,cycle,node,i)
for i in range (0,len(nodeList)):
    if (nodeList[i].color != 0):
        print nodeList[i]," ha colore: ",nodeList[i].color

Ass = CSP_Solver.tree_csp_solver(problem,nodeList,matrix)
