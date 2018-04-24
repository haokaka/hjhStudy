import networkx as nx
import random
import os

def DyGenerator(g, addNode, p, q):
    g.add_node(addNode)
    selectOne = random.sample(g.nodes(), 1)[0]
    neighbor = nx.neighbors(g, selectOne)
    for each in neighbor:
        g.add_edge(each, addNode)
    if random.uniform(0, 1) <= p:
        g.add_edge(selectOne, addNode)
        if len(neighbor) > 1 and random.uniform(0, 1) <= q:
            selectNeighbor = random.sample(neighbor, 1)[0]
            g.remove_node(selectNeighbor)

def make_dyNet(path, p, q, length, nodeName):
    for i in range(3, 1000):
        DyGenerator(g, nodeName+'%s' % i, p, q)
        time = 1000 / length
        if i % time == 0:
            nx.write_edgelist(g, path + '\dyNetT%s.txt' % i, data=False, delimiter='\t')
            print(i)


def main():
    p = 0.3
    q = 0.7
    for j in range(1, 6):
        dirPath = os.path.join(path, 'DyNet%s' % j)
        if os.path.exists(dirPath):
            make_dyNet(dirPath, p, q, 10, 'a')
        else:
            os.mkdir(dirPath)
            make_dyNet(dirPath, p, q, 10, 'a')

        print('j:', j)

def prepareForTWADN():
    path = 'G:\machine learning\myown\DynamicNetwork\p0.3_q0.7'
    for j in range(1, 6):
        dirPath = os.path.join(path, 'DyNet%s' % j)
        if os.path.exists(dirPath):
            fileList = os.listdir(dirPath)
            fw = open(os.path.join(dirPath, 'TWADNdynet%s.txt' % j), 'w')
            for each in fileList:
                fr = open(os.path.join(dirPath, each), 'r')
                for edge in fr.readlines():
                    fw.write(each + '\t' + edge)
                fr.close()
            fw.close()
            print(dirPath, 'finish')

if __name__ == '__main__':
    path = 'G:\machine learning\myown\DynamicNetwork\p0.3_q0.7'

    g = nx.Graph()
    g.add_edge('a0', 'a1')
    g.add_edge('a0', 'a2')
    g.add_edge('a2', 'a1')
    prepareForTWADN()
    # main()