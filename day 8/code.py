import numpy as np


with open("input.txt") as f:
    # lines = "8888\n8898\n8888".split("\n")
    lines = f.read().split("\n")

forest = np.array(list(map(list, lines)), dtype=int)


def p1(forest):
    height, width = forest.shape
    tot = 0
    for i in range(height):
        for j in range(width):
            if i==0 or i==height-1 or j==0 or j==width-1:
                tot += 1
                continue
            
            val = forest[i,j]
            for k in range(j):
                if forest[i,k] >= val:
                    break
            else:
                # print(i,j,"from ouest")
                tot += 1
                continue
            
            for k in range(j+1, width):
                if forest[i,k] >= val:
                    break
            else:
                # print(i,j,"from est")
                tot += 1
                continue
            
            for k in range(i):
                if forest[k,j] >= val:
                    break
            else:
                # print(i,j,"from north")
                tot += 1
                continue
            
            for k in range(i+1, height):
                if forest[k,j] >= val:
                    break
            else:
                # print(i,j,"from south")
                tot += 1
                continue

    print(tot)


def p2(forest):
    height, width = forest.shape
    res = 0
    pos = (-1,-1)
    for i in range(height):
        for j in range(width):
            if i==0 or i==height-1 or j==0 or j==width-1:
                continue
            
            val = forest[i,j]
            score = 1

            dist = 0
            for k in range(j-1, -1, -1):
                dist += 1
                if forest[i,k] >= val:
                    break
            score *= dist
            
            dist = 0
            for k in range(j+1, width):
                dist += 1
                if forest[i,k] >= val:
                    break
            score *= dist
            
            dist = 0
            for k in range(i-1, -1, -1):
                dist += 1
                if forest[k,j] >= val:
                    break
            score *= dist
            
            dist = 0
            for k in range(i+1, height):
                dist += 1
                if forest[k,j] >= val:
                    break
            score *= dist
            
            if score > res:
                res = score
                pos = (i,j)

    print(res, pos)

p2(forest)
