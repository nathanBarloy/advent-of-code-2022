from numpy_map import numpy_map

def dist(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def combine_intervalles(l):
    ls = sorted(l, key=lambda x: x[0])
    res = []
    while len(ls) > 0:
        inter = ls.pop(0)
        while len(ls) > 0 and ls[0][0] <= inter[1]+1:
            start, end = ls.pop(0)
            inter = (inter[0], max(inter[1], end))
        res.append(inter)
    return res

lines = []
with open("input.txt") as f:
    for l in f.readlines():
        a, b = l.split(": ")
        x1, y1 = a.split(", ")
        x2, y2 = b.split(", ")
        x1 = int(x1.split("=")[1])
        x2 = int(x2.split("=")[1])
        y1 = int(y1.split("=")[1])
        y2 = int(y2.split("=")[1])
        lines.append(((y1, x1), (y2, x2), dist((y1, x1), (y2, x2))))

n = 4000000
pourcent = n//100
i = pourcent
k = 0
for l in range(n):
    if i<0:
        k+=1
        print(k)
        i = pourcent
    i -= 1

    intervalles = []
    for s, b, d in lines:
        offset = abs(s[0] - l)
        if offset <= d:
            start = s[1] - (d-offset)
            end = s[1] + (d-offset)
            intervalles.append((start, end))

    intervalles = combine_intervalles(intervalles)
    if len(intervalles) > 1:
        print(intervalles[0][1]+1, l)

"""
print(intervalles)

total = 0
for s,e in intervalles:
    total += e-s+1

beacons = set()
for scan, beacon, d in lines:  
    if beacon[0] == l and (beacon not in beacons):
        beacons.add(beacon)
        total -= 1

print(total)
"""


