import random
import math

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 1},
    'D': {'B': 2},
    'E': {'B': 5, 'F': 3},
    'F': {'C': 1, 'E': 3}
}


class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.total_cost = 0

    def add_child(self, child_state):
        child_node = Node(child_state, self)
        self.children.append(child_node)
        return child_node

    def update(self, cost):
        self.visits += 1
        self.total_cost += cost

    def is_fully_expanded(self):
        return set(graph[self.state].keys()).issubset({child.state for child in self.children})

    def best_child(self, c_param=1.4):
        choices_weights = [
            (child.total_cost / child.visits) + c_param * (2 * math.log(self.visits) / child.visits) ** 0.5
            for child in self.children
        ]
        return self.children[choices_weights.index(max(choices_weights))]


def simulate_path(current_state, goal, visited):
    total_cost = 0
    while current_state != goal:
        next_states = list(set(graph[current_state].keys()) - visited)
        if not next_states:  # Dead end reached, break simulation
            break
        next_state = random.choice(next_states)
        total_cost += graph[current_state][next_state]
        visited.add(next_state)
        current_state = next_state
    return total_cost

def uct_search(start, goal, iterations=1000):
    root = Node(start)

    for _ in range(iterations):
        node = root
        visited = set([start])

        # Selection
        while node.is_fully_expanded() and not node.state == goal:
            node = node.best_child()
            visited.add(node.state)

        # Expansion
        if not node.state == goal:
            next_states = set(graph[node.state].keys()) - visited
            if next_states:
                next_state = random.choice(list(next_states))
                visited.add(next_state)
                node = node.add_child(next_state)

        # Simulation
        total_cost = simulate_path(node.state, goal, visited)

        # Backpropagation
        while node is not None:
            node.update(total_cost)
            total_cost -= graph[node.state][node.parent.state] if node.parent else 0
            node = node.parent

    # Return the path from the root to the best child
    path = []
    node = root.best_child(0)
    while node:
        path.append(node.state)
        node = node.best_child(0) if node.children else None

    return path

# Run MCTS for each agent
start_node_agent1 = 'A'
goal_node_agent1 = 'F'
best_path_agent1 = uct_search(start_node_agent1, goal_node_agent1)

start_node_agent2 = 'B'
goal_node_agent2 = 'E'
best_path_agent2 = uct_search(start_node_agent2, goal_node_agent2)

print("Best path for Agent 1:", best_path_agent1)
print("Best path for Agent 2:", best_path_agent2)