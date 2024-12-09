# adj=[[2,3,1], [0], [0,4], [0], [2]]    #this is the adjacency list
adj=[[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
result=[] #return traversal of the graph
visited=[0]*len(adj)

def dfs(node):
    visited[node]=1
    result.append(node)
    
    for i in adj[node]:
        if visited[i]!=1:
            dfs(i)
    return result

print(dfs(0))
    