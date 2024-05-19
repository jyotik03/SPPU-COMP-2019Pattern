graph={
    'a':['b','c'],
    'b':['d','e'],
    'c':['e'],
    'd':[],
    'e':['f'],
    'f':[],
}
visited=[]
queue=[]

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)

    while queue:
        s=queue.pop(0)
        print(s,end=" ")

        for neighbour in graph [s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
print("Following is Breadth First Search:")
bfs(visited,graph,'a')
print("\n")

visited=set()
def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)

        for neighbour in graph [node]:
            dfs(visited,graph,neighbour)
        
print("Following is Depth First Search:")
dfs(visited,graph,'a')


