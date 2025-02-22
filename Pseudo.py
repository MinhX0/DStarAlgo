function DStar(graph, start, goal):
    initialize openList as a priority queue
    initialize cost[start] to 0
    initialize cost[all other nodes] to infinity
    initialize backpointer[all nodes] to null

    add start to openList with priority 0

    while openList is not empty:
        current = node in openList with lowest cost

        if current == goal:
            return reconstructPath(backpointer, goal)

        remove current from openList

        for each neighbor of current:
            tentativeCost = cost[current] + edgeCost(current, neighbor)

            if tentativeCost < cost[neighbor]:
                cost[neighbor] = tentativeCost
                backpointer[neighbor] = current
                if neighbor is not in openList:
                    add neighbor to openList with priority tentativeCost
                else:
                    update priority of neighbor in openList to tentativeCost

    return "No path found"

function reconstructPath(backpointer, goal):
    path = []
    current = goal
    while current is not null:
        insert current at the beginning of path
        current = backpointer[current]
    return path
