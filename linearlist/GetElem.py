def GetElem(l, i):
    if len(l) < 1:
        return False
    j = 1
    while (j < i and j <= len(l)):
        j += 1

    if j > len(l) or j != i:
        return False

    return l[i-1]
