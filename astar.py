# import heapq

# def a_star(graph, start, goal, heuristic):
#     open_list = []
#     heapq.heappush(open_list, (0, start))
   
#     g_cost = {node: float('inf') for node in graph}
#     g_cost[start] = 0
   
#     parent = {}
   
#     while open_list:
#         _, current = heapq.heappop(open_list)
       
#         if current == goal:
#             # Reconstruct path
#             path = []
#             while current in parent:
#                 path.append(current)
#                 current = parent[current]
#             path.append(start)
#             path.reverse()
#             return path
       
#         for neighbor, cost in graph[current]:
#             new_g = g_cost[current] + cost
           
#             if new_g < g_cost[neighbor]:
#                 g_cost[neighbor] = new_g
#                 f_cost = new_g + heuristic[neighbor]
#                 heapq.heappush(open_list, (f_cost, neighbor))
#                 parent[neighbor] = current
   
#     return None


import heapq

def a_star(graph, h, start, goal):
    pq = [(0, start)]          
    g = {start: 0}
    parent = {start: None}

    while pq:
        f, node = heapq.heappop(pq)

        if node == goal:
            path = []
            while node:
                path.append(node)
                node = parent[node]
            return path[::-1]

        for neigh, cost in graph[node]:
            new_g = g[node] + cost
            if neigh not in g or new_g < g[neigh]:
                g[neigh] = new_g
                heapq.heappush(pq, (new_g + h[neigh], neigh))
                parent[neigh] = node

    return None


# Example
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

h = {'A':6, 'B':4, 'C':5, 'D':2, 'E':1, 'F':2, 'G':0}

print(a_star(graph, h, 'A', 'G'))