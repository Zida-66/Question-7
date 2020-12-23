def getI(x1,x2,l1,l2):
    indexI = x2 * l1 + x1
    return indexI

def getcoordinate(indexI,l1,l2):
    x1 = indexI % l1
    x2 = indexI // l1
    return x1,x2




