import Node

def Revise(problem, u, v):
    Rw = False
    Du = Node.Node.getDomain(u)
    Dv = Node.Node.getDomain(v)
    for i in Du:
        d = 0
        for j in Dv:
            if (i == j):
                d += 1
        if (d == len(Dv)):
            Du = Du - i
        else:
            return True
    return Rw

def TopSort(matrix, root):
    ts = []
    n = 0
    for i in range (0,len(matrix)):
        for j in range (0,len(matrix)):
            if (matrix[i][j] == 0):
                n += 1
        if (n == len(matrix)):
            ts.append(i)
    visit(matrix,ts,root)
    for i in range (0,len(matrix)):
        ts.append(i)
    ts = Remove(ts)
    return ts

def visit(matrix,ts,i):
    for j in range (0,len(matrix)):
        if (i != j):
            if (matrix[i][j] == 1):
                for k in range (0,len(matrix)):
                    matrix[k][i] = 0
                visit(matrix,ts,j)
    ts.append(i)

def Remove(ts):
    final_list = []
    for num in ts:
        if num not in final_list:
            final_list.append(num)
    return final_list

def DAC(problem, nodeList, matrix):
    for i in range (0, len(nodeList)):
        u = nodeList[i]
        for j in range(0, i):
            v = nodeList[j]
            if (matrix[i][j] == 1):
                Revise(problem, u, v)