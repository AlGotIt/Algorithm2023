class Node:
    def __init__(self, a) -> None:
        self.name = a
        self.next = None

    def set_next(self, node):
        self.next = node

    def get_next(self):
        return self.next

def find(l, p):
    node = l
    names = []
    while True:
        if node.name not in names:
            if node.name == p:
                return "T"
            names.append(node.name)
            if node.next == None: break
            node = node.next
        else:
            break
    return "F"

def find_tail(node):
    c = node
    names = []
    while c.next != None:
        if c.next.name in names : break
        names.append(c.name)
        c = c.next
    return c

n = int(input())
nodes = []
heads = []

for _ in range(n):
    now, next = input().split(' is ')
    now_node = Node(now)
    next_node = Node(next)
    
    if now not in heads:
        nodes.append(now_node)
        heads.append(now)

    if next not in heads:
        nodes.append(next_node)
        heads.append(next)
    else:
        next_node = nodes[heads.index(next)]
        
    for l in nodes:
        tail = find_tail(l)
        if tail.name == now_node.name:
            tail.set_next(next_node)




m = int(input())
for _ in range(m):
    p, q = input().split(' is ')
    if p not in heads: 
        print("F")
        continue
    result = find(nodes[heads.index(p)], q)
    print(result)
