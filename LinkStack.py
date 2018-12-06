class LinkStackNode():
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node  = next_node

class LinkStack():
    def __init__(self, top = None):
        self.top = top
        self.count = 0

    #将新数据放入链栈
    def push(self, data):
        node = LinkStackNode(data)          #新数据变成新节点
        node.next_node = self.top
        self.top = node
        self.count += 1

    #删除链栈的栈顶元素，并将删除的数据返回
    def pop(self):
        if self.count < 1:
            return False
        
        n = self.top
        e = n.data
        self.top = self.top.next_node
        del n
        self.count -= 1
        return e

if __name__ == '__main__':
    node1 = LinkStackNode(1)
    node2 = LinkStackNode(2)
    node3 = LinkStackNode(3)
    node4 = LinkStackNode(4)
    ls1 = LinkStack()
