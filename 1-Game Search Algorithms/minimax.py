class Minimax:
    def __init__(self, game):
        self.game = game

    def search(self, state, depth, maximizing):
        if depth == 0 or self.game.is_terminal(state):
            return self.game.evaluate(state), None

        best_move = None

        if maximizing:
            max_eval = float('-inf')
            for move in self.game.get_moves(state):
                val, _ = self.search(self.game.apply_move(state, move), depth - 1, False)
                if val > max_eval:
                    max_eval = val
                    best_move = move
            return max_eval, best_move
        else:
            min_eval = float('inf')
            for move in self.game.get_moves(state):
                val, _ = self.search(self.game.apply_move(state, move), depth - 1, True)
                if val < min_eval:
                    min_eval = val
                    best_move = move
            return min_eval, best_move


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

    value, move = Minimax(Game()).search(state, 2, True)

    print("\nGame Tree (Minimax):\n")
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

    for i, child in enumerate(state["children"]):
        if child == move:
            print("\nBest Value:", value)
            print("Chosen Move: Move", i+1, "→", [c["value"] for c in child["children"]])