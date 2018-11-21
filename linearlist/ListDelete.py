def ListDelete(L, i):
    if len(L) < 1:
        return False
    if i < 1 or i > len(L):
        return False
    for k in range(i, len(L)):
        L[k-1] = L[k]
    L.pop()
    return True
