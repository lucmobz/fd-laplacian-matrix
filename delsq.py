#!/usr/bin/env python3

import numpy as np
from sys import argv

# 5-points finite difference laplacian stencil with weights:
#   -1
#-1 +4 -1
#   -1
def delsq(G):
    m, n = G.shape
    D = np.diag(4 * np.ones((m - 2) * (n - 2)))
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            for k in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if G[k] > 0:
                    D[G[i, j] - 1, G[k] - 1] = -1
    return D

if __name__ == "__main__":
    if len(argv) != 2:
        exit(1)

    with open(argv[1], "rb") as f:
        m = int.from_bytes(f.read(4), "little")
        n = int.from_bytes(f.read(4), "little")
        G = np.fromfile(f, dtype="i4").reshape(m, n)
    
    D = delsq(G)

    with open("D.bin", "wb") as f:
        f.write(np.asarray(D.shape, dtype="int32").data)
        f.write(D.data)
    
    print(G)
    print(D)
