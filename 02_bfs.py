def bfs(tree, start, target):
    queue = [start]
    visited = [start]
    while queue:
        current = queue.pop(0)  # pop the first element
        print(f"Visited node {current}")

        if current == target:
            return True

        if current not in tree:
            pass
        
        for i in tree[current]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
    return False

n = int(input("Enter number of nodes: "))
tree = {}
for _ in range(n):
    node = input("Enter node: ")
    child = []
    nc = int(input("Enter number of children: "))
    for _ in range(nc):
        c = input("Enter child: ")
        child.append(c)
    tree[node] = child
print("Input tree:", tree)
target = input("Enter the target: ")
start = input("Enter the start node: ")
result = bfs(tree, start, target)
if result:
    path = []
    path.append(target)
    while path[-1] != start:
        for key in tree:
            if path[-1] in tree[key]:
                path.append(key)
    print("Final path:", path[::-1])
    print("Node found")
else:
    print("Not found")
