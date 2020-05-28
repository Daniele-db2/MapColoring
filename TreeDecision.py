def find_cycle(matrix, order, n, m, root, cycle):
    for i in order:
        for j in range(0, len(matrix)):
            if (matrix[i][j] == 1):
                if (j != n and j != m):
                    if (j != root):
                        cycle.append(j)
                        #print "valore aggiunto, ", cycle
                        n = m
                        m = j
                        cycle = find_cycle(matrix, order, n, m, root, cycle)
                    else:
                        cycle.append(root)
                        #print "ciclo", cycle
                        break
        return cycle

def cutset_decomposition(matrix, order, root):
    cycle = []
    mx = matrix
    n = order[0]
    m = order[0]
    print root
    cycle = find_cycle(mx, order, n, m, root, cycle)
    cycle = rmv(cycle)
    print "\nCiclo: ",cycle
    for pos in range (0,len(cycle)):
        ind = cycle[pos]
        for j in range(0, len(matrix)):
            if j in cycle:
                mx[j][ind] = 0
                mx[ind][j] = 0
    return [cycle,mx]

def rmv (cycle):
    final_list = []
    for num in cycle:
        if num not in final_list:
            final_list.append(num)
    return final_list


# matrix =([[1, 1, 1, 0, 1, 1, 0],
#           [1, 1, 1, 0, 0, 0, 0],
#           [1, 1, 1, 1, 1, 0, 0],
#           [0, 0, 1, 1, 1, 0, 0],
#           [1, 0, 1, 1, 1, 1, 0],
#           [1, 0, 0, 0, 1, 1, 1],
#           [1, 0, 0, 0, 0, 1, 1]])
# order = [0,1,2,3,4,5]
# cutset_decomposition(matrix,order,0)
# print matrix

