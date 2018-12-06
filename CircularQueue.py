#大话数据结构第115页，采用了方法二，需要保证队列始终空出来至少一位
class CircularQueue():
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.front = 0
        self.rear = 0
        
        self.data = []
        for i in range(self.maxsize):
            self.data.append(None)

    def __repr__(self):
        return str(self.data)

    @property
    def length(self):
        return ((self.rear - self.front + self.maxsize) % self.maxsize)

    #将数据e加入队列
    def enQueue(self, e):
        if (self.rear + 1) % self.maxsize == self.front:
            return False

        self.data[self.rear] = e
        self.rear = (self.rear + 1) % self.maxsize      #rear向后移动一位

    def deQueue(self):
        if self.length <= 0:
            return False

        e = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.maxsize
        return e

if __name__ == '__main__':
    cq = CircularQueue(6)

        
