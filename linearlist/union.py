#实现两个线性表的合并
def union(La, Lb):
    for l in La:
        if not l in Lb:
            Lb.append(l)
    return Lb
