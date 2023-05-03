#!/usr/bin/env python3

import numpy as np
from sys import argv

if len(argv) != 2:
  exit(1)

try:
  m = int(argv[1]) 
except ValueError:
  exit(1)

n = (m - 2)**2

G = np.zeros((m, m), dtype="int32")
G[1:m-1, 1:m-1].flat = np.arange(1, n + 1)

with open("G.bin", "wb") as f:
  f.write(np.asarray(G.shape, dtype="int32").data)
  f.write(G.data)
