import numpy as np
from MyTestGraphs import *


def process_supernode_node(n, matrix_traversal_index, R, G):
    edge_data = G.edges(n, data=True)

    for e in edge_data:
        if e[2]['type'] == 'resistor' and e[1] != 'GND':
            connected_node_index = G.nodes.get(e[1])['index']
            R[matrix_traversal_index][connected_node_index] += 1 / e[2]['resistance']


def find_inverse_sum(n, G):
    sums = 0.0
    edge_data = G.edges(n, data=True)

    for e in edge_data:
        if e[2]['type'] == 'resistor':
            sums += -1 / e[2]['resistance']
    return sums


def find_v(matrixR, matrixI):
    Rinv = np.linalg.inv(matrixR)
    V = np.matmul(Rinv, matrixI)
    return V


def get_R_I(G):
    node_data = list(G.nodes(data=True))
    N = len(G.nodes) - 1

    edge_data = list(G.edges(data=True))
    num_of_edges = len(edge_data)

    R = np.array(np.zeros((N, N)))
    I = np.array(np.zeros((N, 1)))

    matrix_traversal_index = 0

    for e in edge_data:
        if e[2]['type'] == 'Vsource':
            n1 = e[0]
            n2 = e[1]
            n1_index = G.nodes.get(n1)['index']
            n2_index = G.nodes.get(n2)['index']

            I[matrix_traversal_index][0] = e[2]['voltage']

            if n1 == 'GND':
                R[matrix_traversal_index][n2_index] = 1
                matrix_traversal_index += 1
                G.nodes.get(n2)['skip'] = True

            elif n2 == 'GND':
                R[matrix_traversal_index][n1_index] = 1
                matrix_traversal_index += 1
                G.nodes.get(n1)['skip'] = True

            else:
                R[matrix_traversal_index][n2_index] = 1
                R[matrix_traversal_index][n1_index] = -1

                G.nodes.get(n1)['supernode'] = [True, n2]
                G.nodes.get(n2)['supernode'] = [True, n1]

                matrix_traversal_index += 1

    for n in node_data:
        curr_n_index = n[1]['index']
        if n[0] != 'GND' and not n[1]['supernode'][0] and not n[1]['skip']:
            R[matrix_traversal_index][curr_n_index] = find_inverse_sum(n[0], G)
            for neighbor_edge in G.edges(n[0], data=True):
                if neighbor_edge[2]['type'] == 'resistor':
                    curr_neighbor_node = neighbor_edge[1]
                    if curr_neighbor_node != 'GND':
                        curr_neighbor_index = G.nodes.get(curr_neighbor_node)['index']

                        R[matrix_traversal_index][curr_neighbor_index] = 1 / neighbor_edge[2]['resistance']
                elif neighbor_edge[2]['type'] == 'Csource':
                    if neighbor_edge[0] == neighbor_edge[2]['origin']:
                        I[matrix_traversal_index] += neighbor_edge[2]['current']
                    else:
                        I[matrix_traversal_index] += -neighbor_edge[2]['current']

            matrix_traversal_index += 1

        elif n[0] != 'GND' and not n[1]['skip']:
            other_supernode = n[1]['supernode'][1]
            other_supernode_index = G.nodes.get(other_supernode)['index']
            R[matrix_traversal_index][curr_n_index] = find_inverse_sum(n[0], G)
            R[matrix_traversal_index][other_supernode_index] = find_inverse_sum(other_supernode, G)
            process_supernode_node(n[0], matrix_traversal_index, R, G)
            process_supernode_node(other_supernode, matrix_traversal_index, R, G)
            G.nodes.get(other_supernode)['skip'] = True
            matrix_traversal_index += 1

    # print("R:")
    # print(R)
    # print("------------------")
    # print("I:")
    # print(I)
    # print("------------------")
    # print(find_v(R, I))

    return R, I


def print_info(R, I):
    print("R:")
    print(R)
    print("------------------")
    print("I:")
    print(I)
    print("------------------")
    V = find_v(R, I)
    for i in range(len(V)):
        print("V{} = {}".format(i + 1, V[i]))
    print()
    print("!Analysis Complete!\n")


# get_R_I(DIRECTED_Set1_I_NOOR.N)
# get_R_I(DIRECTED_Set1_E_MULTIPLE_VSandCS.E)
# get_R_I(DIRECTED_Set1_F_MULTIPLE_VSandCS.F)
# get_R_I(DIRECTED_Set1_C_VSandCS.C)
# get_R_I(DIRECTED_Set1_B_CS.B)
# print()
# print()
# get_R_I(DIRECTED_Set1_I_SUPERNODE.I)
# get_R_I(DIRECTED_Set1_A_SUPERNODE.A)
R, I = get_R_I(DIRECTED_Set1_I_NOOR.N)
# R, I = get_R_I(DIRECTED_H_3X3_Simple.H)
print_info(R, I)
# print(find_inverse_sum('v2', DIRECTED_Set1_A.A))
