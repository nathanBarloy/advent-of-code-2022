
f = open("input.txt", "r")

lines = list(map(lambda x: x.strip(), f.readlines()))



def prio(c):
    if "a"<=c<="z":
        return ord(c) - ord("a") + 1
    return 27 + ord(c) - ord("A")

tot = 0

"""  
for line in lines:
    half = len(line)//2
    l1 = line[:half]
    l2 = line[half:]
    s1 = set(l1)
    s2 = set(l2)
    v = s1.intersection(s2).pop()
    tot += prio(v)
"""

for i in range(0, len(lines), 3):
    s1 = set(lines[i])
    s2 = set(lines[i+1])
    s3 = set(lines[i+2])
    inter = s1.intersection(s2).intersection(s3)
    print(inter)
    badge = inter.pop()
    tot += prio(badge)

print(tot)
    

f.close()
