Monte Carlo Tree Search (MCTS) – Documentation and README


Introduction

This document demonstrates the implementation of the Monte Carlo Tree Search (MCTS) Algorithm, a powerful Artificial Intelligence search technique used in decision-making and game-playing systems.

MCTS is widely used in:

* Chess engines
* Go AI
* Game AI systems
* Robotics
* Strategic planning systems

Unlike Minimax, MCTS does not explore the entire game tree. Instead, it:

* Randomly simulates games
* Learns from outcomes
* Selects moves based on statistical success

Objective

The objective of this program is to:

* Implement Monte Carlo Tree Search
* Simulate random game outcomes
* Use statistical analysis to choose the best move
* Demonstrate AI decision-making using simulations

Concepts Used

Monte Carlo Tree Search

MCTS works in four major steps:

* Selection
* Expansion
* Simulation
* Backpropagation

The algorithm repeatedly performs these steps to improve decision-making.

Node

Each node represents a game state.

Each node stores:

* State information
* Parent node
* Child nodes
* Visit count
* Win score

UCB1 Formula

The algorithm uses the UCB1 formula to balance:

* Exploration of new moves
* Exploitation of successful moves

Formula:

UCB1 = (wins / visits) + sqrt(2 * log(parent visits) / visits)

Code Explanation

Class: Node

class Node:

This class represents a node in the search tree.

Constructor

def **init**(self, state, parent=None):

Purpose:
Initializes a node.

Variables:

* state → Current game state
* parent → Parent node
* children → List of child nodes
* visits → Number of visits
* wins → Total win score

Class: MCTS

class MCTS:

This class contains the Monte Carlo Tree Search logic.

Constructor

def **init**(self, game, iterations=300):

Purpose:
Initializes the game and number of iterations.

Parameters:

* game → Game object
* iterations → Number of simulations

UCB1 Function

def ucb1(self, node):

Purpose:
Calculates the UCB1 score for node selection.

Logic:

* If node has not been visited, return infinity
* Otherwise calculate exploration-exploitation score

Formula Used

UCB1 = (wins / visits) + sqrt(2 * log(parent visits) / visits)

Selection Phase

def select(self, node):

Purpose:
Selects the best node using UCB1 values.

Logic:

* Repeatedly choose child with highest UCB1 score
* Continue until leaf node is reached

Expansion Phase

def expand(self, node):

Purpose:
Adds child nodes to the selected node.

Logic:

* If node is terminal, return it
* Otherwise generate all possible moves
* Add child nodes
* Randomly choose one child

Simulation Phase

def simulate(self, state):

Purpose:
Performs random play until terminal state is reached.

Logic:

* Randomly choose moves
* Continue until game ends
* Return final state value

Backpropagation Phase

def backpropagate(self, node, result):

Purpose:
Updates statistics after simulation.

Logic:

* Increase visit count
* Add simulation result to wins
* Move upward to parent nodes

Search Function

def search(self, state):

Purpose:
Main MCTS function.

Steps:

* Create root node
* Run multiple iterations
* Perform selection, expansion, simulation, and backpropagation
* Return child with highest visits

Game Class

class Game:

This is a simple game implementation used for testing.

Functions

Get Moves

def get_moves(self, state):
return state["children"]

Returns all possible child states.

Check Terminal State

def is_terminal(self, state):
return "value" in state

If node contains "value", it is a terminal node.

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
            ROOT
    /          |          \
  Move1      Move2       Move3
/   |   \   /   |   \   /   |   \
```

3    5    6 9    1    2 0   -1   4

Working of MCTS

Selection

* Choose best node using UCB1

Expansion

* Add unexplored child nodes

Simulation

* Play random moves until terminal state

Backpropagation

* Update node statistics

This process repeats for many iterations.

Expected Output

MCTS Result:

Chosen Move: Move 1

The chosen move may vary slightly because MCTS uses randomness during simulations.

Time Complexity

Time Complexity depends on:

* Number of iterations
* Branching factor
* Simulation depth

Approximate Complexity:
O(iterations × simulation depth)

Space Complexity

O(number of nodes)

Because nodes are stored in the search tree.

Advantages

* Efficient for very large game trees
* Does not require exploring entire tree
* Learns from simulations
* Works well for uncertain environments

Limitations

* Results may vary because of randomness
* Requires many iterations for accuracy
* Can be slower for simple games

Test Cases

Test Case 1

Input Tree

[
[3,5,6],
[9,1,2],
[0,-1,4]
]

Possible Output

Chosen Move: Move 1

Test Case 2

Modified Tree

state = {
"children": [
{"children": [{"value": 8}, {"value": 7}]},
{"children": [{"value": 2}, {"value": 5}]}
]
}

Possible Output

Chosen Move: Move 1

Because higher simulation rewards are expected from first branch.

Test Case 3

Modified Tree

state = {
"children": [
{"children": [{"value": -5}, {"value": -2}]},
{"children": [{"value": -1}, {"value": -9}]}
]
}

Possible Output

Chosen Move: Move 2

Because simulations may favor higher values statistically.