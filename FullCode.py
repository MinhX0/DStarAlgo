import heapq

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}
        self.cost = float('inf')
        self.backpointer = None

    def add_neighbor(self, neighbor, edge_cost):
        self.neighbors[neighbor] = edge_cost

def dstar(graph, start_name, goal_name):
    open_list = []
    start = graph[start_name]
    goal = graph[goal_name]
    start.cost = 0

    heapq.heappush(open_list, (start.cost, start))

    while open_list:
        current_cost, current_node = heapq.heappop(open_list)

        if current_node == goal:
            return reconstruct_path(goal)

        for neighbor, edge_cost in current_node.neighbors.items():
            tentative_cost = current_cost + edge_cost

            if tentative_cost < neighbor.cost:
                neighbor.cost = tentative_cost
                neighbor.backpointer = current_node

                heapq.heappush(open_list, (tentative_cost, neighbor))

    return "Không tìm thấy đường đi"

def reconstruct_path(goal):
    path = []
    current = goal

    while current:
        path.insert(0, current.name)
        current = current.backpointer

    return path

def create_graph():
    # Tạo đồ thị mẫu
    graph = {
        'A': Node('A'),
        'B': Node('B'),
        'C': Node('C'),
        'D': Node('D'),
        'E': Node('E'),
        'F': Node('F'),
        'G': Node('G')
    }

    # Thêm các cạnh và chi phí tương ứng
    graph['A'].add_neighbor(graph['B'], 1)
    graph['A'].add_neighbor(graph['C'], 4)
    graph['B'].add_neighbor(graph['D'], 2)
    graph['C'].add_neighbor(graph['D'], 1)
    graph['D'].add_neighbor(graph['E'], 3)
    graph['E'].add_neighbor(graph['F'], 1)
    graph['F'].add_neighbor(graph['G'], 2)

    return graph

if __name__ == "__main__":
    graph = create_graph()
    start = 'A'
    goal = 'G'
    path = dstar(graph, start, goal)
    print("Đường đi ngắn nhất từ {} đến {}: {}".format(start, goal, path))
