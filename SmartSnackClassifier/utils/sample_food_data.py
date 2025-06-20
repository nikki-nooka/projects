"""
Sample food data for Smart Snack Predictor application.
This file contains structured data for food classification, nutrition information,
and recommendation features.
"""

# Sample healthy foods with their nutritional properties
HEALTHY_FOODS = [
    {
        "name": "Apple",
        "confidence": 92.5,
        "category": "Fruit",
        "calories": 95,
        "protein": 0.5,
        "carbs": 25,
        "fat": 0.3,
        "fiber": 4.4,
        "sugar": 19,
        "vitamins": ["Vitamin C", "Potassium"],
        "benefits": ["Supports heart health", "High in antioxidants", "Promotes gut health"],
        "image_description": "Red apple with green leaf"
    },
    {
        "name": "Banana",
        "confidence": 91.8,
        "category": "Fruit",
        "calories": 105,
        "protein": 1.3,
        "carbs": 27,
        "fat": 0.4,
        "fiber": 3.1,
        "sugar": 14,
        "vitamins": ["Vitamin B6", "Potassium", "Vitamin C"],
        "benefits": ["Supports muscle function", "Aids in digestion", "Provides quick energy"],
        "image_description": "Yellow banana"
    },
    {
        "name": "Broccoli",
        "confidence": 88.7,
        "category": "Vegetable",
        "calories": 55,
        "protein": 3.7,
        "carbs": 11,
        "fat": 0.6,
        "fiber": 5.1,
        "sugar": 2.6,
        "vitamins": ["Vitamin C", "Vitamin K", "Folate", "Vitamin A"],
        "benefits": ["Supports immune function", "Anti-inflammatory properties", "May help prevent cancer"],
        "image_description": "Fresh broccoli florets"
    },
    {
        "name": "Spinach",
        "confidence": 87.9,
        "category": "Vegetable",
        "calories": 23,
        "protein": 2.9,
        "carbs": 3.6,
        "fat": 0.4,
        "fiber": 2.2,
        "sugar": 0.4,
        "vitamins": ["Vitamin K", "Vitamin A", "Vitamin C", "Iron", "Folate"],
        "benefits": ["Supports eye health", "Reduces oxidative stress", "Promotes heart health"],
        "image_description": "Fresh green spinach leaves"
    },
    {
        "name": "Greek Yogurt",
        "confidence": 85.2,
        "category": "Dairy",
        "calories": 130,
        "protein": 17,
        "carbs": 6,
        "fat": 4.5,
        "fiber": 0,
        "sugar": 6,
        "vitamins": ["Calcium", "Vitamin B12", "Potassium"],
        "benefits": ["Supports gut health", "Helps build muscle", "Promotes bone health"],
        "image_description": "Creamy white Greek yogurt in a bowl"
    },
    {
        "name": "Salmon",
        "confidence": 89.3,
        "category": "Protein",
        "calories": 206,
        "protein": 22,
        "carbs": 0,
        "fat": 13,
        "fiber": 0,
        "sugar": 0,
        "vitamins": ["Omega-3 fatty acids", "Vitamin D", "Vitamin B12", "Selenium"],
        "benefits": ["Reduces inflammation", "Supports brain function", "Promotes heart health"],
        "image_description": "Fresh salmon fillet"
    },
    {
        "name": "Quinoa",
        "confidence": 84.5,
        "category": "Grain",
        "calories": 120,
        "protein": 4.4,
        "carbs": 21,
        "fat": 1.9,
        "fiber": 2.8,
        "sugar": 0.9,
        "vitamins": ["Magnesium", "Phosphorus", "Manganese", "Folate"],
        "benefits": ["Complete protein source", "High in fiber", "Supports digestive health"],
        "image_description": "Cooked quinoa in a bowl"
    },
    {
        "name": "Avocado",
        "confidence": 93.1,
        "category": "Fruit",
        "calories": 160,
        "protein": 2,
        "carbs": 8.5,
        "fat": 14.7,
        "fiber": 6.7,
        "sugar": 0.7,
        "vitamins": ["Vitamin K", "Folate", "Vitamin C", "Potassium"],
        "benefits": ["Promotes heart health", "Supports weight management", "Improves digestion"],
        "image_description": "Halved avocado showing pit"
    },
    {
        "name": "Almonds",
        "confidence": 90.6,
        "category": "Nuts",
        "calories": 164,
        "protein": 6,
        "carbs": 6,
        "fat": 14,
        "fiber": 3.5,
        "sugar": 1.2,
        "vitamins": ["Vitamin E", "Magnesium", "Riboflavin", "Manganese"],
        "benefits": ["Helps lower cholesterol", "Supports brain function", "Promotes skin health"],
        "image_description": "Raw almonds scattered"
    },
    {
        "name": "Blueberries",
        "confidence": 94.7,
        "category": "Fruit",
        "calories": 84,
        "protein": 1.1,
        "carbs": 21,
        "fat": 0.5,
        "fiber": 3.6,
        "sugar": 15,
        "vitamins": ["Vitamin K", "Vitamin C", "Manganese"],
        "benefits": ["Powerful antioxidant properties", "Supports brain function", "May improve memory"],
        "image_description": "Fresh blueberries"
    },
    {
        "name": "Sweet Potato",
        "confidence": 88.3,
        "category": "Vegetable",
        "calories": 112,
        "protein": 2,
        "carbs": 26,
        "fat": 0.1,
        "fiber": 3.8,
        "sugar": 5.4,
        "vitamins": ["Vitamin A", "Vitamin C", "Manganese", "Potassium"],
        "benefits": ["Supports eye health", "Boosts immune function", "Promotes gut health"],
        "image_description": "Orange sweet potato"
    },
    {
        "name": "Lentils",
        "confidence": 86.9,
        "category": "Legume",
        "calories": 116,
        "protein": 9,
        "carbs": 20,
        "fat": 0.4,
        "fiber": 8,
        "sugar": 1.8,
        "vitamins": ["Folate", "Iron", "Potassium", "Zinc"],
        "benefits": ["Supports heart health", "Stabilizes blood sugar", "High in plant protein"],
        "image_description": "Cooked brown lentils"
    },
    {
        "name": "Oatmeal",
        "confidence": 91.5,
        "category": "Grain",
        "calories": 150,
        "protein": 5,
        "carbs": 27,
        "fat": 2.5,
        "fiber": 4,
        "sugar": 1,
        "vitamins": ["Manganese", "Phosphorus", "Magnesium", "Vitamin B1"],
        "benefits": ["Lowers cholesterol levels", "Helps control blood sugar", "Promotes feeling of fullness"],
        "image_description": "Bowl of cooked oatmeal"
    },
    {
        "name": "Eggs",
        "confidence": 92.2,
        "category": "Protein",
        "calories": 78,
        "protein": 6.3,
        "carbs": 0.6,
        "fat": 5.3,
        "fiber": 0,
        "sugar": 0.6,
        "vitamins": ["Vitamin B12", "Vitamin D", "Choline", "Selenium"],
        "benefits": ["Complete protein source", "Supports brain health", "Promotes eye health"],
        "image_description": "Two brown eggs"
    },
    {
        "name": "Kale",
        "confidence": 89.4,
        "category": "Vegetable",
        "calories": 33,
        "protein": 3,
        "carbs": 6,
        "fat": 0.5,
        "fiber": 2,
        "sugar": 1.6,
        "vitamins": ["Vitamin K", "Vitamin C", "Vitamin A", "Manganese"],
        "benefits": ["Anti-inflammatory properties", "Supports heart health", "Loaded with antioxidants"],
        "image_description": "Fresh kale leaves"
    }
]

# Sample unhealthy foods with their nutritional properties
UNHEALTHY_FOODS = [
    {
        "name": "French Fries",
        "confidence": 95.2,
        "category": "Fast Food",
        "calories": 365,
        "protein": 3.4,
        "carbs": 48,
        "fat": 17,
        "fiber": 4.5,
        "sugar": 0.5,
        "concerns": ["High sodium", "Trans fats", "Acrylamide formation", "High glycemic index"],
        "healthier_alternatives": ["Baked Sweet Potato Fries", "Air-fried Vegetable Sticks", "Roasted Potato Wedges"],
        "image_description": "Golden fried french fries"
    },
    {
        "name": "Cheeseburger",
        "confidence": 94.8,
        "category": "Fast Food",
        "calories": 520,
        "protein": 25,
        "carbs": 40,
        "fat": 30,
        "fiber": 2,
        "sugar": 7,
        "concerns": ["Saturated fat", "High sodium", "Processed meat", "Refined carbohydrates"],
        "healthier_alternatives": ["Turkey Burger on Whole Grain Bun", "Portobello Mushroom Burger", "Bean Burger"],
        "image_description": "Cheeseburger with lettuce and tomato"
    },
    {
        "name": "Chocolate Cake",
        "confidence": 93.5,
        "category": "Dessert",
        "calories": 395,
        "protein": 5,
        "carbs": 55,
        "fat": 18,
        "fiber": 2,
        "sugar": 36,
        "concerns": ["Added sugar", "Refined flour", "Saturated fat", "Low nutrient density"],
        "healthier_alternatives": ["Dark Chocolate Avocado Mousse", "Greek Yogurt Chocolate Pudding", "Fruit-based Dessert"],
        "image_description": "Slice of chocolate cake with frosting"
    },
    {
        "name": "Pizza",
        "confidence": 92.7,
        "category": "Fast Food",
        "calories": 285,
        "protein": 12,
        "carbs": 39,
        "fat": 10,
        "fiber": 2.5,
        "sugar": 3.8,
        "concerns": ["Refined carbs", "High sodium", "Processed meat", "Saturated fat"],
        "healthier_alternatives": ["Cauliflower Crust Veggie Pizza", "Whole Grain Pita Pizza", "Portobello Mushroom Pizza Cups"],
        "image_description": "Slice of pepperoni pizza"
    },
    {
        "name": "Ice Cream",
        "confidence": 91.3,
        "category": "Dessert",
        "calories": 273,
        "protein": 4.6,
        "carbs": 31,
        "fat": 14.5,
        "fiber": 0.7,
        "sugar": 28,
        "concerns": ["Added sugar", "Saturated fat", "Low nutrient density", "Artificial additives"],
        "healthier_alternatives": ["Frozen Banana Ice Cream", "Greek Yogurt Berry Freeze", "Chia Pudding"],
        "image_description": "Scoop of vanilla ice cream"
    },
    {
        "name": "Donut",
        "confidence": 90.6,
        "category": "Dessert",
        "calories": 253,
        "protein": 4,
        "carbs": 31,
        "fat": 14,
        "fiber": 1,
        "sugar": 10,
        "concerns": ["Trans fats", "Added sugar", "Refined flour", "Deep fried"],
        "healthier_alternatives": ["Baked Whole Grain Donuts", "Fruit and Yogurt Parfait", "Oatmeal Energy Bites"],
        "image_description": "Glazed donut with sprinkles"
    },
    {
        "name": "Potato Chips",
        "confidence": 89.9,
        "category": "Snack",
        "calories": 152,
        "protein": 2,
        "carbs": 15,
        "fat": 10,
        "fiber": 1.3,
        "sugar": 0.1,
        "concerns": ["Acrylamide", "High sodium", "Low nutrient density", "Refined carbohydrates"],
        "healthier_alternatives": ["Air-popped Popcorn", "Baked Kale Chips", "Roasted Chickpeas"],
        "image_description": "Potato chips in a bowl"
    },
    {
        "name": "Soda",
        "confidence": 97.4,
        "category": "Beverage",
        "calories": 140,
        "protein": 0,
        "carbs": 39,
        "fat": 0,
        "fiber": 0,
        "sugar": 39,
        "concerns": ["Added sugar", "No nutrients", "Tooth decay", "Weight gain"],
        "healthier_alternatives": ["Sparkling Water with Fruit", "Herbal Tea", "Infused Water"],
        "image_description": "Glass of dark soda with ice"
    },
    {
        "name": "Candy Bar",
        "confidence": 96.1,
        "category": "Snack",
        "calories": 235,
        "protein": 3,
        "carbs": 32,
        "fat": 11,
        "fiber": 1.5,
        "sugar": 29,
        "concerns": ["Added sugar", "Saturated fat", "Low nutrient density", "Artificial ingredients"],
        "healthier_alternatives": ["Dark Chocolate with Nuts", "Fruit and Nut Mix", "Energy Ball"],
        "image_description": "Chocolate candy bar"
    },
    {
        "name": "Fried Chicken",
        "confidence": 93.8,
        "category": "Fast Food",
        "calories": 320,
        "protein": 26,
        "carbs": 16,
        "fat": 19,
        "fiber": 0.9,
        "sugar": 0.3,
        "concerns": ["Saturated fat", "High sodium", "Trans fats", "Advanced glycation end products"],
        "healthier_alternatives": ["Baked Chicken with Herbs", "Air-fried Chicken", "Grilled Chicken Breast"],
        "image_description": "Fried chicken pieces"
    },
    {
        "name": "Milkshake",
        "confidence": 91.7,
        "category": "Beverage",
        "calories": 420,
        "protein": 9,
        "carbs": 63,
        "fat": 15,
        "fiber": 0.5,
        "sugar": 56,
        "concerns": ["Added sugar", "Saturated fat", "Low nutrient density", "High calorie"],
        "healthier_alternatives": ["Fruit and Yogurt Smoothie", "Protein Shake", "Banana and Nut Butter Smoothie"],
        "image_description": "Strawberry milkshake with whipped cream"
    },
    {
        "name": "White Bread",
        "confidence": 89.1,
        "category": "Grain",
        "calories": 98,
        "protein": 3.3,
        "carbs": 18,
        "fat": 0.8,
        "fiber": 0.8,
        "sugar": 1.6,
        "concerns": ["Refined flour", "Low fiber", "High glycemic index", "Limited nutrients"],
        "healthier_alternatives": ["Whole Grain Bread", "Sprouted Grain Bread", "Ezekiel Bread"],
        "image_description": "Slices of white bread"
    },
    {
        "name": "Bacon",
        "confidence": 95.3,
        "category": "Protein",
        "calories": 129,
        "protein": 9,
        "carbs": 0.4,
        "fat": 10,
        "fiber": 0,
        "sugar": 0,
        "concerns": ["Processed meat", "High sodium", "Saturated fat", "Potential carcinogens"],
        "healthier_alternatives": ["Turkey Bacon", "Tempeh Bacon", "Avocado Slices"],
        "image_description": "Cooked bacon strips"
    },
    {
        "name": "Instant Noodles",
        "confidence": 94.2,
        "category": "Processed Food",
        "calories": 380,
        "protein": 7,
        "carbs": 54,
        "fat": 14,
        "fiber": 2,
        "sugar": 1,
        "concerns": ["High sodium", "Refined carbohydrates", "Preservatives", "MSG"],
        "healthier_alternatives": ["Whole Grain Pasta", "Zucchini Noodles", "Rice Noodles with Homemade Broth"],
        "image_description": "Bowl of instant noodles"
    },
    {
        "name": "Energy Drink",
        "confidence": 96.8,
        "category": "Beverage",
        "calories": 160,
        "protein": 0,
        "carbs": 40,
        "fat": 0,
        "fiber": 0,
        "sugar": 38,
        "concerns": ["Added sugar", "High caffeine", "Artificial ingredients", "Potential heart issues"],
        "healthier_alternatives": ["Green Tea", "Coconut Water", "Fruit-infused Water"],
        "image_description": "Can of energy drink"
    }
]

# Mapping of moods to recommended food types
MOOD_FOOD_MAPPING = {
    "Happy": [
        {
            "food_type": "Dark Chocolate",
            "reason": "Contains compounds that trigger the release of endorphins",
            "nutrients": "Antioxidants, Magnesium"
        },
        {
            "food_type": "Berries",
            "reason": "The natural sweetness and bright colors enhance positive feelings",
            "nutrients": "Vitamin C, Antioxidants"
        },
        {
            "food_type": "Nuts",
            "reason": "The crunch and healthy fats provide satisfaction",
            "nutrients": "Vitamin E, Healthy Fats, Protein"
        }
    ],
    "Sad": [
        {
            "food_type": "Fatty Fish",
            "reason": "Omega-3 fatty acids support brain health and mood regulation",
            "nutrients": "Omega-3s, Vitamin D, Protein"
        },
        {
            "food_type": "Whole Grains",
            "reason": "Complex carbs increase serotonin levels which elevate mood",
            "nutrients": "B Vitamins, Fiber, Magnesium"
        },
        {
            "food_type": "Fermented Foods",
            "reason": "Support gut health which is linked to emotional well-being",
            "nutrients": "Probiotics, B Vitamins"
        }
    ],
    "Energetic": [
        {
            "food_type": "Fresh Fruit",
            "reason": "Natural sugars provide immediate energy",
            "nutrients": "Vitamins, Natural Sugars, Fiber"
        },
        {
            "food_type": "Nuts and Seeds",
            "reason": "Protein and healthy fats provide sustained energy",
            "nutrients": "Protein, Healthy Fats, Magnesium"
        },
        {
            "food_type": "Whole Grains",
            "reason": "Complex carbs release energy slowly",
            "nutrients": "B Vitamins, Fiber, Iron"
        }
    ],
    "Tired": [
        {
            "food_type": "Leafy Greens",
            "reason": "Iron helps combat fatigue and boosts energy",
            "nutrients": "Iron, Folate, Vitamin K"
        },
        {
            "food_type": "Lean Protein",
            "reason": "Supports muscle function and provides steady energy",
            "nutrients": "Protein, B Vitamins, Iron"
        },
        {
            "food_type": "Hydrating Foods",
            "reason": "Dehydration can cause fatigue, these foods help rehydrate",
            "nutrients": "Electrolytes, Water, Vitamins"
        }
    ],
    "Stressed": [
        {
            "food_type": "Herbal Tea",
            "reason": "Contains compounds that promote relaxation",
            "nutrients": "Antioxidants, Anti-inflammatory compounds"
        },
        {
            "food_type": "Dark Leafy Greens",
            "reason": "Rich in magnesium which helps regulate stress response",
            "nutrients": "Magnesium, Folate, Vitamin C"
        },
        {
            "food_type": "Citrus Fruits",
            "reason": "Vitamin C may help lower stress hormones",
            "nutrients": "Vitamin C, Flavonoids"
        }
    ],
    "Focused": [
        {
            "food_type": "Blueberries",
            "reason": "Antioxidants improve brain function and memory",
            "nutrients": "Antioxidants, Vitamin K"
        },
        {
            "food_type": "Fatty Fish",
            "reason": "Omega-3 fatty acids support brain health",
            "nutrients": "Omega-3s, Protein, Vitamin D"
        },
        {
            "food_type": "Eggs",
            "reason": "Choline supports brain health and cognitive function",
            "nutrients": "Choline, Protein, B Vitamins"
        }
    ],
    "Relaxed": [
        {
            "food_type": "Warm Oatmeal",
            "reason": "Comforting and increases serotonin levels",
            "nutrients": "Complex Carbs, Fiber, B Vitamins"
        },
        {
            "food_type": "Chamomile Tea",
            "reason": "Contains compounds that promote relaxation",
            "nutrients": "Antioxidants, Anti-inflammatory compounds"
        },
        {
            "food_type": "Bananas",
            "reason": "Contains magnesium and potassium which help relax muscles",
            "nutrients": "Magnesium, Potassium, Vitamin B6"
        }
    ]
}

# Common ingredients and their nutritional benefits
INGREDIENT_BENEFITS = {
    "Apple": {
        "benefits": ["Supports heart health", "Aids digestion", "Rich in antioxidants"],
        "nutrients": ["Fiber", "Vitamin C", "Potassium"]
    },
    "Banana": {
        "benefits": ["Supports heart health", "Aids exercise recovery", "Improves digestion"],
        "nutrients": ["Potassium", "Vitamin B6", "Fiber"]
    },
    "Spinach": {
        "benefits": ["Supports eye health", "Maintains healthy blood pressure", "Strengthens bones"],
        "nutrients": ["Vitamin K", "Iron", "Vitamin A"]
    },
    "Avocado": {
        "benefits": ["Supports heart health", "Improves digestion", "Nourishes skin"],
        "nutrients": ["Healthy fats", "Fiber", "Potassium"]
    },
    "Salmon": {
        "benefits": ["Reduces inflammation", "Supports brain health", "Protects heart health"],
        "nutrients": ["Omega-3 fatty acids", "Protein", "Vitamin D"]
    },
    "Blueberries": {
        "benefits": ["Improves brain function", "Fights inflammation", "Supports heart health"],
        "nutrients": ["Antioxidants", "Vitamin K", "Vitamin C"]
    },
    "Oats": {
        "benefits": ["Lowers cholesterol", "Stabilizes blood sugar", "Supports digestive health"],
        "nutrients": ["Fiber", "Manganese", "Phosphorus"]
    },
    "Greek Yogurt": {
        "benefits": ["Improves gut health", "Supports muscle growth", "Strengthens bones"],
        "nutrients": ["Protein", "Calcium", "Probiotics"]
    },
    "Almonds": {
        "benefits": ["Supports heart health", "Aids weight management", "Improves skin health"],
        "nutrients": ["Vitamin E", "Magnesium", "Healthy fats"]
    },
    "Eggs": {
        "benefits": ["Supports brain health", "Builds muscle", "Provides sustainable energy"],
        "nutrients": ["Protein", "Choline", "Vitamin B12"]
    },
    "Quinoa": {
        "benefits": ["Supports digestive health", "Helps manage weight", "Provides sustained energy"],
        "nutrients": ["Complete protein", "Fiber", "Magnesium"]
    },
    "Sweet Potato": {
        "benefits": ["Improves eye health", "Boosts immune system", "Supports digestive health"],
        "nutrients": ["Vitamin A", "Vitamin C", "Fiber"]
    },
    "Broccoli": {
        "benefits": ["Supports detoxification", "Reduces inflammation", "Supports heart health"],
        "nutrients": ["Vitamin C", "Vitamin K", "Fiber"]
    }
}

# Sample recipe categories for organization
RECIPE_CATEGORIES = [
    "Quick & Easy",
    "High Protein",
    "Low Calorie",
    "Vegetarian",
    "Vegan",
    "Gluten-Free",
    "Dairy-Free",
    "Breakfast",
    "Lunch",
    "Dinner",
    "Snacks",
    "Desserts",
    "Kid-Friendly",
    "Mood-Boosting",
    "Energy-Enhancing"
]

# Health facts for display in the application
HEALTH_FACTS = [
    "Eating protein-rich foods can help you feel full longer.",
    "Dark green vegetables are rich in nutrients that support immune function.",
    "Berries contain antioxidants that may improve brain function.",
    "Whole grains provide sustained energy and support digestive health.",
    "Staying hydrated helps maintain energy levels throughout the day.",
    "Plant-based proteins can be just as effective as animal proteins for muscle building.",
    "Eating a variety of colorful foods helps ensure you get a wide range of nutrients.",
    "Fermented foods support gut health, which is linked to overall wellbeing.",
    "Adding healthy fats to meals helps with absorption of fat-soluble vitamins.",
    "Consuming fiber-rich foods can help regulate blood sugar levels.",
    "Eating mindfully can improve digestion and prevent overeating.",
    "Including omega-3 fatty acids in your diet supports brain and heart health.",
    "Vitamin D helps with calcium absorption for stronger bones.",
    "Magnesium-rich foods may help reduce stress and improve sleep quality.",
    "Zinc supports immune function and wound healing."
]

# Cooking tips for recipe pages
COOKING_TIPS = [
    "Prep all ingredients before you start cooking to make the process smoother.",
    "A sharp knife is safer and more efficient than a dull one.",
    "Adding salt to cooking water enhances the flavor of grains and pasta.",
    "Let meats rest after cooking to retain their juices.",
    "Toast spices before using them to enhance their flavor.",
    "Use fresh herbs at the end of cooking for maximum flavor.",
    "Save vegetable scraps to make homemade stock.",
    "Room temperature ingredients blend better than cold ones.",
    "Store fresh herbs in water like flowers to make them last longer.",
    "Taste and adjust seasoning as you cook.",
    "Invest in a kitchen thermometer for perfectly cooked meats.",
    "Don't overcrowd the pan when sautéing to ensure even cooking.",
    "Let baked goods cool completely before slicing.",
    "Use a timer to avoid overcooking.",
    "Clean as you go to make post-cooking cleanup easier."
]
