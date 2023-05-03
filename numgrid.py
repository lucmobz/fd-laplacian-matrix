#!/usr/bin/env python3

import numpy as np
from sys import argv

def numgrid(n):
    G = np.zeros((n, n), dtype="int32")
    G[1:n - 1, 1:n - 1].flat = np.arange(1, (n - 2)**2 + 1)
    return G

if __name__ == "__main__":
  if len(argv) != 2:
      exit(1)
  try:
      n = int(argv[1])
  except ValueError:
      exit(1)

  G = numgrid(n)

  with open("G.bin", "wb") as f:
      f.write(np.asarray(G.shape, dtype="int32").data)
      f.write(G.data)
