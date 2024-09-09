j1max=int(input("Enter maximum capacity of jug 1: "))
j2max=int(input("Enter maximum capacity of jug 2: "))
jug_goal=input("Enter goal state(separated by space): ")

g1,g2=jug_goal.split()
g1=int(g1)
g2=int(g2)
gstate=(g1,g2)
traversal = input("Enter BFS or DFS: ")
if traversal == "BFS":
    index = 0
else:
    index = -1

visited = []
queue = [(0,0)]
tree={}

while(queue):
    current = queue[index]
    children=[]
    queue.pop(index)
    if current not in visited:
        visited.append(current)
        j1=current[0]
        j2=current[1]

        if((j1<j1max)):
            queue.append((j1max,j2))
            children.append((j1max,j2))

        if((j2<j2max)):
            queue.append((j1,j2max))
            children.append((j1,j2max))
        
        if((j1>0)):
            queue.append((0,j2))
            children.append((0,j2))
        
        if((j2>0)):
            queue.append((j1,0))
            children.append((j1,0))
      
        if((j1+j2)<=j1max and j2>0):
            queue.append((j1+j2,0))
            children.append((j1+j2,0))

        if((j1+j2)<=j2max and j1>0):
            queue.append((0,j1+j2))
            children.append((0,j1+j2))

        if((j1+j2)>j1max and (j2-(j1max-j1)>0 and (current!=(j1max,j2max)))):
            queue.append((j1max,j2-(j1max-j1)))
            children.append((j1max,j2-(j1max-j1)))
        
        if((j1+j2)>j2max and (j1-(j2max-j2)>0 and (current!=(j1max,j2max)))):
            queue.append((j1-(j2max-j2),j2max))
            children.append((j1-(j2max-j2),j2max))

        tree[current]=children
    if(current==gstate):
        break

print("Visited: ",visited) 

goal=visited[-1]
final_path=[goal]
i=-2
while(goal!=(0,0)):
    if goal in tree[visited[i]]:
        final_path.append(visited[i])
        goal = visited[i]
    i-=1

print("Final Path:",final_path[::-1])