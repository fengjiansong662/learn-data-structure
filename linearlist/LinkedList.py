class Node():
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return str(self.data)

class LinkedList():
    def __init__(self, head = None):
        self.head = head

    def __len__(self):
        count = 0
        node = self.head
        while node:
            node = node.next_node
            count += 1
        return count

    def printList(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next_node
            
    #获取第i个元素的值        
    def getElem(self, i):
        if len(self) < 1:
            return False

        j = 1
        node = self.head
        
        while j < i and j < len(self):
            node = node.next_node
            j += 1
            
        if j != i:
            return False    
        return node.data
    
    #在第i个位置插入元素e
    def InsertElem(self, i, e):
        if len(self) < 1:
            return False

        j = 1
        node = self.head
        #如果插入到链表头
        if i == 1:
            node_new = Node(e)
            node_new.next_node = node
            self.head = node_new
            return
        
        while j < i-1 and j < len(self):
            j += 1
            node = node.next_node

        if j != i-1:
            return False

        node_new = Node(e)
        node_new.next_node = node.next_node
        node.next_node = node_new
        
    #删除第i个元素
    def DeleteElem(self, i):
        if len(self) < 1:
            return False

        j = 1
        node = self.head

        if i == 1:
            self.head = node.next_node
            return

        while j < i-1 and j < len(self)-1:
            j += 1
            node = node.next_node

        if j != i-1:
            return False

        node.next_node = node.next_node.next_node

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.next_node = n2
n2.next_node = n3
n3.next_node = n4

l_empty = LinkedList()
l2 = LinkedList(n1)
