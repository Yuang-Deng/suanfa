import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
# 读取文件，获取节点和边
base_dir = "/Users/Enko/Desktop/Courses/Algorithms/Lab04-Yuanhang-Yin/"
pdf = PdfPages('g.pdf')
fig = plt.figure()
for i in range(6):
    plt.subplot(2, 3, i + 1)
    fn = open(base_dir + "compnode" + str(i+1) + ".out", "r")
    fe = open(base_dir + "compedge" + str(i+1) + ".out", "r")
    edgelist = []
    nodess = fn.readline()
    nodelist = nodess.strip().split(' ')
    edges = fe.readlines()
    n, m = len(nodelist), 0
    for line in edges:
        nodes = line.strip().split(' ')
        m += 1
        if nodes[1] in nodelist:
            edgelist.append((nodes[0], nodes[1]))
    fn.close()
    fe.close()


    # 有向图绘制
    G = nx.DiGraph()
    G.add_nodes_from(nodelist)
    G.add_edges_from(edgelist)
    nx.draw_networkx(G, pos=None, arrows=True, with_labels=True, alpha=0.5,
                     node_size=[50] * n, font_size=3, arrowsize=2,
                     linewidths=0.1, width=0.3, arrowstyle='->')
pdf.savefig()
pdf.close()
plt.show()
