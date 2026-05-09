Knowledge-Based AI Travel Planner – Documentation and README

Introduction
This project demonstrates the implementation of a Knowledge-Based AI Travel Planner using Python.

The system recommends travel destinations based on:
* User travel intent
* Budget preference
* Food preference

The project uses concepts from:
* Artificial Intelligence
* Knowledge Representation
* Ontology Mapping
* Rule-Based Recommendation Systems

The system intelligently filters and recommends destinations according to user requirements.

Objective

The objective of this project is to:

* Build a knowledge-based recommendation system
* Store travel information using structured knowledge
* Use ontology mapping for intent understanding
* Recommend destinations based on preferences
* Demonstrate AI-based decision making

Concepts Used

Knowledge Base

A Knowledge Base stores structured information about travel destinations.

Each destination contains:

* Place name
* Place type
* Estimated cost
* Available food options

Ontology

Ontology is used to map user intents into destination categories.

Example:

* leisure → beach
* adventure → mountain
* urban → city

This helps the system understand natural user preferences.

Recommendation System

The recommendation system filters destinations based on:

* Travel type
* Budget
* Food preference

The results are sorted according to budget similarity.

Code Explanation

Class: KnowledgeBase

class KnowledgeBase:

This class stores all travel-related information.

Constructor

def **init**(self):

Purpose:
Initializes:

* Travel destinations
* Ontology mappings

Places Dataset

self.places = [...]

Stores all destination details.

Each destination contains:

* name
* type
* cost
* food

Example:

{
"name": "Goa",
"type": "beach",
"cost": 18000,
"food": ["Seafood", "Goan", "Continental"]
}

Ontology Mapping

self.ontology = {
"leisure": "beach",
"adventure": "mountain",
"urban": "city"
}

Purpose:
Converts user intent into destination categories.

Get All Foods Function

def get_all_foods(self):

Purpose:
Returns all available food options from the dataset.

Logic:

* Uses set comprehension to avoid duplicates
* Sorts food list alphabetically

Class: TravelPlanner

class TravelPlanner:

This class handles recommendation logic.

Constructor

def **init**(self, kb):
self.kb = kb

Purpose:
Initializes the Knowledge Base.

Parameters:

* kb → KnowledgeBase object

Budget Conversion Function

def get_budget_value(self, budget_choice):

Purpose:
Converts budget categories into numeric values.

Mappings:

* low → 10000
* medium → 20000
* high → 50000

Intent Mapping Function

def map_intent(self, intent):

Purpose:
Maps user intent using ontology.

Example:

* leisure → beach

Recommendation Function

def recommend(self, intent, budget_choice, food_pref):

Purpose:
Main recommendation engine.

Steps Performed

Step 1:
Convert user intent into place type.

Step 2:
Convert budget category into numeric value.

Step 3:
Filter places by destination type.

Step 4:
Filter by food preference.

Step 5:
Sort places according to budget similarity.

Filtering Logic

filtered = [p for p in self.kb.places if p["type"] == place_type]

Filters destinations matching selected type.

Food Preference Filtering

if food_pref.lower() != "any":

Checks whether user entered specific food preference.

Sorting Logic

filtered.sort(key=lambda x: abs(x["cost"] - budget))

Purpose:
Sorts destinations based on closest budget match.

Print Results Function

def print_results(results):

Purpose:
Displays recommended destinations in formatted style.

Displayed Information:

* Place name
* Destination type
* Food options
* Estimated cost per day

Program Flow

Step 1:
User enters travel preference:

* leisure
* adventure
* urban
  OR direct category:
* beach
* mountain
* city

Step 2:
User selects budget:

* low
* medium
* high

Step 3:
User selects food preference.

Step 4:
System filters matching destinations.

Step 5:
Recommended destinations are displayed.

Sample Input

Enter preference: leisure
Enter budget: medium
Enter food preference: Seafood

Expected Output

AI Travel Recommendations:

Preference 1:
Place: Goa
Type: beach
Food: Seafood, Goan, Continental
Cost/Day: ₹18000

Preference 2:
Place: Pondicherry
Type: beach
Food: French, Seafood, South Indian
Cost/Day: ₹12000

Knowledge Representation Example

Destination Knowledge Example

{
"name": "Manali",
"type": "mountain",
"cost": 12000,
"food": ["North Indian", "Cafe"]
}

Ontology Representation

{
"leisure": "beach",
"adventure": "mountain",
"urban": "city"
}

Time Complexity

Filtering Complexity:
O(n)

Sorting Complexity:
O(n log n)

Where:

* n = Number of destinations

Space Complexity

O(n)

Because filtered destinations are stored in lists.

Advantages

* Simple AI-based recommendation system
* Uses ontology for intelligent mapping
* Easy to expand with more destinations
* Supports multiple user preferences
* Demonstrates knowledge representation concepts

Limitations

* Uses static dataset
* Limited destination types
* No real-time travel data
* No machine learning used

Test Cases

Test Case 1

Input

Preference: leisure
Budget: medium
Food: Seafood

Expected Output

Goa
Pondicherry

Test Case 2

Input

Preference: adventure
Budget: low
Food: Cafe

Expected Output

Manali

Test Case 3

Input

Preference: urban
Budget: medium
Food: Biryani

Expected Output

Hyderabad

Test Case 4

Input

Preference: beach
Budget: high
Food: International

Expected Output

Maldives

Test Case 5

Input

Preference: mountain
Budget: low
Food: South Indian

Expected Output

Ooty