import numpy as np


with open("input.txt") as f:
    lines = f.read().strip().split("\n")
    lines = list(map(lambda x: x.split(), lines))
    lines = [(a,int(b)) for a,b in lines]

direction = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}

def addpos(p1, p2):
    return (p1[0]+p2[0], p1[1]+p2[1])


def move(mypos, target):
    if mypos[0] >= target[0] + 2:
        if mypos[1] > target[1]:
            return (mypos[0]-1, mypos[1]-1)
        elif mypos[1] < target[1]:
            return (mypos[0]-1, mypos[1]+1)
        else:
            return (mypos[0]-1, mypos[1])
    
    if mypos[0] <= target[0] - 2:
        if mypos[1] > target[1]:
            return (mypos[0]+1, mypos[1]-1)
        elif mypos[1] < target[1]:
            return (mypos[0]+1, mypos[1]+1)
        else:
            return (mypos[0]+1, mypos[1])
    
    if mypos[1] >= target[1] + 2:
        if mypos[0] > target[0]:
            return (mypos[0]-1, mypos[1]-1)
        elif mypos[0] < target[0]:
            return (mypos[0]+1, mypos[1]-1)
        else:
            return (mypos[0], mypos[1]-1)
    
    if mypos[1] <= target[1] - 2:
        if mypos[0] > target[0]:
            return (mypos[0]-1, mypos[1]+1)
        elif mypos[0] < target[0]:
            return (mypos[0]+1, mypos[1]+1)
        else:
            return (mypos[0], mypos[1]+1)
    
    return mypos
    



def p1():
    width = 4
    height = 4
    start = (1, 1)
    head = start
    tail = start
    plan = np.zeros((height, width), dtype=bool)
    plan[tail] = True
    
    for d, nb in lines:
        for _ in range(nb):
            
            # Resize if needed
            if head[0] == 0:
                plan = np.append(np.zeros((height, width), dtype=bool), plan, axis=0)
                head = (head[0]+height, head[1])
                tail= (tail[0]+height, tail[1])
                start = (start[0]+height, start[1])
                height *= 2
            
            if head[0] == height - 1:
                plan = np.append(plan, np.zeros((height, width), dtype=bool), axis=0)
                height *= 2
            
            if head[1] == 0:
                plan = np.append(np.zeros((height, width), dtype=bool), plan, axis=1)
                head = (head[0], head[1]+width)
                tail= (tail[0], tail[1]+width)
                start = (start[0], start[1]+width)
                width *= 2
            
            if head[1] == width - 1:
                plan = np.append(plan, np.zeros((height, width), dtype=bool), axis=1)
                width *= 2
            
            # cases where you drag the tail
            if d == "U" and tail[0] > head[0]:
                tail = head

            if d == "D" and tail[0] < head[0]:
                tail = head
            
            if d == "L" and tail[1] > head[1]:
                tail = head
            
            if d == "R" and tail[1] < head[1]:
                tail = head
            
            # Update head pos and the plan
            head = addpos(head, direction[d])
            plan[tail] = True
    
    #print(plan)
    print(np.count_nonzero(plan))
             
 
def p2():
    width = 4
    height = 4
    start = (1, 1)
    rope = [start] * 10
    plan = np.zeros((height, width), dtype=bool)
    plan[start] = True
    
    for d, nb in lines:
        for _ in range(nb):
            
            # Resize if needed
            if rope[0][0] == 0:
                plan = np.append(np.zeros((height, width), dtype=bool), plan, axis=0)
                for i in range(10):
                    rope[i] = (rope[i][0]+height, rope[i][1])
                start = (start[0]+height, start[1])
                height *= 2
            
            if rope[0][0] == height - 1:
                plan = np.append(plan, np.zeros((height, width), dtype=bool), axis=0)
                height *= 2
            
            if rope[0][1] == 0:
                plan = np.append(np.zeros((height, width), dtype=bool), plan, axis=1)
                for i in range(10):
                    rope[i] = (rope[i][0], rope[i][1]+width)
                start = (start[0], start[1]+width)
                width *= 2
            
            if rope[0][1] == width - 1:
                plan = np.append(plan, np.zeros((height, width), dtype=bool), axis=1)
                width *= 2
            
            # Update head pos
            rope[0] = addpos(rope[0], direction[d])

            # Move the rope
            for i in range(1,10):
                rope[i] = move(rope[i], rope[i-1])

            # Update plan
            plan[rope[-1]] = True
    
    #print(plan)
    print(np.count_nonzero(plan))

p2()
