def ggt(m,n):
    if m > n:
        p = m%n
        if p == 0:
            return n
        else:
            return ggt(n,p)
    else:
        p = n%m
        if p == 0:
            return m
        else:
            return ggt(m,p)