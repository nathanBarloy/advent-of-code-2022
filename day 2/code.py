f = open("input.txt", "r")

lines = f.readlines()
lines = list(map(lambda x: x.split(), lines))

"""
myScore = {"X": 1,
           "Y": 2,
           "Z": 3}

winScore = {("A", "X"): 3,
            ("A", "Y"): 6,
            ("A", "Z"): 0,
            ("B", "X"): 0,
            ("B", "Y"): 3,
            ("B", "Z"): 6,
            ("C", "X"): 6,
            ("C", "Y"): 0,
            ("C", "Z"): 3}
"""

myScore = {("A", "X"): 3,
           ("A", "Y"): 1,
           ("A", "Z"): 2,
           ("B", "X"): 1,
           ("B", "Y"): 2,
           ("B", "Z"): 3,
           ("C", "X"): 2,
           ("C", "Y"): 3,
           ("C", "Z"): 1,}

winScore = {"X": 0,
            "Y": 3,
            "Z": 6}

score = 0
for a, b in lines :
    #score += myScore[b]
    #score += winScore[(a,b)]
    score += winScore[b]
    score += myScore[(a,b)]

print(score)



f.close()