from random import shuffle


class Node:
    def __init__(self, val, neighbors=None):
        self.neighbors = neighbors or []
        self.d = None
        self.f = None
        self.val = val


t = 0
top_sort = []


def dfs(graph):
    for v in graph:
        if v.d is None:
            dfs_visit(v)


def dfs_visit(u: Node):
    global t
    t += 1
    u.d = t
    for v in u.neighbors:
        if v.d is None:
            dfs_visit(v)
    t += 1
    u.f = t
    top_sort.append(u)


briefs = Node("briefs")
pants = Node("pants")
shoes = Node("shoes")
socks = Node("socks")
shirt = Node("shirt")
belt = Node("belt")
tie = Node("tie")
jacket = Node("jacket")
watch = Node("watch")

nodes = [
    briefs,
    pants,
    shoes,
    socks,
    shirt,
    belt,
    tie,
    jacket,
    watch,
]
shuffle(nodes)

briefs.neighbors.extend([pants, shoes])
socks.neighbors.append(shoes)
pants.neighbors.extend([belt, shoes])
shirt.neighbors.extend([belt, tie])
belt.neighbors.append(jacket)
tie.neighbors.append(jacket)


dfs(nodes)

print(*reversed([x.val for x in top_sort]))