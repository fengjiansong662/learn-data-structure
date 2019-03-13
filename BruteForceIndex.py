#大话数据结构P133，朴素模式匹配

#返回字符串b在主字符串a中第i个字符之后的位置，若不匹配则返回-1
def bruteForceIndex(a, b, i):
    for j in range(i-1, len(a)-len(b)+1):
        for k in range(len(b)):
            if b[k] != a[j+k]:
                break
            if k == len(b) - 1:
                return j + 1
    return -1
