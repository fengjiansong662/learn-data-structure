def ListInsert(l, i, e):
    if len(l) < 1:
        return False
    if ((i < 1) or (i > len(l))):
        return False
    if (i <= len(l)):
        l.append(l[len(l)-1])
        for k in range(len(l)-1, i-1, -1):
            l[k] = l[k-1]
        l[i-1] = e
    return True
