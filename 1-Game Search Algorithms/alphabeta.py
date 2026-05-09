class AlphaBeta:
    def __init__(self, game):
        self.game = game
        self.pruned = []

    def search(self, state, depth, alpha, beta, maximizing):
        if depth == 0 or self.game.is_terminal(state):
            return self.game.evaluate(state), None

        best_move = None

        if maximizing:
            value = float('-inf')
            for move in self.game.get_moves(state):
                val, _ = self.search(self.game.apply_move(state, move), depth - 1, alpha, beta, False)
                if val > value:
                    value = val
                    best_move = move
                alpha = max(alpha, value)
                if alpha >= beta:
                    self.pruned.append(move)
                    break
            return value, best_move
        else:
            value = float('inf')
            for move in self.game.get_moves(state):
                val, _ = self.search(self.game.apply_move(state, move), depth - 1, alpha, beta, True)
                if val < value:
                    value = val
                    best_move = move
                beta = min(beta, value)
                if alpha >= beta:
                    self.pruned.append(move)
                    break
            return value, best_move


if __name__ == "__main__":
    class Game:
        def get_moves(self, state): return state["children"]
        def apply_move(self, state, move): return move
        def is_terminal(self, state): return "value" in state
        def evaluate(self, state): return state["value"]

    state = {
        "children": [
            {"children": [{"value": 3}, {"value": 5}, {"value": 6}]},
            {"children": [{"value": 9}, {"value": 1}, {"value": 2}]},
            {"children": [{"value": 0}, {"value": -1}, {"value": 4}]}
        ]
    }

    solver = AlphaBeta(Game())
    value, move = solver.search(state, 2, float('-inf'), float('inf'), True)

    print("\nGame Tree (Alpha-Beta with Pruning):\n")
    print("                MAX")
    print("        /        |        \\")
    print("      MIN       MIN       MIN")
    print("    /  |  \\   /  |  \\   /  |  \\")
    
    min_vals = []
    for child in state["children"]:
        vals = [c["value"] for c in child["children"]]
        print("   ", "  ".join(map(str, vals)), end="")
        min_vals.append(min(vals))
    print("\n")

    print("     ↓         ↓         ↓")
    print("     ", "   ".join(map(str, min_vals)))
    print("\nMAX(", ", ".join(map(str, min_vals)), ") =", max(min_vals))

    print("\nPruned Branches:", len(solver.pruned))

    for i, child in enumerate(state["children"]):
        if child == move:
            print("\nBest Value:", value)
            print("Chosen Move: Move", i+1, "→", [c["value"] for c in child["children"]])