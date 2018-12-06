#大话数据结构P119，队列的链式存储

class Node():
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

class LinkQueue():
    def __init__(self):
        self.head = Node(None)
        self.front = self.head
        self.rear = self.head

    #插入元素e为队列的队尾元素
    def enQueue(self, e):
        node = Node(e)
        self.rear.next_node = node
        self.rear = node

    #删除队列的队首元素，并将元素值返回
    def deQueue(self):
        if self.rear == self.front:                 #队列为空时返回False
            return False

        n = self.front.next_node
        e = n.data
        self.front.next_node = n.next_node
        if self.rear == n:                          #如果队列只有一个值，那么此时队尾指针也要变化
            self.rear = self.front
        del n
        return e

    def __repr__(self):
        l = []
        self.n = self.front.next_node
        while self.n:
            l.append(self.n.data)
            self.n = self.n.next_node
        return str(l)

if __name__ == '__main__':
    lq = LinkQueue()
        
