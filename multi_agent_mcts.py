graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 1},
    'D': {'B': 2},
    'E': {'B': 5, 'F': 3},
    'F': {'C': 1, 'E': 3}
}

# Define support nodes where agents can assist each other
support_nodes = {'D', 'E'}  # Example nodes where support can be provided

class MultiAgentNode:
    def __init__(self, agent_states, parent=None):
        self.agent_states = agent_states  # A dictionary of agent positions
        self.parent = parent
        self.children = []
        self.visits = 0
        self.total_cost = 0

    def add_child(self, child_agent_states):
        child_node = MultiAgentNode(child_agent_states, self)
        self.children.append(child_node)
        return child_node

    def update(self, cost):
        self.visits += 1
        self.total_cost += cost

    def is_fully_expanded(self):
        # Define expansion logic for multiple agents
        # ...

        pass

    def best_child(self, c_param=1.4):
        # Define best child selection logic for multiple agents
        # ...
        pass

def simulate_multi_agent_path(current_agent_states, goal_states, visited):
    # Adapt to handle multiple agents
    # ...
    pass

def uct_search_multi_agent(start_states, goal_states, iterations=1000):
    root = MultiAgentNode(start_states)

    for _ in range(iterations):
        node = root
        visited = {agent: set([start_states[agent]]) for agent in start_states}

        # Adapt selection, expansion, simulation, and backpropagation for multiple agents
        # ...

    # Construct and return the best path for each agent
    # ...
    pass

# Example usage
start_states = {'Agent1': 'A', 'Agent2': 'B'}
goal_states = {'Agent1': 'F', 'Agent2': 'E'}
best_paths = uct_search_multi_agent(start_states, goal_states)
print("Best paths for multiple agents:", best_paths)
