#!/usr/bin/env python3

import numpy as np
from sys import argv

if len(argv) != 2:
  exit(1)

with open(argv[1], "rb") as f:
  num_nodes_y = int.from_bytes(f.read(4), "little")
  num_nodes_x = int.from_bytes(f.read(4), "little")
  G = np.fromfile(f, dtype="i4").reshape(num_nodes_y, num_nodes_x)

n = (num_nodes_y - 1) * (num_nodes_x - 1)
D = np.diag(4 * np.ones(n))

# 5-points finite difference laplacian stencil with weights:
#   -1
#-1 +4 -1
#   -1
for i in range(1, num_nodes_y - 1):
  for j in range(1, num_nodes_x - 1):
    for k in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
      if G[k] > 0:
        D[G[i, j] - 1, G[k] - 1] = -1

with open("D.bin", "wb") as f:
  f.write(np.asarray(D.shape, dtype="int32").data)
  f.write(D.data)
