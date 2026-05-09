class KnowledgeBase:
    def __init__(self):
        self.places = [
            {"name": "Goa", "type": "beach", "cost": 18000, "food": ["Seafood", "Goan", "Continental"]},
            {"name": "Maldives", "type": "beach", "cost": 55000, "food": ["Seafood", "International"]},
            {"name": "Bali", "type": "beach", "cost": 35000, "food": ["Asian", "Continental"]},
            {"name": "Pondicherry", "type": "beach", "cost": 12000, "food": ["French", "Seafood", "South Indian"]},

            {"name": "Manali", "type": "mountain", "cost": 12000, "food": ["North Indian", "Cafe"]},
            {"name": "Shimla", "type": "mountain", "cost": 10000, "food": ["North Indian"]},
            {"name": "Ladakh", "type": "mountain", "cost": 22000, "food": ["Tibetan", "North Indian"]},
            {"name": "Ooty", "type": "mountain", "cost": 9000, "food": ["South Indian"]},

            {"name": "Delhi", "type": "city", "cost": 8000, "food": ["Street Food", "Mughlai"]},
            {"name": "Mumbai", "type": "city", "cost": 15000, "food": ["Street Food", "Seafood"]},
            {"name": "Hyderabad", "type": "city", "cost": 10000, "food": ["Biryani", "South Indian"]},
            {"name": "Bangalore", "type": "city", "cost": 12000, "food": ["Cafe", "South Indian"]}
        ]

        self.ontology = {
            "leisure": "beach",
            "adventure": "mountain",
            "urban": "city"
        }

    def get_all_foods(self):
        return sorted({f for p in self.places for f in p["food"]})


class TravelPlanner:
    def __init__(self, kb):
        self.kb = kb

    def get_budget_value(self, budget_choice):
        return {"low": 10000, "medium": 20000, "high": 50000}.get(budget_choice, 20000)

    def map_intent(self, intent):
        return self.kb.ontology.get(intent, intent)

    def recommend(self, intent, budget_choice, food_pref):
        place_type = self.map_intent(intent)
        budget = self.get_budget_value(budget_choice)

        filtered = [p for p in self.kb.places if p["type"] == place_type]

        if food_pref.lower() != "any":
            temp = []
            for p in filtered:
                if any(food_pref.lower() in f.lower() for f in p["food"]):
                    temp.append(p)
            if temp:
                filtered = temp

        filtered.sort(key=lambda x: abs(x["cost"] - budget))

        return filtered


def print_results(results):
    print("\nAI Travel Recommendations:\n")

    for i, place in enumerate(results):
        print(f"Preference {i+1}:")
        print(f"  Place: {place['name']}")
        print(f"  Type: {place['type']}")
        print(f"  Food: {', '.join(place['food'])}")
        print(f"  Cost/Day: ₹{place['cost']}\n")


if __name__ == "__main__":
    kb = KnowledgeBase()
    planner = TravelPlanner(kb)

    print("Intent (leisure/adventure/urban) OR direct (beach/mountain/city)")
    intent = input("Enter preference: ").lower()

    print("\nBudget Options:")
    print("low (≤ ₹10,000)")
    print("medium (≤ ₹20,000)")
    print("high (≤ ₹50,000)")
    budget_choice = input("Enter budget: ").lower()

    foods = kb.get_all_foods()
    print("\nAvailable Food Options:")
    print(", ".join(foods))
    print("Type 'any' for no preference")
    food_pref = input("Enter food preference: ")

    results = planner.recommend(intent, budget_choice, food_pref)

    if results:
        print_results(results)
    else:
        print("\nNo matching places found.")