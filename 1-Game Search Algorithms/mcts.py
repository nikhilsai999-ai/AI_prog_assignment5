import random, math

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.wins = 0

class MCTS:
    def __init__(self, game, iterations=300):
        self.game = game
        self.iterations = iterations

    def ucb1(self, node):
        if node.visits == 0:
            return float('inf')
        return node.wins / node.visits + math.sqrt(2 * math.log(node.parent.visits) / node.visits)

    def select(self, node):
        while node.children:
            node = max(node.children, key=self.ucb1)
        return node

    def expand(self, node):
        if self.game.is_terminal(node.state):
            return node
        for move in self.game.get_moves(node.state):
            node.children.append(Node(move, node))
        return random.choice(node.children)

    def simulate(self, state):
        while not self.game.is_terminal(state):
            state = random.choice(self.game.get_moves(state))
        return state["value"]

    def backpropagate(self, node, result):
        while node:
            node.visits += 1
            node.wins += result
            node = node.parent

    def search(self, state):
        root = Node(state)
        for _ in range(self.iterations):
            node = self.select(root)
            node = self.expand(node)
            result = self.simulate(node.state)
            self.backpropagate(node, result)
        return max(root.children, key=lambda n: n.visits).state


if __name__ == "__main__":
    class Game:
        def get_moves(self, state): return state["children"]
        def is_terminal(self, state): return "value" in state

    state = {
        "children": [
            {"children": [{"value": 3}, {"value": 5}, {"value": 6}]},
            {"children": [{"value": 9}, {"value": 1}, {"value": 2}]},
            {"children": [{"value": 0}, {"value": -1}, {"value": 4}]}
        ]
    }

    result = MCTS(Game(), 300).search(state)

    print("\nMCTS Result:\n")
    for i, child in enumerate(state["children"]):
        if child == result:
            print("Chosen Move: Move", i+1)