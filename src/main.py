import numpy as np
import sys
import os

# Ensure parent directory is in path to import circuit definitions
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.test_circuits import *

# -------------------- Matrix Utilities --------------------

def find_v(matrixR, matrixI):
    Rinv = np.linalg.inv(matrixR)
    V = np.matmul(Rinv, matrixI)
    return V

def print_info(R, I):
    print("R matrix:\n", R, "\n")
    print("I vector:\n", I, "\n")
    V = find_v(R, I)
    for i, v in enumerate(V, 1):
        print(f"V{i} = {v[0]}")
    print("\n! Analysis Complete !\n")

# -------------------- MNA Core Functions --------------------

def process_supernode_node(n, matrix_traversal_index, R, G):
    for _, neighbor, attrs in G.edges(n, data=True):
        if attrs['type'] == 'resistor' and neighbor != 'GND':
            idx = G.nodes[neighbor]['index']
            R[matrix_traversal_index][idx] += 1 / attrs['resistance']

def find_inverse_sum(n, G):
    return sum(
        -1 / attrs['resistance']
        for _, _, attrs in G.edges(n, data=True)
        if attrs['type'] == 'resistor'
    )

def get_R_I(G):
    node_data = list(G.nodes(data=True))
    N = len(G.nodes) - 1
    edge_data = list(G.edges(data=True))

    R = np.zeros((N, N))
    I = np.zeros((N, 1))
    idx = 0

    for u, v, attrs in edge_data:
        if attrs['type'] == 'Vsource':
            i_u, i_v = G.nodes[u]['index'], G.nodes[v]['index']
            I[idx][0] = attrs['voltage']

            if u == 'GND':
                R[idx][i_v] = 1
                G.nodes[v]['skip'] = True
            elif v == 'GND':
                R[idx][i_u] = 1
                G.nodes[u]['skip'] = True
            else:
                R[idx][i_v] = 1
                R[idx][i_u] = -1
                G.nodes[u]['supernode'] = [True, v]
                G.nodes[v]['supernode'] = [True, u]
            idx += 1

    for name, data in node_data:
        i = data['index']
        if name == 'GND' or data['skip']:
            continue
        if not data['supernode'][0]:
            R[idx][i] = find_inverse_sum(name, G)
            for _, neighbor, attrs in G.edges(name, data=True):
                if attrs['type'] == 'resistor' and neighbor != 'GND':
                    j = G.nodes[neighbor]['index']
                    R[idx][j] = 1 / attrs['resistance']
                elif attrs['type'] == 'Csource':
                    sign = 1 if name == attrs['origin'] else -1
                    I[idx][0] += sign * attrs['current']
        else:
            j = G.nodes[data['supernode'][1]]['index']
            R[idx][i] = find_inverse_sum(name, G)
            R[idx][j] = find_inverse_sum(data['supernode'][1], G)
            process_supernode_node(name, idx, R, G)
            process_supernode_node(data['supernode'][1], idx, R, G)
            G.nodes[data['supernode'][1]]['skip'] = True
        idx += 1

    return R, I

# -------------------- Example Execution --------------------

if __name__ == "__main__":
    # Pick a test circuit to run
    circuit_funcs = [
        directed_h_3x3_simple,
        directed_set1_a,
        directed_set1_a_supernode,
        directed_set1_b_cs,
        directed_set1_c_vsandcs,
        directed_set1_e_multiple_vsandcs,
        directed_set1_f_multiple_vsandcs,
        directed_set1_i_noor,
        directed_set1_i_supernode,
    ]

    for circuit_func in circuit_funcs:
        print(f"Processing circuit: {circuit_func.__name__}")
        R, I = get_R_I(circuit_func())
        print_info(R, I)
