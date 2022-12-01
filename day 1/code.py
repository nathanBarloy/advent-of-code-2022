f = open("input.txt", "r")

raw = f.read()

elves = raw.split("\n\n")
elves = list(map(lambda x: list(map(int, x.split())), elves))
tot = list(map(sum, elves))
tot.sort()
print(sum(tot[-1:]))


f.close()
