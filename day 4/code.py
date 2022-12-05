f = open("input.txt", "r")

lines = list(map(lambda x: tuple(map(lambda y: tuple(map(int, y.split("-"))), x.strip().split(","))), f.readlines()))

tot = 0
for (d1,f1), (d2,f2) in lines:
    # if (d1>=d2 and f1<=f2) or (d1<=d2 and f1>=f2):
    if not (d1>f2 or d2>f1):
        tot += 1

print(tot)

f.close()