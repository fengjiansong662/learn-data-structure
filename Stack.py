#大话数据结构P92，栈
class Stack():
    def __init__(self, size):
        self.size = size
        self.data = []
        self.top = -1

    #插入e作为新元素
    def push(self, e):
        if self.top == self.size - 1:               #栈满
            return False

        self.top += 1
        self.data.append(e)
        return True

    #删除栈顶的元素，并将出栈的元素返回
    def pop(self):
        if self.top == -1:                              #空栈
            return False

        e = self.data[self.top]
        del self.data[self.top]
        self.top -= 1
        return e

if __name__ == '__main__':
    s = Stack(5)
    
