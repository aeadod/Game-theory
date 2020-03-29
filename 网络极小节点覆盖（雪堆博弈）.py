import random
# 收益矩阵
r = 0.02
interest = {
    'C': {'C': (1, 1), 'D': (1 - r, 1 + r)},
    'D': {'C': (1 + r, 1 - r), 'D': (0, 0)}
}
# 结点数据结构
class Node(object):
    def __init__(self):
        if (random.random() < 0.5):
            self.state = 'C'
        else:
            self.state = 'D'
        self.value = 0
        self.all_value = 0
        self.neighbour_number = 0
        self.nb = list()
        pass
    pass

class Network(object):
    def __init__(self, n):
        self.numbers = n
        self.nodes = list()
        self.edges = list()
        self.generateNode()
    # 生成n个结点
    def generateNode(self):
        for i in range(self.numbers):
            tmp_node = Node()
            self.nodes.append(tmp_node)
    def addEgde(self, es):
        for e in es:
            self.edges.append(e)
    # 保存结点的邻居
    def saveNb(self):
        for a, b in self.edges:
            a.nb.append(self.nodes.index(b))
            b.nb.append(self.nodes.index(a))
        for i in range(self.numbers):
            self.nodes[i].neighbour_number = len(self.nodes[i].nb)
    # 计算每个结点的平均收益
    def calValue(self):
        for i in range(self.numbers):
            self.nodes[i].all_value = 0
        for a, b in self.edges:
            a.all_value += interest[a.state][b.state][0]
            b.all_value += interest[a.state][b.state][1]
        for i in range(self.numbers):
            self.nodes[i].value = self.nodes[i].all_value / self.nodes[i].neighbour_number
    # 更新状态
    def updateState(self):
        for i in range(self.numbers):
            if (self.nodes[i].state == 'C'):
                reward1 = self.getReward(i)
                self.nodes[i].state = 'D'
                reward2 = self.getReward(i)
                if (reward2 <= reward1):
                    self.nodes[i].state = 'C'
            elif (self.nodes[i].state == 'D'):
                reward1 = self.getReward(i)
                self.nodes[i].state = 'C'
                reward2 = self.getReward(i)
                if (reward2 <= reward1):
                    self.nodes[i].state = 'D'

    # 计算单个结点的收益
    def getReward(self, i):
        all_value = 0
        for s in self.nodes[i].nb:
            all_value += interest[self.nodes[i].state][self.nodes[s].state][0]
        value = all_value / self.nodes[i].neighbour_number
        return value
    # 获得总收益
    def getAllReward(self):
        self.reward = 0
        for a, b in self.edges:
            self.reward += sum(interest[a.state][b.state])
        return self.reward
    #输出结果
    def outputState(self):
        print('----------------')
        for i in range(self.numbers):
            print('%d:%c %f ' % (i, self.nodes[i].state, self.nodes[i].value))
        print(self.reward)
        print('----------------')

if __name__ == '__main__':
    def designNet2():
        net = Network(21)
        edge_list = [(0, 10), (0, 20),
                     (1, 12), (1, 2),
                     (2, 16),(2,9),
                     (3, 11), (3, 4),(3,6),
                     (5, 18),(5,14),
                     (6, 13),
                     (7, 15), (7,17),
                     (8,9),(8,20),
                     (9,16),
                     (10,11),
                     (11,19),
                     (12,13),(12,17),
                     (18,19),
                     (19,20)
                     ]
        net.addEgde(
            ({net.nodes[a], net.nodes[b]} for a, b in edge_list))
        return net
    mynet = designNet2()
    mynet.saveNb()
    max_reward = 0
    # i=0
    # max_reward保持3次才输出
    i1 = 0
    while True:
        reward = mynet.getAllReward()
        if (max_reward == reward):
            i1 += 1
            if (i1 == 3):
                mynet.calValue()
                mynet.outputState()
                break
        elif (reward > max_reward):
            i1 = 0
            max_reward = reward
        mynet.updateState()
#C表示合作，D表示背叛