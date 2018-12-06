#大话数据结构P94，双栈
class DoubleStack():
    def __init__(self, size):
        self.size = size
        self.top1 = -1
        self.top2 = size
        self.data = []
        for i in range(size):
            self.data.append(None)

    #插入元素e作为新的栈顶元素
    def push(self, e, stackNumber):
        if self.top1 + 1 == self.top2:              #满栈
            return False

        if stackNumber == 1:
            self.top1 += 1
            self.data[self.top1] = e
        elif stackNumber == 2:
            self.top2 -= 1
            self.data[self.top2] = e
        return True

    #删除栈顶元素，并返回出栈的元素
    def pop(self, stackNumber):
        if stackNumber == 1:
            if self.top1 == -1:                         #栈1是空栈
                return False
            e = self.data[self.top1]
            self.data[self.top1] = None
            self.top1 -= 1
            return e

        elif stackNumber == 2:
            if self.top2 == self.size:
                return False
            e = self.data[self.top2]
            self.data[self.top2] = None
            self.top2 += 1
            return e

if __name__ == '__main__':
    ds = DoubleStack(6)
