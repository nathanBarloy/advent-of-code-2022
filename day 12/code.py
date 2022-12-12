import numpy as np
from math import inf


height_map = None
with open("input.txt") as f:
    height_map = np.array(list(map(lambda x: list(x), f.read().split("\n"))))

n = len(height_map)
m = len(height_map[0])
start_pos = (-1, -1)
end_pos = (-1, -1)
for i in range(n):
    for j in range(m):
        if height_map[i, j] == "S":
            start_pos = (i,j)
            height_map[i, j] = "a"
        if height_map[i, j] == "E":
            end_pos = (i,j)
            height_map[i, j] = "z"


voisin = {}
for i in range(n):
    for j in range(m):
        h = ord(height_map[i,j])
        voisin[(i,j)] = []
        for pos in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
            if pos[0]>=0 and pos[0]<n and pos[1]>=0 and pos[1]<m:
                if h+1 >= ord(height_map[pos]):
                    voisin[(i,j)].append(pos)

res = []
for i in range(n):
    seen = {(i,0): 0}
    while end_pos not in seen:
        shortest = inf
        next_s = (-1, -1)
        for s in seen:
            for v in voisin[s]:
                if v not in seen:
                    if seen[s]+1 < shortest:
                        shortest = seen[s]+1
                        next_s = v
        seen[next_s] = shortest

    print(seen[end_pos])
    res.append(seen[end_pos])
print(min(res))




