Introduction
This project demonstrates the implementation of the Minimax Algorithm, which is commonly used in Artificial Intelligence and Game Theory for decision-making in two-player games.
The algorithm helps an AI agent choose the best possible move by assuming:


The MAX player tries to maximize the score

The MIN player tries to minimize the score

This strategy is widely used in games such as:

Tic Tac Toe
Chess
Checkers
Connect Four


Objective
The objective of this program is to:

Build a simple game tree
Apply the Minimax Algorithm
Find the best possible move for the MAX player
Display the game tree and chosen move


Concepts Used
Minimax Algorithm
The Minimax algorithm works recursively.
MAX Player
Chooses the move with the highest value.
MIN Player
Chooses the move with the lowest value.
The algorithm continues until:
A terminal node is reached OR the search depth becomes 0

Code Explanation
Class: Minimax
class Minimax:
This class contains the Minimax search logic.
Constructor
def __init__(self, game):    self.game = game
Purpose:
Initializes the game object.
Parameters:

game → Object containing game functions

Search Function
def search(self, state, depth, maximizing):
This is the main recursive Minimax function.
Parameters:
state → Current game state
depth → Maximum search depth
maximizing → True for MAX player, False for MIN player

Terminal Condition
if depth == 0 or self.game.is_terminal(state):    return self.game.evaluate(state), None
Meaning:
Stop recursion if:
Depth becomes 0
OR terminal node is reached

Then return:
Evaluation score
No move (None)

Maximizing Player Logic
if maximizing:
The MAX player tries to find the largest value.
Initialization
max_eval = float('-inf')
Starts with negative infinity.
Loop Through Moves
for move in self.game.get_moves(state):
Checks all possible moves.
Recursive Call
val, _ = self.search(...)
Explores child nodes recursively.
Update Best Value
if val > max_eval:
If a better value is found:
Update maximum value
Store best move

Minimizing Player Logic
else:
The MIN player tries to find the smallest value.
Initialization
min_eval = float('inf')
Starts with positive infinity.
Recursive Exploration
The process is similar to MAX player but chooses minimum values.
Game Class
class Game:
This is a simple game implementation used for testing.
Functions
Get Moves
def get_moves(self, state):    return state["children"]
Returns all possible child states.
Apply Move
def apply_move(self, state, move):    return move
Moves to the next state.
Check Terminal State
def is_terminal(self, state):    return "value" in state
If node contains "value", it is a terminal node.
Evaluate State
def evaluate(self, state):    return state["value"]
Returns evaluation score.
Game Tree Structure
state = {    "children": [        {"children": [{"value": 3}, {"value": 5}, {"value": 6}]},        {"children": [{"value": 9}, {"value": 1}, {"value": 2}]},        {"children": [{"value": 0}, {"value": -1}, {"value": 4}]}    ]}
Tree Representation
                MAX        /        |        \      MIN       MIN       MIN    /  |  \   /  |  \   /  |  \   3   5   6  9   1   2  0  -1  4
Minimax Calculation
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
Therefore:
Best value = 3
Best move = First branch

Expected Output
Game Tree (Minimax):                MAX        /        |        \      MIN       MIN       MIN    /  |  \   /  |  \   /  |  \    3  5  6    9  1  2    0  -1  4     ↓         ↓         ↓      3   1   -1MAX( 3, 1, -1 ) = 3Best Value: 3Chosen Move: Move 1 → [3, 5, 6]
Time Complexity
O(bd)O(b^d)O(bd)
Where:
b = Branching factor
d = Depth of tree


Space Complexity
O(d)O(d)O(d)
Because recursion stores one path at a time.
Test Cases
Test Case 1
Input Tree
[    [3,5,6],    [9,1,2],    [0,-1,4]]
Expected Output
Best Value = 3Chosen Move = [3,5,6]
Test Case 2
Modified Tree
state = {    "children": [        {"children": [{"value": 8}, {"value": 7}]},        {"children": [{"value": 2}, {"value": 5}]}    ]}
Calculation
min(8,7) = 7
min(2,5) = 2

MAX chooses:
max(7,2) = 7

Expected Output
Best Value = 7Chosen Move = [8,7]
Test Case 3
Modified Tree
state = {    "children": [        {"children": [{"value": -5}, {"value": -2}]},        {"children": [{"value": -1}, {"value": -9}]}    ]}
Calculation

min(-5,-2) = -5
min(-1,-9) = -9

MAX chooses:
max(-5,-9) = -5

Expected Output
Best Value = -5Chosen Move = [-5,-2]