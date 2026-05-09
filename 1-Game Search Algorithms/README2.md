Alpha-Beta Pruning Algorithm – Documentation and README

Introduction

This document demonstrates the implementation of the Alpha-Beta Pruning Algorithm, an optimized version of the Minimax Algorithm used in Artificial Intelligence and Game Theory for decision-making in two-player games.

Alpha-Beta Pruning improves the efficiency of Minimax by eliminating branches that do not affect the final decision.

The algorithm assumes:

* The MAX player tries to maximize the score
* The MIN player tries to minimize the score

Applications include:

* Chess AI
* Tic Tac Toe
* Checkers
* Connect Four
* Strategic decision-making systems

Objective

The objective of this program is to:

* Implement the Alpha-Beta Pruning Algorithm
* Optimize Minimax search using pruning
* Reduce unnecessary node exploration
* Find the best possible move for the MAX player
* Display the game tree and pruned branches

Concepts Used

Alpha-Beta Pruning

Alpha-Beta Pruning is an optimization technique for the Minimax Algorithm.

It reduces the number of nodes evaluated in the game tree.

Two important values are used:

Alpha (α)

* Best value currently guaranteed for MAX player

Beta (β)

* Best value currently guaranteed for MIN player

Pruning occurs when:
alpha >= beta

This means further exploration of that branch is unnecessary.

Code Explanation

Class: AlphaBeta

class AlphaBeta:

This class contains the Alpha-Beta Pruning logic.

Constructor

def **init**(self, game):
self.game = game
self.pruned = []

Purpose:

* Initializes the game object
* Stores pruned branches in a list

Parameters:

* game → Object containing game functions

Search Function

def search(self, state, depth, alpha, beta, maximizing):

This is the main recursive Alpha-Beta search function.

Parameters:

* state → Current game state
* depth → Maximum search depth
* alpha → Best value for MAX player
* beta → Best value for MIN player
* maximizing → True for MAX player, False for MIN player

Terminal Condition

if depth == 0 or self.game.is_terminal(state):
return self.game.evaluate(state), None

Meaning:
Stop recursion if:

* Depth becomes 0
* OR terminal node is reached

Then return:

* Evaluation score
* No move (None)

Maximizing Player Logic

if maximizing:

The MAX player tries to maximize the score.

Initialization

value = float('-inf')

Starts with negative infinity.

Loop Through Moves

for move in self.game.get_moves(state):

Checks all possible moves.

Recursive Call

val, _ = self.search(...)

Explores child nodes recursively.

Update Best Value

if val > value:

If a better value is found:

* Update maximum value
* Store best move

Update Alpha

alpha = max(alpha, value)

Updates alpha value for MAX player.

Pruning Condition

if alpha >= beta:

If alpha becomes greater than or equal to beta:

* Remaining branches are pruned
* Exploration stops

Pruned branch is stored using:

self.pruned.append(move)

Minimizing Player Logic

else:

The MIN player tries to minimize the score.

Initialization

value = float('inf')

Starts with positive infinity.

Update Beta

beta = min(beta, value)

Updates beta value for MIN player.

Pruning occurs similarly when:
alpha >= beta

Game Class

class Game:

This is a simple game implementation used for testing.

Functions

Get Moves

def get_moves(self, state):
return state["children"]

Returns all possible child states.

Apply Move

def apply_move(self, state, move):
return move

Moves to the next state.

Check Terminal State

def is_terminal(self, state):
return "value" in state

If node contains "value", it is a terminal node.

Evaluate State

def evaluate(self, state):
return state["value"]

Returns evaluation score.

Game Tree Structure

state = {
"children": [
{"children": [{"value": 3}, {"value": 5}, {"value": 6}]},
{"children": [{"value": 9}, {"value": 1}, {"value": 2}]},
{"children": [{"value": 0}, {"value": -1}, {"value": 4}]}
]
}

Tree Representation

```
            MAX
    /        |        \
  MIN       MIN       MIN
/  |  \   /  |  \   /  |  \
```

3   5   6  9   1   2  0  -1  4

Alpha-Beta Calculation

Step 1 – MIN Nodes Choose Minimum

Branch 1:
Values = 3, 5, 6
MIN chooses = 3

Branch 2:
Values = 9, 1, 2
MIN chooses = 1

Branch 3:
Values = 0, -1, 4
MIN chooses = -1

So MIN layer becomes:
3, 1, -1

Step 2 – MAX Chooses Maximum

MAX(3, 1, -1) = 3

Best value = 3

Pruning Explanation

During traversal, some branches are skipped because they cannot improve the final result.

Condition for pruning:
alpha >= beta

This reduces unnecessary computations and improves performance.

Expected Output

Game Tree (Alpha-Beta with Pruning):

```
            MAX
    /        |        \
  MIN       MIN       MIN
/  |  \   /  |  \   /  |  \
3  5  6    9  1  2    0  -1  4

 ↓         ↓         ↓
  3   1   -1
```

MAX( 3, 1, -1 ) = 3

Pruned Branches: 1

Best Value: 3
Chosen Move: Move 1 → [3, 5, 6]

Time Complexity

Best Case:
O(b^(d/2))

Worst Case:
O(b^d)

Where:

* b = Branching factor
* d = Depth of tree

Space Complexity

O(d)

Because recursion stores one path at a time.

Test Cases

Test Case 1

Input Tree

[
[3,5,6],
[9,1,2],
[0,-1,4]
]

Expected Output

Best Value = 3
Chosen Move = [3,5,6]
Pruned Branches = 1

Test Case 2

Modified Tree

state = {
"children": [
{"children": [{"value": 8}, {"value": 7}]},
{"children": [{"value": 2}, {"value": 5}]}
]
}

Calculation

* min(8,7) = 7
* min(2,5) = 2

MAX chooses:

* max(7,2) = 7

Expected Output

Best Value = 7
Chosen Move = [8,7]

Test Case 3

Modified Tree

state = {
"children": [
{"children": [{"value": -5}, {"value": -2}]},
{"children": [{"value": -1}, {"value": -9}]}
]
}

Calculation

* min(-5,-2) = -5
* min(-1,-9) = -9

MAX chooses:

* max(-5,-9) = -5

Expected Output

Best Value = -5
Chosen Move = [-5,-2]