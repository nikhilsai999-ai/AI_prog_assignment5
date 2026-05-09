Bayesian Network Implementation using pgmpy – Documentation and README

Introduction
This project demonstrates the implementation of a Bayesian Network using Python and the pgmpy library.

A Bayesian Network is a probabilistic graphical model used in Artificial Intelligence for:

* Decision making
* Reasoning under uncertainty
* Prediction
* Inference
* Risk analysis

Bayesian Networks represent relationships between variables using:

* Nodes
* Directed edges
* Conditional probabilities

This project models a real-world traffic prediction scenario using:

* Rain
* Accident
* Traffic

Objective

The objective of this project is to:

* Understand Bayesian Networks
* Model probabilistic relationships
* Represent problems using directed graphs
* Perform inferencing using probability distributions
* Explore tools used for Bayesian Network modelling

Bayesian Networks

A Bayesian Network is a Directed Acyclic Graph (DAG) where:

* Nodes represent variables
* Edges represent dependencies
* Probabilities define relationships

Bayesian Networks are widely used in:

* Medical diagnosis
* Weather prediction
* Fraud detection
* Traffic analysis
* Robotics
* AI systems

Concepts Used

Probabilistic Reasoning

Bayesian Networks use probability to represent uncertain events.

Example:

* Rain can increase traffic
* Accidents can also increase traffic

Directed Acyclic Graph (DAG)

A DAG is a graph with:

* Directed edges
* No cycles

Example:

Rain ------> Traffic
Accident --> Traffic

Conditional Probability

Conditional Probability defines the probability of an event given another event.

Example:
Probability of Traffic given Rain and Accident.

Inference

Inference means predicting unknown variables using known evidence.

Example:
Finding traffic probability when Rain = True.

Tools Used for Bayesian Networks

The program includes some popular Bayesian Network tools:

pgmpy

* Python library for probabilistic graphical models

BayesiaLab

* Visual Bayesian modelling software

GeNIe

* Bayesian network modelling environment

Netica

* Bayesian belief network software

Hugin

* Decision support and probabilistic reasoning tool

Code Explanation

Import Statements

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

Purpose:
Imports required Bayesian Network libraries.

Libraries Used

pgmpy

* Used for Bayesian Network modelling
* Supports inference and probability computations

VariableElimination

* Performs probabilistic inference

Creating Bayesian Network

model = BayesianNetwork([
('Rain', 'Traffic'),
('Accident', 'Traffic')
])

Purpose:
Creates the Bayesian Network structure.

Relationships:

* Rain affects Traffic
* Accident affects Traffic

Graph Representation

Rain ------> Traffic
Accident --> Traffic

Conditional Probability Distribution (CPD)

CPDs define probabilities for variables.

Rain CPD

cpd_rain = TabularCPD(
variable='Rain',
variable_card=2,
values=[[0.7], [0.3]]
)

Meaning:

* Probability of No Rain = 0.7
* Probability of Rain = 0.3

Accident CPD

cpd_accident = TabularCPD(
variable='Accident',
variable_card=2,
values=[[0.8], [0.2]]
)

Meaning:

* Probability of No Accident = 0.8
* Probability of Accident = 0.2

Traffic CPD

cpd_traffic = TabularCPD(
variable='Traffic',
variable_card=2,
values=[
[0.9, 0.6, 0.5, 0.1],
[0.1, 0.4, 0.5, 0.9]
],
evidence=['Rain', 'Accident'],
evidence_card=[2, 2]
)

Purpose:
Defines Traffic probabilities based on:

* Rain
* Accident

Traffic Probability Table

| Rain | Accident | P(No Traffic) | P(Traffic) |
| ---- | -------- | ------------- | ---------- |
| No   | No       | 0.9           | 0.1        |
| No   | Yes      | 0.6           | 0.4        |
| Yes  | No       | 0.5           | 0.5        |
| Yes  | Yes      | 0.1           | 0.9        |

Adding CPDs to Model

model.add_cpds(cpd_rain, cpd_accident, cpd_traffic)

Purpose:
Adds probability distributions to the network.

Checking Model Validity

model.check_model()

Purpose:
Checks whether:

* Probabilities are valid
* CPDs are correctly defined
* Network structure is correct

Expected Output

Model Validity: True

Bayesian Network Tools

tools = [
"pgmpy",
"BayesiaLab",
"GeNIe",
"Netica",
"Hugin"
]

Purpose:
Displays popular Bayesian Network tools.

Inference Engine

inference = VariableElimination(model)

Purpose:
Creates inference engine for probabilistic queries.

Variable Elimination

Variable Elimination is an inference algorithm used to:

* Compute probabilities efficiently
* Eliminate unnecessary variables

Performing Inference

result = inference.query(
variables=['Traffic'],
evidence={'Rain': 1}
)

Purpose:
Predicts Traffic probability when:
Rain = True

Inference Example

Given:
Rain = Yes

The model calculates:
Probability of Traffic.

Expected Output

Inference Result:

+------------+--------------+
| Traffic    |   phi(Traffic) |
+============+==============+
| Traffic(0) |     0.42      |
+------------+--------------+
| Traffic(1) |     0.58      |
+------------+--------------+

Meaning:
When it is raining:

* Probability of Traffic = 58%
* Probability of No Traffic = 42%

Problem Representation

Problem:
Predict traffic conditions using uncertain events.

Variables:

* Rain
* Accident
* Traffic

Dependencies:

* Rain affects Traffic
* Accident affects Traffic

Reasoning:
Traffic probability changes depending on weather and accidents.

Applications of Bayesian Networks

* Medical diagnosis systems
* Weather prediction
* Fraud detection
* Risk analysis
* Robotics
* Autonomous vehicles
* Traffic management systems

Time Complexity

Inference complexity depends on:

* Number of variables
* Network structure
* Variable dependencies

Approximate Complexity:
Exponential in worst case

Space Complexity

Depends on:

* Number of probability tables
* Variable states
* Graph size

Advantages

* Handles uncertainty effectively
* Supports probabilistic reasoning
* Easy graphical representation
* Useful for prediction systems
* Supports intelligent inference

Limitations

* Large networks become computationally expensive
* Requires accurate probability values
* Complex modelling for huge systems

Test Cases

Test Case 1

Evidence:
Rain = Yes

Expected Result:
Higher probability of Traffic.

Test Case 2

Evidence:
Rain = No
Accident = No

Expected Result:
Low probability of Traffic.

Test Case 3

Evidence:
Rain = Yes
Accident = Yes

Expected Result:
Very high probability of Traffic.

Test Case 4

Evidence:
Accident = Yes

Expected Result:
Traffic probability increases.

Conclusion

This project successfully demonstrates modelling, problem representation, and inferencing using Bayesian Networks in Python.

The system:

* Represents uncertain relationships using probability
* Uses directed graphs for modelling
* Performs intelligent inferencing using evidence
* Demonstrates real-world probabilistic reasoning