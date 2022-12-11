from math import gcd


def lcm(l):
    res = 1
    for i in l:
        res = res*i//gcd(res, i)
    return res


monkeys = []


class Monkey:
    def __init__(self, input_text):
        self.items = []
        self.isdiv = 0
        self.op = ""
        self.opval = 0
        self.true = -1
        self.false = -1
        self.nb_items = 0
        self.lcm = 0

        a,b,c,d,e,f = input_text.split("\n")
        for x in b[18:].split(", "):
            self.items.append(int(x))
        self.op, aux = c[23:].split()
        if aux == "old":
            self.opval = "old"
        else:
            self.opval = int(aux)
        self.isdiv = int(d[21:])
        self.true = int(e[29:])
        self.false = int(f[30:])
    
    def add(self, x):
        self.items.append(x)
    
    def add_lcm(self, val):
        self.lcm = val
        
    def operate(self, x):
        if self.opval == "old":
            #return (x*x)//3
            return (x*x)%self.lcm
        if self.op == "+":
            #return (x + self.opval)//3
            return (x + self.opval)%self.lcm
        if self.op == "*":
            #return (x * self.opval)//3
            return (x * self.opval)%self.lcm
        print("Operation inconnue")
    
    def turn(self):
        for x in self.items:
            new = self.operate(x)
            if new % self.isdiv == 0:
                monkeys[self.true].add(new)
            else:
                monkeys[self.false].add(new)
        self.nb_items += len(self.items)
        self.items = []



with open("input.txt") as f:
    inps = f.read().split("\n\n")

for x in inps:
    monkeys.append(Monkey(x))

lcm_val = lcm([m.isdiv for m in monkeys])
for m in monkeys:
    m.add_lcm(lcm_val)

for _ in range(10000):
    for m in monkeys:
        m.turn()

for m in monkeys:
    print(m.nb_items)

best = sorted([m.nb_items for m in monkeys])[-2:]
print(best, best[0]*best[1])
