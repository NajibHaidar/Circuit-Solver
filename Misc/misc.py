# nodal_analysis(np.array([[1, 0, 0], [1 / 2, -11 / 6, 1 / 3], [1 / 4, 1 / 3, -13 / 12]]), np.array([1, 0, 0]))
# loop_analysis(np.array([[9, -3, -4], [-3, 6, -2], [-4, -2, 6]]), np.array([0, 0, 1]))

# nodal_analysis([[1, 0], [1, -3 / 2]], [3, 0])
# R, I = get_R_I(G)
# nodal_analysis(R, I)

# resistors = np.array([])
# nodes = np.array([])
# v_sources = np.array([])
#
# for node in G:
#     comp_type = G.nodes[node]['type']
#     if comp_type == "resistor":
#         resistors = np.append(resistors, node)
#     elif comp_type == "node":
#         nodes = np.append(nodes, node)
#     elif comp_type == "Vsource":
#         v_sources = np.append(v_sources, node)


# print("Resistors: ", resistors)
# print("Nodes: ", nodes)
# print("V Sources: ", v_sources)