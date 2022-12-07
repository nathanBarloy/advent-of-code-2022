import math


class FileTree:
    def __init__(self, name, parent, size=0):
        self.name = name
        self.parent = parent
        self.size = size
        self.isDir = (size == 0)
        if parent is not None:
            self.path = parent.path + name + "/"
        else:
            self.path = "/"
        self.childs = {}
        self.totalSize = size

    def addFile(self, name, size):
        self.childs[name] = FileTree(name, self, size)

    def addDir(self, name):
        self.childs[name] = FileTree(name, self)

    def calcSize(self):
        if not self.isDir:
            return self.totalSize
        for child in self.childs.values():
            self.totalSize += child.calcSize()
        return self.totalSize

    def p1(self):
        if not self.isDir:
            return 0
        res = self.totalSize if self.totalSize <= 100_000 else 0
        for child in self.childs.values():
            res += child.p1()
        return res

    def p2(self, minSize):
        if self.totalSize < minSize:
            return math.inf
        res = self.totalSize
        for child in self.childs.values():
            res = min(res, child.p2(minSize))
        return res


lines = []
with open("input.txt") as f:
    lines = f.readlines()

root = FileTree("/", None)
current = root
for line in lines:
    if line.startswith("$ cd"):
        nextDir = line[5:].strip()
        if nextDir == "..":
            current = current.parent
        elif nextDir == "/":
            current = root
        else:
            current = current.childs[nextDir]

    elif line.startswith("$ ls"):
        continue

    else:
        size, name = line.strip().split()
        if size == "dir":
            current.addDir(name)
        else:
            size = int(size)
            current.addFile(name, size)


root.calcSize()
# print(root.p1())
print(root.p2(30_000_000 - (70_000_000 - root.totalSize)))
