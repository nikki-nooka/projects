import random
import time

def get_mood_recommendations(mood, intensity=5, time_of_day="Afternoon", get_recipes=False):
    """
    Get food recommendations based on mood
    
    Args:
        mood: User's current mood
        intensity: Intensity of the mood (1-10)
        time_of_day: Time of day (Morning, Afternoon, Evening, Late Night)
        get_recipes: Whether to return recipe objects instead of simple food names
        
    Returns:
        List of recommended foods or recipes
    """
    # Simulate processing time
    time.sleep(0.5)
    
    # Define mood-based food recommendations with explanations
    mood_foods = {
        "Happy": {
            "foods": [
                {"name": "Dark Chocolate", "reason": "Contains compounds that trigger the release of endorphins", "nutrients": "Antioxidants, Magnesium", "color": "#795548"},
                {"name": "Berries", "reason": "The natural sweetness and bright colors enhance positive feelings", "nutrients": "Vitamin C, Antioxidants", "color": "#E91E63"},
                {"name": "Yogurt Parfait", "reason": "Probiotics support gut health, which is linked to mood", "nutrients": "Protein, Probiotics, Calcium", "color": "#9C27B0"},
                {"name": "Fruit Smoothie", "reason": "Natural sugars provide immediate energy boost", "nutrients": "Vitamins, Fiber, Natural Sugars", "color": "#3F51B5"},
                {"name": "Trail Mix", "reason": "Variety of textures and flavors create a satisfying experience", "nutrients": "Healthy Fats, Protein, Iron", "color": "#FF9800"}
            ]
        },
        "Sad": {
            "foods": [
                {"name": "Dark Chocolate", "reason": "Stimulates the production of endorphins that can elevate mood", "nutrients": "Magnesium, Antioxidants", "color": "#795548"},
                {"name": "Banana", "reason": "Contains dopamine precursors that help regulate mood", "nutrients": "Vitamin B6, Potassium", "color": "#FFEB3B"},
                {"name": "Salmon", "reason": "Omega-3 fatty acids support brain health and mood regulation", "nutrients": "Omega-3s, Vitamin D, Protein", "color": "#FF5722"},
                {"name": "Green Tea", "reason": "L-theanine promotes relaxation without drowsiness", "nutrients": "L-theanine, Antioxidants", "color": "#4CAF50"},
                {"name": "Walnuts", "reason": "Rich in serotonin that helps stabilize mood", "nutrients": "Omega-3s, Antioxidants", "color": "#8D6E63"}
            ]
        },
        "Energetic": {
            "foods": [
                {"name": "Apple with Almond Butter", "reason": "Balanced protein and complex carbs for sustained energy", "nutrients": "Fiber, Protein, Healthy Fats", "color": "#8BC34A"},
                {"name": "Greek Yogurt with Honey", "reason": "Protein-rich with natural sweetness for quick energy", "nutrients": "Protein, Probiotics, Natural Sugars", "color": "#F5F5F5"},
                {"name": "Rice Cakes with Avocado", "reason": "Healthy fats and carbs for lasting energy", "nutrients": "Healthy Fats, Complex Carbs", "color": "#CDDC39"},
                {"name": "Edamame", "reason": "Plant protein and fiber keep energy levels stable", "nutrients": "Protein, Fiber, Iron", "color": "#4CAF50"},
                {"name": "Hummus with Vegetables", "reason": "Balanced nutrition with protein and complex carbs", "nutrients": "Protein, Fiber, Healthy Fats", "color": "#FFC107"}
            ]
        },
        "Tired": {
            "foods": [
                {"name": "Oatmeal with Fruit", "reason": "Slow-release carbs provide steady energy", "nutrients": "Complex Carbs, Fiber, B Vitamins", "color": "#BEIGE"},
                {"name": "Banana with Peanut Butter", "reason": "Natural sugars paired with protein for sustained energy", "nutrients": "Potassium, Protein, Magnesium", "color": "#FFEB3B"},
                {"name": "Green Smoothie", "reason": "Nutrient-dense with a mix of vitamins and minerals", "nutrients": "Iron, B Vitamins, Folate", "color": "#4CAF50"},
                {"name": "Hard-Boiled Eggs", "reason": "Protein and choline support brain function", "nutrients": "Protein, Choline, B12", "color": "#F5F5F5"},
                {"name": "Trail Mix", "reason": "Quick energy from dried fruits and sustained energy from nuts", "nutrients": "Healthy Fats, Natural Sugars, Protein", "color": "#FF9800"}
            ]
        },
        "Stressed": {
            "foods": [
                {"name": "Dark Chocolate", "reason": "Reduces cortisol and helps lower stress levels", "nutrients": "Magnesium, Antioxidants", "color": "#795548"},
                {"name": "Avocado Toast", "reason": "B vitamins help reduce stress and anxiety", "nutrients": "Healthy Fats, B Vitamins, Fiber", "color": "#8BC34A"},
                {"name": "Chamomile Tea", "reason": "Contains compounds that promote relaxation", "nutrients": "Antioxidants, Anti-inflammatory compounds", "color": "#FFECB3"},
                {"name": "Blueberries", "reason": "Antioxidants help counteract stress hormones", "nutrients": "Vitamin C, Antioxidants", "color": "#3F51B5"},
                {"name": "Yogurt with Almonds", "reason": "Probiotics and magnesium work together to calm the nervous system", "nutrients": "Probiotics, Magnesium, Protein", "color": "#F5F5F5"}
            ]
        },
        "Relaxed": {
            "foods": [
                {"name": "Herbal Tea", "reason": "Calming herbs promote continued relaxation", "nutrients": "Antioxidants, Anti-inflammatory compounds", "color": "#4CAF50"},
                {"name": "Warm Oatmeal", "reason": "Comforting and increases serotonin levels", "nutrients": "Complex Carbs, Fiber, B Vitamins", "color": "#BEIGE"},
                {"name": "Cottage Cheese with Fruit", "reason": "Contains the sleep-promoting amino acid tryptophan", "nutrients": "Protein, Calcium, Tryptophan", "color": "#F5F5F5"},
                {"name": "Roasted Pumpkin Seeds", "reason": "Rich in magnesium which helps maintain relaxation", "nutrients": "Magnesium, Zinc, Protein", "color": "#8D6E63"},
                {"name": "Peppermint Dark Chocolate", "reason": "Aromatherapeutic properties combined with stress-reducing compounds", "nutrients": "Magnesium, Antioxidants", "color": "#795548"}
            ]
        },
        "Focused": {
            "foods": [
                {"name": "Blueberries", "reason": "Antioxidants improve brain function and memory", "nutrients": "Antioxidants, Vitamin K", "color": "#3F51B5"},
                {"name": "Walnuts", "reason": "Omega-3 fatty acids support brain health", "nutrients": "Omega-3s, Antioxidants", "color": "#8D6E63"},
                {"name": "Green Tea", "reason": "Contains L-theanine which improves focus without jitters", "nutrients": "L-theanine, Antioxidants", "color": "#4CAF50"},
                {"name": "Dark Chocolate", "reason": "Improves blood flow to the brain and contains natural stimulants", "nutrients": "Flavanols, Caffeine", "color": "#795548"},
                {"name": "Pumpkin Seeds", "reason": "Rich in zinc which is essential for cognitive function", "nutrients": "Zinc, Magnesium, Healthy Fats", "color": "#8D6E63"}
            ]
        },
        "Hungry": {
            "foods": [
                {"name": "Greek Yogurt with Berries", "reason": "Protein-rich to provide satiety", "nutrients": "Protein, Probiotics, Vitamin C", "color": "#9C27B0"},
                {"name": "Apple with Nut Butter", "reason": "Fiber and protein combination keeps you full", "nutrients": "Fiber, Protein, Healthy Fats", "color": "#8BC34A"},
                {"name": "Hummus with Vegetables", "reason": "Fiber-rich for satiety with protein and healthy fats", "nutrients": "Protein, Fiber, Healthy Fats", "color": "#FFC107"},
                {"name": "Oatmeal with Nuts", "reason": "Complex carbs with protein for lasting fullness", "nutrients": "Complex Carbs, Fiber, Protein", "color": "#BEIGE"},
                {"name": "Hard-Boiled Eggs", "reason": "High protein content suppresses hunger hormones", "nutrients": "Protein, Choline, B12", "color": "#F5F5F5"}
            ]
        }
    }
    
    # If mood not found, default to Energetic
    if mood not in mood_foods:
        mood = "Energetic"
    
    # Select foods based on mood
    foods = mood_foods[mood]["foods"]
    
    # Adjust recommendations based on time of day
    if time_of_day == "Morning":
        # Prioritize energizing options
        foods = sorted(foods, key=lambda x: "energy" in x["reason"].lower() or "boost" in x["reason"].lower(), reverse=True)
    elif time_of_day == "Evening" or time_of_day == "Late Night":
        # Prioritize relaxing options
        foods = sorted(foods, key=lambda x: "relax" in x["reason"].lower() or "calm" in x["reason"].lower(), reverse=True)
    
    # If get_recipes is True, convert to recipe format
    if get_recipes:
        recipes = []
        for food in foods:
            # Create a recipe object
            recipe = {
                "id": f"recipe_{random.randint(1000, 9999)}",
                "name": food["name"],
                "reason": food["reason"],
                "nutrients": food["nutrients"],
                "color": food["color"],
                "time": random.randint(5, 30),
                "calories": random.randint(100, 400),
                "key_ingredients": generate_ingredients_for_food(food["name"]),
                "steps": generate_steps_for_food(food["name"]),
                "image_url": ""  # Would be a real URL in production
            }
            recipes.append(recipe)
        return recipes
    
    # Otherwise return simple food recommendation list
    return foods

def generate_ingredients_for_food(food_name):
    """Generate plausible ingredients for a food"""
    
    ingredients_by_food = {
        "Dark Chocolate": ["Cocoa powder", "Cocoa butter", "Sugar", "Vanilla extract", "Sea salt"],
        "Berries": ["Strawberries", "Blueberries", "Raspberries", "Blackberries"],
        "Yogurt Parfait": ["Greek yogurt", "Granola", "Honey", "Mixed berries", "Chia seeds"],
        "Fruit Smoothie": ["Banana", "Berries", "Greek yogurt", "Almond milk", "Honey"],
        "Trail Mix": ["Almonds", "Walnuts", "Dark chocolate chips", "Dried cranberries", "Pumpkin seeds"],
        "Banana": ["Ripe banana"],
        "Salmon": ["Salmon fillet", "Olive oil", "Lemon", "Dill", "Black pepper"],
        "Green Tea": ["Green tea leaves", "Hot water", "Lemon (optional)", "Honey (optional)"],
        "Walnuts": ["Raw walnuts"],
        "Apple with Almond Butter": ["Apple", "Almond butter", "Cinnamon (optional)"],
        "Greek Yogurt with Honey": ["Greek yogurt", "Honey", "Cinnamon", "Vanilla extract"],
        "Rice Cakes with Avocado": ["Brown rice cakes", "Ripe avocado", "Sea salt", "Red pepper flakes"],
        "Edamame": ["Fresh or frozen edamame pods", "Sea salt"],
        "Hummus with Vegetables": ["Chickpeas", "Tahini", "Olive oil", "Lemon juice", "Garlic", "Carrots", "Cucumber", "Bell peppers"],
        "Oatmeal with Fruit": ["Rolled oats", "Milk or water", "Banana", "Berries", "Honey"],
        "Banana with Peanut Butter": ["Ripe banana", "Natural peanut butter"],
        "Green Smoothie": ["Spinach", "Banana", "Apple", "Almond milk", "Chia seeds"],
        "Hard-Boiled Eggs": ["Eggs", "Salt", "Pepper"],
        "Avocado Toast": ["Whole grain bread", "Ripe avocado", "Lemon juice", "Red pepper flakes", "Sea salt"],
        "Chamomile Tea": ["Dried chamomile flowers", "Hot water", "Honey (optional)"],
        "Blueberries": ["Fresh blueberries"],
        "Yogurt with Almonds": ["Greek yogurt", "Almonds", "Honey", "Cinnamon"],
        "Herbal Tea": ["Herbal tea blend", "Hot water", "Honey (optional)"],
        "Warm Oatmeal": ["Rolled oats", "Milk or water", "Cinnamon", "Honey", "Chopped nuts"],
        "Cottage Cheese with Fruit": ["Cottage cheese", "Fresh berries", "Honey", "Cinnamon"],
        "Roasted Pumpkin Seeds": ["Raw pumpkin seeds", "Olive oil", "Sea salt", "Spices of choice"],
        "Peppermint Dark Chocolate": ["Dark chocolate", "Peppermint extract", "Cocoa powder", "Sugar", "Coconut oil"],
        "Pumpkin Seeds": ["Raw pumpkin seeds"]
    }
    
    # Return specific ingredients if available, otherwise generate generic ones
    if food_name in ingredients_by_food:
        return ingredients_by_food[food_name]
    else:
        # Generate generic ingredients
        base_ingredients = ["Main ingredient", "Secondary ingredient", "Seasoning", "Garnish"]
        return [f"{food_name} base"] + base_ingredients

def generate_steps_for_food(food_name):
    """Generate plausible preparation steps for a food"""
    
    steps_by_food = {
        "Dark Chocolate": [
            "Break the chocolate into small pieces and place in a microwave-safe bowl.",
            "Microwave in 30-second intervals, stirring between each until melted.",
            "Pour into molds or onto a parchment-lined tray.",
            "Let cool and harden before enjoying."
        ],
        "Yogurt Parfait": [
            "Place a layer of Greek yogurt at the bottom of a glass.",
            "Add a layer of granola.",
            "Add a layer of mixed berries.",
            "Repeat the layers, ending with berries on top.",
            "Drizzle with honey and sprinkle with chia seeds."
        ],
        "Fruit Smoothie": [
            "Add all ingredients to a blender.",
            "Blend until smooth.",
            "Pour into a glass and enjoy immediately."
        ],
        "Apple with Almond Butter": [
            "Wash and slice the apple into wedges.",
            "Spread almond butter on each slice.",
            "Sprinkle with cinnamon if desired."
        ],
        "Hummus with Vegetables": [
            "Blend chickpeas, tahini, olive oil, lemon juice, and garlic until smooth.",
            "Wash and cut vegetables into sticks.",
            "Serve hummus in a bowl with vegetable sticks for dipping."
        ],
        "Avocado Toast": [
            "Toast the bread until golden and crisp.",
            "Cut the avocado in half, remove the pit, and scoop out the flesh.",
            "Mash the avocado with lemon juice, salt, and pepper.",
            "Spread the mashed avocado on the toast.",
            "Sprinkle with red pepper flakes and sea salt."
        ]
    }
    
    # Return specific steps if available, otherwise generate generic ones
    if food_name in steps_by_food:
        return steps_by_food[food_name]
    else:
        # Generate generic steps based on food type
        if "Smoothie" in food_name:
            return [
                "Add all ingredients to a blender.",
                "Blend until smooth.",
                "Pour into a glass and enjoy immediately."
            ]
        elif "Tea" in food_name:
            return [
                "Boil water in a kettle.",
                "Place tea in a mug.",
                "Pour hot water over the tea.",
                "Let steep for 3-5 minutes.",
                "Remove tea and add sweetener if desired."
            ]
        elif "Toast" in food_name:
            return [
                "Toast bread until golden brown.",
                "Prepare toppings by slicing or mashing.",
                "Spread toppings evenly on toast.",
                "Sprinkle with seasonings as desired.",
                "Serve immediately while warm."
            ]
        else:
            return [
                f"Prepare {food_name} according to package instructions.",
                "Arrange on a plate or bowl.",
                "Add optional toppings or seasonings.",
                "Serve and enjoy."
            ]
