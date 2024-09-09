nodecost={'A':16,'B':4,'C':16,'D':2,'E':1,'F':4,'G':0}
graph={'A':{'B':10,'C':4},'B':{'A':10,'C':4,'D':6},'C':{'A':4,'B':4,'E':6},'D':{'B':6,'E':6,'F':4},'E':{'C':6,'D':6,'G':14},'F':{'D':4,'G':4},'G':{'E':14,'F':4}}
target=input("Enter the goal node:")
start=input("Enter the start node:")
close={}
open={}
path={}
close[start]=nodecost[start]
path[start]=[start]
while start!=target:
    for i in graph[start]:
        if i not in close:
            if i in open:
                if open[i]>close[start]-nodecost[start]+graph[start][i]+nodecost[i]:
                    open[i]=close[start]-nodecost[start]+graph[start][i]+nodecost[i]
                    path[i]=path[start]+[i]
            else:
                open[i]=close[start]-nodecost[start]+graph[start][i]+nodecost[i]
                path[i]=path[start]+[i]
        else:
            if close[i]>close[start]-nodecost[start]+graph[start][i]+nodecost[i]:
                open[i]=close[start]-nodecost[start]+graph[start][i]+nodecost[i]
                path[i]=path[start]+[i]
                close.pop(i)
    start=min(open,key=open.get)
    close[start]=open[start]
    open.pop(start)
print("Path:"+str(path[target]) + "\nCost:"+str(close[target]))
