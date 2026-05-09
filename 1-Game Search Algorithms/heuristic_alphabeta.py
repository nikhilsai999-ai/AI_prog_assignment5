class HeuristicAlphaBeta:
    def __init__(self, game):
        self.game = game

    def search(self, state, depth, alpha, beta, maximizing):
        if depth == 0 or self.game.is_terminal(state):
            return self.game.heuristic(state), None

        best_move = None
        moves = sorted(self.game.get_moves(state), key=lambda m: self.game.estimate(m), reverse=maximizing)

        if maximizing:
            value = float('-inf')
            for move in moves:
                val, _ = self.search(self.game.apply_move(state, move), depth - 1, alpha, beta, False)
                if val > value:
                    value = val
                    best_move = move
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value, best_move
        else:
            value = float('inf')
            for move in moves:
                val, _ = self.search(self.game.apply_move(state, move), depth - 1, alpha, beta, True)
                if val < value:
                    value = val
                    best_move = move
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return value, best_move


if __name__ == "__main__":
    class Game:
        def get_moves(self, state): return state["children"]
        def apply_move(self, state, move): return move
        def is_terminal(self, state): return "value" in state
        def heuristic(self, state): return state["value"]
        def estimate(self, state):
            if "value" in state:
                return state["value"]
            return sum(child["value"] for child in state["children"])

    state = {
        "children": [
            {"children": [{"value": 3}, {"value": 5}, {"value": 6}]},
            {"children": [{"value": 9}, {"value": 1}, {"value": 2}]},
            {"children": [{"value": 0}, {"value": -1}, {"value": 4}]}
        ]
    }

    value, move = HeuristicAlphaBeta(Game()).search(state, 2, float('-inf'), float('inf'), True)

    print("\nHeuristic Alpha-Beta Result:\n")
    print("Best Value:", value)

    for i, child in enumerate(state["children"]):
        if child == move:
            print("Chosen Move: Move", i+1, "→", [c["value"] for c in child["children"]])