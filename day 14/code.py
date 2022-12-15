import numpy as np


with open("input.txt") as f:
    lines = f.readlines()
    lines = list(map(lambda l: list(map(lambda t: tuple(map(int, t.split(","))), l.split(" -> "))), lines))


def print_cave(cave):
    for l in cave:
        print("".join(l))


min_c = 500
max_c = 500
max_l = 0
for line in lines:
    for (c,l) in line:
        max_l = max(max_l, l)
        max_c = max(max_c, c)
        min_c = min(min_c, c)


def p1():
    shift = min_c - 1
    height = max_l + 2
    width = max_c - min_c + 3
    cave = np.full((height, width), ".")


    for line in lines:
        for k in range(len(line)-1):
            a0, a1 = line[k]
            b0, b1 = line[k+1]
            if a0 == b0:  # Se déplace en colonne
                sens = 1 if a1 < b1 else -1
                for i in range(a1, b1+sens, sens):
                    cave[i, a0-shift] = "#"
            
            else:  # Se déplace en ligne
                sens = 1 if a0 < b0 else -1
                for j in range(a0, b0+sens, sens):
                    cave[a1, j-shift] = "#"

    start = (0, 500-shift)
    cave[start] = "+"

    total = 0
    finished = False
    while not finished:
        sandx, sandy = start
        placed = False
        while not placed:
            if sandx == height-1:
                finished = True
                break
            
            if cave[sandx+1, sandy] == ".":
                sandx += 1
            elif cave[sandx+1, sandy-1] == ".":
                sandx += 1
                sandy -= 1
            elif cave[sandx+1, sandy+1] == ".":
                sandx += 1
                sandy += 1
            else:
                cave[sandx, sandy] = "o"
                total += 1
                placed = True

    #print_cave(cave)
    print(total)



def p2():
    
    height = max_l + 3
    min_c = 500 - height
    max_c = 500 + height
    width = max_c - min_c -1
    shift = min_c + 1
    
    cave = np.full((height, width), ".")

    for j in range(width):
        cave[height-1, j] = "#"

    for line in lines:
        for k in range(len(line)-1):
            a0, a1 = line[k]
            b0, b1 = line[k+1]
            if a0 == b0:  # Se déplace en colonne
                sens = 1 if a1 < b1 else -1
                for i in range(a1, b1+sens, sens):
                    cave[i, a0-shift] = "#"
            
            else:  # Se déplace en ligne
                sens = 1 if a0 < b0 else -1
                for j in range(a0, b0+sens, sens):
                    cave[a1, j-shift] = "#"

    start = (0, 500-shift)
    cave[start] = "+"

    total = 0
    finished = False
    while not finished:
        sandx, sandy = start
        placed = False
        while not placed:
            
            if cave[sandx+1, sandy] == ".":
                sandx += 1
            elif cave[sandx+1, sandy-1] == ".":
                sandx += 1
                sandy -= 1
            elif cave[sandx+1, sandy+1] == ".":
                sandx += 1
                sandy += 1
            else:
                cave[sandx, sandy] = "o"
                total += 1
                placed = True

                if (sandx, sandy) == start:
                    finished = True

    #print_cave(cave)
    print(total)
    


p2()
