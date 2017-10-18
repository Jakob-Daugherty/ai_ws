from time import time
def FiB(n, F):

    if F[n] != -1:
        return F[n]
    F[n] = FiB(n-1, F) + FiB(n-2, F)
    return F[n]

def main():
    mark = time() * 1000
    result = None
    F = []
    for i in range(2, 1000):
        F.append(-1)
    F[0], F[1] = 1, 1
    result = FiB(100, F)
    print result
    now = time() * 1000
    diff = now - mark
    print 'time diff ->', diff


main()