def dfs(tree,start,target,visited,path):

    if start not in visited:
        visited.append(start)
        path.append(start)

    if start==target:
        print("Traversing order:",visited)
        print("Final path:",path)
        return True
      
    for i in tree[start]:
        if i not in visited:
            if dfs(tree,i,target,visited,path):
                return True
    path.pop()
    return False
     
n=int(input("Enter number of nodes: "))
tree={}
for i in range(n):
        node=input("Enter node:")
        child=[]
        nc=int(input("Enter number of children: "))
        for i in range(nc):
            c=input("Enter child:")
            child.append(c)
        tree[node]=child
print("Input tree:",tree)
target=input("Enter the goal node: ")
start=input("Enter the source node: ")
visited=[]
path=[]
result=dfs(tree,start,target,visited,path)

if result:
    print("Node found")
else:
    print("Not found")
