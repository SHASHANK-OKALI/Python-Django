graph = {

    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],
    'E':[],
    'F':[],
    'G':[]
}

visited = []

def dfs(node):
    if node not in visited:
       print(node,end=" ")
       visited.append(node)
       for neighbour in graph[node]:
        dfs(neighbour)
print("Following is Depth First Search")
dfs('A')
