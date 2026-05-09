Heuristic Alpha-Beta Pruning – Documentation and README

Introduction
This document demonstrates the implementation of the Heuristic Alpha-Beta Pruning Algorithm, an advanced optimization of the Minimax Algorithm used in Artificial Intelligence and Game Theory.

The algorithm improves search efficiency by:

* Using Alpha-Beta pruning to eliminate unnecessary branches
* Using heuristic evaluation and move ordering to explore promising moves first

This approach is commonly used in:

* Chess engines
* Game AI systems
* Strategic planning applications
* Decision-making systems

Objective

The objective of this program is to:

* Implement Heuristic Alpha-Beta Pruning
* Optimize Minimax search using pruning and heuristics
* Reduce unnecessary node exploration
* Find the best possible move efficiently
* Demonstrate move ordering using heuristic estimates

Concepts Used

Heuristic Function

A heuristic function estimates how good a game state is without exploring the entire tree.

In this program:

* Terminal states return their actual value
* Non-terminal states are estimated using child node values

Alpha-Beta Pruning

Alpha-Beta Pruning eliminates branches that cannot affect the final decision.

Two important values are used:

Alpha (α)

* Best value guaranteed for MAX player

Beta (β)

* Best value guaranteed for MIN player

Pruning occurs when:
alpha >= beta

Move Ordering

Moves are sorted before exploration using heuristic estimates.

Better moves are explored first to increase pruning efficiency.

Code Explanation

Class: HeuristicAlphaBeta

class HeuristicAlphaBeta:

This class contains the Heuristic Alpha-Beta search logic.

Constructor

def **init**(self, game):
self.game = game

Purpose:
Initializes the game object.

Parameters:

* game → Object containing game functions

Search Function

def search(self, state, depth, alpha, beta, maximizing):

This is the main recursive search function.

Parameters:

* state → Current game state
* depth → Maximum search depth
* alpha → Best value for MAX player
* beta → Best value for MIN player
* maximizing → True for MAX player, False for MIN player

Terminal Condition

if depth == 0 or self.game.is_terminal(state):
return self.game.heuristic(state), None

Meaning:
Stop recursion if:

* Depth becomes 0
* OR terminal node is reached

Then return:

* Heuristic evaluation score
* No move (None)

Move Ordering

moves = sorted(self.game.get_moves(state), key=lambda m: self.game.estimate(m), reverse=maximizing)

Purpose:

* Sorts moves using heuristic estimates
* Best moves are explored first

If maximizing is True:

* Moves are sorted in descending order

If maximizing is False:

* Moves are sorted in ascending order

Maximizing Player Logic

if maximizing:

The MAX player tries to maximize the score.

Initialization

value = float('-inf')

Starts with negative infinity.

Loop Through Moves

for move in moves:

Checks all ordered moves.

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

Updates alpha value.

Pruning Condition

if alpha >= beta:
break

Stops exploring unnecessary branches.

Minimizing Player Logic

else:

The MIN player tries to minimize the score.

Initialization

value = float('inf')

Starts with positive infinity.

Update Beta

beta = min(beta, value)

Updates beta value.

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

Heuristic Function

def heuristic(self, state):
return state["value"]

Returns heuristic evaluation score.

Estimate Function

def estimate(self, state):
if "value" in state:
return state["value"]
return sum(child["value"] for child in state["children"])

Purpose:

* Estimates the quality of a move
* Used for move ordering

For non-terminal states:

* Returns the sum of child node values

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

Heuristic Evaluation

Branch 1:
3 + 5 + 6 = 14

Branch 2:
9 + 1 + 2 = 12

Branch 3:
0 + (-1) + 4 = 3

Moves are explored in order of estimated strength.

Minimax Calculation

Step 1 – MIN Nodes Choose Minimum

Branch 1:
min(3,5,6) = 3

Branch 2:
min(9,1,2) = 1

Branch 3:
min(0,-1,4) = -1

Step 2 – MAX Chooses Maximum

MAX(3,1,-1) = 3

Best value = 3

Expected Output

Heuristic Alpha-Beta Result:

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

Advantages

* Faster than standard Minimax
* More efficient than normal Alpha-Beta pruning
* Uses move ordering for better pruning
* Reduces unnecessary computation

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