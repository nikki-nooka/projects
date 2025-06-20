import random
import time

def get_recipe_recommendation(food_name, healthy=True):
    """
    Get recipe recommendations based on food name
    
    Args:
        food_name: Name of the food
        healthy: Whether to focus on healthy recipes
        
    Returns:
        List of recipe dictionaries
    """
    # Simulate processing time
    time.sleep(0.5)
    
    # Healthy recipe ideas for common foods
    healthy_recipes = {
        "Apple": [
            {"name": "Apple Cinnamon Overnight Oats", "difficulty": "Easy", "time": 10},
            {"name": "Baked Apple with Walnuts and Honey", "difficulty": "Easy", "time": 25},
            {"name": "Apple Spinach Smoothie", "difficulty": "Easy", "time": 5}
        ],
        "Banana": [
            {"name": "Banana Peanut Butter Smoothie", "difficulty": "Easy", "time": 5},
            {"name": "Banana Oatmeal Cookies", "difficulty": "Medium", "time": 20},
            {"name": "Banana Chia Pudding", "difficulty": "Easy", "time": 10}
        ],
        "Avocado": [
            {"name": "Avocado Toast with Egg", "difficulty": "Easy", "time": 10},
            {"name": "Avocado Chocolate Mousse", "difficulty": "Medium", "time": 15},
            {"name": "Stuffed Avocados with Quinoa Salad", "difficulty": "Medium", "time": 20}
        ],
        "Greek Yogurt": [
            {"name": "Greek Yogurt Parfait", "difficulty": "Easy", "time": 5},
            {"name": "Tzatziki Sauce", "difficulty": "Easy", "time": 10},
            {"name": "Frozen Greek Yogurt Bark", "difficulty": "Easy", "time": 15}
        ],
        "Salmon": [
            {"name": "Baked Lemon Garlic Salmon", "difficulty": "Medium", "time": 25},
            {"name": "Salmon Avocado Poke Bowl", "difficulty": "Medium", "time": 20},
            {"name": "Grilled Salmon with Dill Sauce", "difficulty": "Medium", "time": 15}
        ],
        "Broccoli": [
            {"name": "Roasted Broccoli with Garlic", "difficulty": "Easy", "time": 20},
            {"name": "Broccoli Cheddar Soup", "difficulty": "Medium", "time": 30},
            {"name": "Broccoli Quinoa Salad", "difficulty": "Easy", "time": 15}
        ],
    }
    
    # Healthier alternative recipes for unhealthy foods
    alternative_recipes = {
        "French Fries": [
            {"name": "Baked Sweet Potato Fries", "difficulty": "Easy", "time": 25},
            {"name": "Air Fryer Vegetable Fries", "difficulty": "Easy", "time": 20},
            {"name": "Zucchini Fries with Greek Yogurt Dip", "difficulty": "Medium", "time": 30}
        ],
        "Cheeseburger": [
            {"name": "Portobello Mushroom Burger", "difficulty": "Medium", "time": 25},
            {"name": "Turkey Spinach Burger on Whole Grain Bun", "difficulty": "Medium", "time": 20},
            {"name": "Lentil Walnut Burger", "difficulty": "Medium", "time": 35}
        ],
        "Chocolate Cake": [
            {"name": "Flourless Dark Chocolate Cake", "difficulty": "Medium", "time": 40},
            {"name": "Chocolate Avocado Mousse", "difficulty": "Easy", "time": 15},
            {"name": "Black Bean Brownies", "difficulty": "Medium", "time": 30}
        ],
        "Pizza": [
            {"name": "Cauliflower Crust Veggie Pizza", "difficulty": "Medium", "time": 45},
            {"name": "Whole Grain Flatbread Pizza", "difficulty": "Easy", "time": 20},
            {"name": "Portobello Mushroom Mini Pizzas", "difficulty": "Easy", "time": 25}
        ],
        "Ice Cream": [
            {"name": "Frozen Banana Nice Cream", "difficulty": "Easy", "time": 10},
            {"name": "Greek Yogurt Berry Freeze", "difficulty": "Easy", "time": 15},
            {"name": "Chia Seed Pudding with Fruit", "difficulty": "Easy", "time": 15}
        ],
    }
    
    # Select the appropriate recipe list
    if healthy and food_name in healthy_recipes:
        recipes = healthy_recipes[food_name]
    elif not healthy and food_name in alternative_recipes:
        recipes = alternative_recipes[food_name]
    else:
        # Generate generic recipes if specific ones aren't available
        recipes = [
            {"name": f"Healthy {food_name} Bowl", "difficulty": "Easy", "time": random.randint(10, 20)},
            {"name": f"Baked {food_name} with Herbs", "difficulty": "Medium", "time": random.randint(20, 30)},
            {"name": f"{food_name} Salad", "difficulty": "Easy", "time": random.randint(10, 15)}
        ]
    
    # Add unique ids and additional information to recipes
    for i, recipe in enumerate(recipes):
        recipe["id"] = f"recipe_{random.randint(1000, 9999)}"
        recipe["calories"] = random.randint(150, 450)
        recipe["rating"] = round(random.uniform(3.5, 5.0), 1)
        
        # Add color for visual variety in UI
        colors = ["#4CAF50", "#2196F3", "#F44336", "#FF9800", "#9C27B0", "#3F51B5"]
        recipe["color"] = random.choice(colors)
    
    return recipes

def get_recipe_by_ingredients(ingredients):
    """
    Get recipes based on available ingredients
    
    Args:
        ingredients: List of available ingredients
        
    Returns:
        List of recipe dictionaries with ingredients used
    """
    # Simulate processing time
    time.sleep(0.8)
    
    # Sample recipe database with ingredient requirements
    recipe_database = [
        {
            "id": "recipe_1001",
            "name": "Apple Cinnamon Oatmeal",
            "required_ingredients": ["Apple", "Oats", "Cinnamon"],
            "optional_ingredients": ["Honey", "Almonds", "Milk"],
            "time": 15,
            "calories": 320,
            "difficulty": "Easy"
        },
        {
            "id": "recipe_1002",
            "name": "Berry Yogurt Parfait",
            "required_ingredients": ["Berries", "Greek Yogurt"],
            "optional_ingredients": ["Honey", "Granola", "Chia Seeds"],
            "time": 5,
            "calories": 210,
            "difficulty": "Easy"
        },
        {
            "id": "recipe_1003",
            "name": "Avocado Toast",
            "required_ingredients": ["Avocado", "Whole Grain Bread"],
            "optional_ingredients": ["Eggs", "Tomato", "Salt", "Pepper"],
            "time": 10,
            "calories": 280,
            "difficulty": "Easy"
        },
        {
            "id": "recipe_1004",
            "name": "Banana Smoothie Bowl",
            "required_ingredients": ["Banana", "Greek Yogurt"],
            "optional_ingredients": ["Berries", "Almonds", "Honey", "Chia Seeds"],
            "time": 10,
            "calories": 290,
            "difficulty": "Easy"
        },
        {
            "id": "recipe_1005",
            "name": "Vegetable Hummus Wrap",
            "required_ingredients": ["Hummus", "Spinach", "Carrot"],
            "optional_ingredients": ["Bell Pepper", "Cucumber", "Whole Grain Bread"],
            "time": 15,
            "calories": 340,
            "difficulty": "Easy"
        },
        {
            "id": "recipe_1006",
            "name": "Trail Mix",
            "required_ingredients": ["Almonds", "Walnuts"],
            "optional_ingredients": ["Dark Chocolate", "Dried Cranberries", "Pumpkin Seeds"],
            "time": 5,
            "calories": 210,
            "difficulty": "Easy"
        },
        {
            "id": "recipe_1007",
            "name": "Egg and Vegetable Muffins",
            "required_ingredients": ["Eggs", "Spinach", "Bell Pepper"],
            "optional_ingredients": ["Cheese", "Tomato", "Onion"],
            "time": 25,
            "calories": 220,
            "difficulty": "Medium"
        },
        {
            "id": "recipe_1008",
            "name": "Quinoa Salad",
            "required_ingredients": ["Quinoa", "Cucumber", "Tomato"],
            "optional_ingredients": ["Feta Cheese", "Olive Oil", "Lemon"],
            "time": 20,
            "calories": 310,
            "difficulty": "Medium"
        },
        {
            "id": "recipe_1009",
            "name": "Apple Almond Butter Snack",
            "required_ingredients": ["Apple", "Almond Butter"],
            "optional_ingredients": ["Cinnamon", "Honey"],
            "time": 5,
            "calories": 180,
            "difficulty": "Easy"
        },
        {
            "id": "recipe_1010",
            "name": "Energy Balls",
            "required_ingredients": ["Oats", "Peanut Butter", "Honey"],
            "optional_ingredients": ["Dark Chocolate", "Chia Seeds", "Coconut"],
            "time": 15,
            "calories": 240,
            "difficulty": "Easy"
        }
    ]
    
    # Convert ingredient list to lowercase for case-insensitive matching
    available_ingredients = [ing.lower() for ing in ingredients]
    
    # Find recipes that can be made with available ingredients
    matching_recipes = []
    
    for recipe in recipe_database:
        # Check how many required ingredients we have
        required_count = 0
        required_total = len(recipe["required_ingredients"])
        
        for req_ing in recipe["required_ingredients"]:
            if req_ing.lower() in available_ingredients:
                required_count += 1
        
        # Check how many optional ingredients we have
        optional_count = 0
        optional_total = len(recipe["optional_ingredients"])
        
        for opt_ing in recipe["optional_ingredients"]:
            if opt_ing.lower() in available_ingredients:
                optional_count += 1
        
        # Calculate match score (percentage of required ingredients + bonus for optional)
        required_percentage = required_count / required_total if required_total > 0 else 0
        optional_percentage = optional_count / optional_total if optional_total > 0 else 0
        
        match_score = required_percentage * 0.7 + optional_percentage * 0.3
        
        # Create lists of ingredients used and missing
        ingredients_used = []
        missing_ingredients = []
        
        for ing in recipe["required_ingredients"]:
            if ing.lower() in available_ingredients:
                ingredients_used.append(ing)
            else:
                missing_ingredients.append(ing)
        
        for ing in recipe["optional_ingredients"]:
            if ing.lower() in available_ingredients:
                ingredients_used.append(ing)
        
        # Only include recipe if it has at least 50% of required ingredients
        if required_percentage >= 0.5:
            recipe_copy = recipe.copy()
            recipe_copy["match_score"] = match_score
            recipe_copy["ingredients_used"] = ingredients_used
            recipe_copy["missing_ingredients"] = missing_ingredients
            
            # Add color for visual variety in UI
            colors = ["#4CAF50", "#2196F3", "#F44336", "#FF9800", "#9C27B0", "#3F51B5"]
            recipe_copy["color"] = random.choice(colors)
            
            matching_recipes.append(recipe_copy)
    
    # Sort by match score
    matching_recipes.sort(key=lambda x: x["match_score"], reverse=True)
    
    return matching_recipes

def search_recipes(query, meal_types=None, max_time=None, dietary_restrictions=None, max_calories=None, difficulty=None, sort_by="Popularity", limit=10):
    """
    Search for recipes based on criteria
    
    Args:
        query: Search query
        meal_types: List of meal types (Breakfast, Snack, Lunch, Dinner, Dessert)
        max_time: Maximum preparation time in minutes
        dietary_restrictions: List of dietary restrictions
        max_calories: Maximum calories per serving
        difficulty: Difficulty level (Easy, Medium, Hard)
        sort_by: Sort method (Popularity, Quick & Easy, Nutritional Value)
        limit: Maximum number of results to return
        
    Returns:
        List of matching recipes
    """
    # Simulate processing time
    time.sleep(0.5)
    
    # Sample recipe database
    recipes_db = [
        {
            "id": "recipe_1001",
            "name": "Apple Cinnamon Overnight Oats",
            "meal_types": ["Breakfast", "Snack"],
            "time": 10,
            "calories": 320,
            "difficulty": "Easy",
            "popularity": 4.7,
            "nutritional_value": 8.5,
            "dietary_properties": ["Vegetarian"],
            "description": "A delicious and filling breakfast that you prepare the night before."
        },
        {
            "id": "recipe_1002",
            "name": "Berry Yogurt Parfait",
            "meal_types": ["Breakfast", "Snack", "Dessert"],
            "time": 5,
            "calories": 210,
            "difficulty": "Easy",
            "popularity": 4.5,
            "nutritional_value": 8.0,
            "dietary_properties": ["Vegetarian", "Gluten-Free"],
            "description": "A quick, protein-rich breakfast or snack with layers of yogurt, berries, and granola."
        },
        {
            "id": "recipe_1003",
            "name": "Avocado Toast with Poached Egg",
            "meal_types": ["Breakfast", "Lunch"],
            "time": 15,
            "calories": 350,
            "difficulty": "Medium",
            "popularity": 4.8,
            "nutritional_value": 8.7,
            "dietary_properties": ["Vegetarian"],
            "description": "Creamy avocado on toasted bread topped with a perfectly poached egg."
        },
        {
            "id": "recipe_1004",
            "name": "Green Smoothie Bowl",
            "meal_types": ["Breakfast", "Snack"],
            "time": 10,
            "calories": 290,
            "difficulty": "Easy",
            "popularity": 4.3,
            "nutritional_value": 9.0,
            "dietary_properties": ["Vegetarian", "Vegan", "Gluten-Free", "Dairy-Free"],
            "description": "A nutritious smoothie bowl packed with leafy greens, fruits, and healthy toppings."
        },
        {
            "id": "recipe_1005",
            "name": "Hummus and Vegetable Wrap",
            "meal_types": ["Lunch", "Snack"],
            "time": 15,
            "calories": 340,
            "difficulty": "Easy",
            "popularity": 4.2,
            "nutritional_value": 7.8,
            "dietary_properties": ["Vegetarian", "Vegan", "Dairy-Free"],
            "description": "A portable wrap filled with creamy hummus and crunchy fresh vegetables."
        },
        {
            "id": "recipe_1006",
            "name": "Homemade Trail Mix",
            "meal_types": ["Snack"],
            "time": 5,
            "calories": 210,
            "difficulty": "Easy",
            "popularity": 4.0,
            "nutritional_value": 7.5,
            "dietary_properties": ["Vegetarian", "Gluten-Free", "Dairy-Free"],
            "description": "A customizable energy-boosting mix of nuts, seeds, and dried fruits."
        },
        {
            "id": "recipe_1007",
            "name": "Mini Vegetable Frittatas",
            "meal_types": ["Breakfast", "Snack"],
            "time": 25,
            "calories": 220,
            "difficulty": "Medium",
            "popularity": 4.4,
            "nutritional_value": 8.3,
            "dietary_properties": ["Vegetarian", "Gluten-Free"],
            "description": "Protein-packed egg muffins filled with colorful vegetables."
        },
        {
            "id": "recipe_1008",
            "name": "Mediterranean Quinoa Salad",
            "meal_types": ["Lunch", "Dinner", "Snack"],
            "time": 20,
            "calories": 310,
            "difficulty": "Medium",
            "popularity": 4.6,
            "nutritional_value": 8.9,
            "dietary_properties": ["Vegetarian", "Gluten-Free"],
            "description": "A protein-rich salad with Mediterranean flavors that works as a meal or side dish."
        },
        {
            "id": "recipe_1009",
            "name": "Apple Slices with Almond Butter",
            "meal_types": ["Snack"],
            "time": 5,
            "calories": 180,
            "difficulty": "Easy",
            "popularity": 4.1,
            "nutritional_value": 7.2,
            "dietary_properties": ["Vegetarian", "Vegan", "Gluten-Free", "Dairy-Free"],
            "description": "A simple, satisfying snack combining crisp apples with creamy almond butter."
        },
        {
            "id": "recipe_1010",
            "name": "No-Bake Energy Balls",
            "meal_types": ["Snack", "Dessert"],
            "time": 15,
            "calories": 240,
            "difficulty": "Easy",
            "popularity": 4.5,
            "nutritional_value": 7.0,
            "dietary_properties": ["Vegetarian", "Dairy-Free"],
            "description": "Portable, nutrient-dense bites perfect for on-the-go energy."
        },
        {
            "id": "recipe_1011",
            "name": "Chickpea and Vegetable Buddha Bowl",
            "meal_types": ["Lunch", "Dinner"],
            "time": 25,
            "calories": 420,
            "difficulty": "Medium",
            "popularity": 4.7,
            "nutritional_value": 9.2,
            "dietary_properties": ["Vegetarian", "Vegan", "Gluten-Free", "Dairy-Free"],
            "description": "A colorful, nutrient-packed bowl of grains, proteins, and vegetables."
        },
        {
            "id": "recipe_1012",
            "name": "Dark Chocolate Covered Strawberries",
            "meal_types": ["Snack", "Dessert"],
            "time": 15,
            "calories": 150,
            "difficulty": "Easy",
            "popularity": 4.8,
            "nutritional_value": 6.5,
            "dietary_properties": ["Vegetarian", "Gluten-Free", "Dairy-Free"],
            "description": "Juicy strawberries dipped in antioxidant-rich dark chocolate."
        },
        {
            "id": "recipe_1013",
            "name": "Baked Sweet Potato Fries",
            "meal_types": ["Snack", "Lunch", "Dinner"],
            "time": 30,
            "calories": 190,
            "difficulty": "Easy",
            "popularity": 4.6,
            "nutritional_value": 7.8,
            "dietary_properties": ["Vegetarian", "Vegan", "Gluten-Free", "Dairy-Free"],
            "description": "A healthier alternative to regular fries, full of vitamin A and fiber."
        },
        {
            "id": "recipe_1014",
            "name": "Spinach and Feta Stuffed Mushrooms",
            "meal_types": ["Snack", "Appetizer"],
            "time": 25,
            "calories": 160,
            "difficulty": "Medium",
            "popularity": 4.3,
            "nutritional_value": 7.6,
            "dietary_properties": ["Vegetarian", "Gluten-Free"],
            "description": "Savory mushroom caps filled with a flavorful spinach and feta mixture."
        },
        {
            "id": "recipe_1015",
            "name": "Mango Coconut Chia Pudding",
            "meal_types": ["Breakfast", "Snack", "Dessert"],
            "time": 10,
            "calories": 230,
            "difficulty": "Easy",
            "popularity": 4.4,
            "nutritional_value": 8.2,
            "dietary_properties": ["Vegetarian", "Vegan", "Gluten-Free", "Dairy-Free"],
            "description": "A tropical-flavored pudding that's packed with omega-3s and fiber."
        }
    ]
    
    # Filter recipes based on search criteria
    filtered_recipes = recipes_db.copy()
    
    # Filter by query
    if query:
        query = query.lower()
        filtered_recipes = [r for r in filtered_recipes if query in r["name"].lower() or query in r["description"].lower()]
    
    # Filter by meal types
    if meal_types and len(meal_types) > 0:
        filtered_recipes = [r for r in filtered_recipes if any(mt in r["meal_types"] for mt in meal_types)]
    
    # Filter by cooking time
    if max_time:
        filtered_recipes = [r for r in filtered_recipes if r["time"] <= max_time]
    
    # Filter by dietary restrictions
    if dietary_restrictions and len(dietary_restrictions) > 0:
        filtered_recipes = [r for r in filtered_recipes if all(dr in r["dietary_properties"] for dr in dietary_restrictions)]
    
    # Filter by calories
    if max_calories:
        filtered_recipes = [r for r in filtered_recipes if r["calories"] <= max_calories]
    
    # Filter by difficulty
    if difficulty:
        filtered_recipes = [r for r in filtered_recipes if r["difficulty"] == difficulty]
    
    # Sort results
    if sort_by == "Popularity":
        filtered_recipes.sort(key=lambda x: x["popularity"], reverse=True)
    elif sort_by == "Quick & Easy":
        filtered_recipes.sort(key=lambda x: x["time"])
    elif sort_by == "Nutritional Value":
        filtered_recipes.sort(key=lambda x: x["nutritional_value"], reverse=True)
    
    # Add colors for UI
    colors = ["#4CAF50", "#2196F3", "#F44336", "#FF9800", "#9C27B0", "#3F51B5"]
    for recipe in filtered_recipes:
        recipe["color"] = random.choice(colors)
    
    # Limit results
    filtered_recipes = filtered_recipes[:limit]
    
    return filtered_recipes

def get_recipe_details(recipe_id):
    """
    Get detailed information for a specific recipe
    
    Args:
        recipe_id: ID of the recipe
        
    Returns:
        Dictionary with recipe details
    """
    # Simulate processing time
    time.sleep(0.5)
    
    # Sample detailed recipes
    recipe_details = {
        "recipe_1001": {
            "id": "recipe_1001",
            "name": "Apple Cinnamon Overnight Oats",
            "description": "A delicious make-ahead breakfast that's packed with fiber and protein.",
            "prep_time": 10,
            "cook_time": 0,
            "total_time": 10,
            "servings": 1,
            "calories": 320,
            "ingredients": [
                "1/2 cup rolled oats",
                "1/2 cup milk of choice",
                "1/4 cup Greek yogurt",
                "1/2 apple, diced",
                "1/2 tsp ground cinnamon",
                "1 tbsp maple syrup or honey",
                "1 tbsp chia seeds",
                "1 tbsp chopped walnuts (optional)"
            ],
            "steps": [
                "In a jar or container, combine oats, milk, yogurt, chia seeds, and maple syrup.",
                "Stir well to combine all ingredients.",
                "Add diced apple and cinnamon, stir again.",
                "Seal container and refrigerate overnight or for at least 4 hours.",
                "When ready to eat, top with chopped walnuts if desired."
            ],
            "nutrition": {
                "calories": 320,
                "protein": 15,
                "carbs": 45,
                "fat": 10,
                "fiber": 8,
                "sugar": 18
            },
            "health_score": 85,
            "health_notes": "This recipe is high in fiber and protein, which helps keep you full longer. The apple provides natural sweetness and additional fiber, while cinnamon may help regulate blood sugar levels."
        },
        "recipe_1002": {
            "id": "recipe_1002",
            "name": "Berry Yogurt Parfait",
            "description": "A quick, protein-rich breakfast or snack with layers of yogurt, berries, and granola.",
            "prep_time": 5,
            "cook_time": 0,
            "total_time": 5,
            "servings": 1,
            "calories": 210,
            "ingredients": [
                "1 cup Greek yogurt",
                "1/2 cup mixed berries (strawberries, blueberries, raspberries)",
                "2 tbsp granola",
                "1 tsp honey or maple syrup",
                "1/2 tsp vanilla extract",
                "1 tsp chia seeds (optional)"
            ],
            "steps": [
                "Mix vanilla extract and honey into yogurt.",
                "In a glass or bowl, add a layer of yogurt.",
                "Add a layer of mixed berries.",
                "Add another layer of yogurt.",
                "Top with granola, remaining berries, and chia seeds.",
                "Drizzle with additional honey if desired."
            ],
            "nutrition": {
                "calories": 210,
                "protein": 22,
                "carbs": 25,
                "fat": 4,
                "fiber": 5,
                "sugar": 15
            },
            "health_score": 82,
            "health_notes": "This parfait is high in protein from Greek yogurt, which helps build and repair tissues. Berries are rich in antioxidants that may protect against cell damage, while granola adds a satisfying crunch with whole grains."
        },
        "recipe_1003": {
            "id": "recipe_1003",
            "name": "Avocado Toast with Poached Egg",
            "description": "Creamy avocado on toasted bread topped with a perfectly poached egg.",
            "prep_time": 5,
            "cook_time": 10,
            "total_time": 15,
            "servings": 1,
            "calories": 350,
            "ingredients": [
                "1 slice whole grain bread",
                "1/2 ripe avocado",
                "1 egg",
                "1 tsp lemon juice",
                "Salt and pepper to taste",
                "Red pepper flakes (optional)",
                "1 tbsp chopped fresh herbs (cilantro, parsley, or chives)"
            ],
            "steps": [
                "Toast the bread until golden and crisp.",
                "Scoop avocado into a bowl, add lemon juice, salt, and pepper. Mash with a fork.",
                "Spread mashed avocado on the toast.",
                "Bring a small pot of water to a gentle simmer. Add a splash of vinegar.",
                "Crack egg into a small cup, then carefully slide it into the simmering water.",
                "Cook for 3-4 minutes until whites are set but yolk is still runny.",
                "Remove egg with a slotted spoon and place on top of avocado toast.",
                "Sprinkle with red pepper flakes and fresh herbs."
            ],
            "nutrition": {
                "calories": 350,
                "protein": 14,
                "carbs": 25,
                "fat": 22,
                "fiber": 8,
                "sugar": 2
            },
            "health_score": 88,
            "health_notes": "This recipe combines healthy fats from avocado with protein from the egg, creating a balanced meal that will keep you satisfied. The whole grain bread adds fiber, which supports digestive health."
        },
        "recipe_1006": {
            "id": "recipe_1006",
            "name": "Homemade Trail Mix",
            "description": "A customizable energy-boosting mix of nuts, seeds, and dried fruits.",
            "prep_time": 5,
            "cook_time": 0,
            "total_time": 5,
            "servings": 4,
            "calories": 210,
            "ingredients": [
                "1/4 cup almonds",
                "1/4 cup walnuts",
                "2 tbsp pumpkin seeds",
                "2 tbsp sunflower seeds",
                "2 tbsp dried cranberries",
                "2 tbsp dried cherries",
                "2 tbsp dark chocolate chips",
                "1 tsp cinnamon (optional)"
            ],
            "steps": [
                "Combine all ingredients in a bowl and mix well.",
                "Store in an airtight container for up to two weeks.",
                "Portion into 1/4 cup servings when ready to eat."
            ],
            "nutrition": {
                "calories": 210,
                "protein": 6,
                "carbs": 15,
                "fat": 16,
                "fiber": 4,
                "sugar": 8
            },
            "health_score": 75,
            "health_notes": "This trail mix provides a good balance of healthy fats, protein, and carbohydrates. The nuts and seeds offer omega-3 fatty acids and vitamin E, while dried fruits add antioxidants. Portion control is important due to the calorie density."
        }
    }
    
    # Check if recipe ID exists in our database
    if recipe_id in recipe_details:
        return recipe_details[recipe_id]
    else:
        # Generate a generic recipe detail for unknown IDs
        return {
            "id": recipe_id,
            "name": f"Recipe {recipe_id.split('_')[1]}",
            "description": "A nutritious and delicious recipe for any time of day.",
            "prep_time": random.randint(5, 20),
            "cook_time": random.randint(0, 25),
            "total_time": random.randint(10, 30),
            "servings": random.randint(1, 4),
            "calories": random.randint(150, 400),
            "ingredients": [
                "Main ingredient",
                "Secondary ingredient",
                "Flavoring or spice",
                "Optional topping",
                "Liquid ingredient"
            ],
            "steps": [
                "Prepare the ingredients according to recipe instructions.",
                "Combine main ingredients in a bowl or pan.",
                "Add flavorings and mix well.",
                "Cook or prepare as directed.",
                "Serve with optional toppings."
            ],
            "nutrition": {
                "calories": random.randint(150, 400),
                "protein": random.randint(5, 25),
                "carbs": random.randint(15, 45),
                "fat": random.randint(5, 20),
                "fiber": random.randint(2, 8),
                "sugar": random.randint(2, 15)
            },
            "health_score": random.randint(60, 90),
            "health_notes": "This recipe contains a good balance of nutrients to support overall health and wellbeing."
        }
