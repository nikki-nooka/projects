import numpy as np
import cv2
from PIL import Image
import time
import random

def preprocess_image(image_array):
    """
    Preprocess image for model input
    
    Args:
        image_array: Input image as numpy array
        
    Returns:
        Preprocessed image
    """
    # Resize to standard input size
    image = cv2.resize(image_array, (224, 224))
    
    # Convert to RGB if grayscale
    if len(image.shape) == 2:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    elif image.shape[2] == 4:  # Handle RGBA
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
    
    # Normalize pixel values
    image = image.astype(np.float32) / 255.0
    
    return image

def classify_food(image):
    """
    Classify food image and determine if it's healthy
    
    In a real application, this would use a trained model.
    For this MVP, we're simulating classification results.
    
    Args:
        image: Preprocessed image array
        
    Returns:
        Dictionary with classification results
    """
    # Simulate model prediction time
    time.sleep(1)
    
    # List of healthy foods with their nutrition properties
    healthy_foods = [
        {"name": "Apple", "confidence": 92.5, "category": "Fruit"},
        {"name": "Banana", "confidence": 91.8, "category": "Fruit"},
        {"name": "Broccoli", "confidence": 88.7, "category": "Vegetable"},
        {"name": "Spinach", "confidence": 87.9, "category": "Vegetable"},
        {"name": "Greek Yogurt", "confidence": 85.2, "category": "Dairy"},
        {"name": "Salmon", "confidence": 89.3, "category": "Protein"},
        {"name": "Quinoa", "confidence": 84.5, "category": "Grain"},
        {"name": "Avocado", "confidence": 93.1, "category": "Fruit"},
        {"name": "Almonds", "confidence": 90.6, "category": "Nuts"},
        {"name": "Blueberries", "confidence": 94.7, "category": "Fruit"}
    ]
    
    # List of unhealthy foods with their nutrition properties
    unhealthy_foods = [
        {"name": "French Fries", "confidence": 95.2, "category": "Fast Food"},
        {"name": "Cheeseburger", "confidence": 94.8, "category": "Fast Food"},
        {"name": "Chocolate Cake", "confidence": 93.5, "category": "Dessert"},
        {"name": "Pizza", "confidence": 92.7, "category": "Fast Food"},
        {"name": "Ice Cream", "confidence": 91.3, "category": "Dessert"},
        {"name": "Donut", "confidence": 90.6, "category": "Dessert"},
        {"name": "Potato Chips", "confidence": 89.9, "category": "Snack"},
        {"name": "Soda", "confidence": 97.4, "category": "Beverage"},
        {"name": "Candy Bar", "confidence": 96.1, "category": "Snack"},
        {"name": "Fried Chicken", "confidence": 93.8, "category": "Fast Food"}
    ]
    
    # Randomly select a food type (healthy or unhealthy)
    # We'll use the brightness of the image to bias our selection
    # (This is just for the MVP - a real model would make proper predictions)
    avg_brightness = np.mean(image)
    
    # Brighter images are more likely to be classified as fruits/vegetables (healthy)
    is_healthy = random.random() < (0.5 + avg_brightness / 4)
    
    if is_healthy:
        food = random.choice(healthy_foods)
        food_type = "healthy"
        alternatives = []
    else:
        food = random.choice(unhealthy_foods)
        food_type = "unhealthy"
        # Suggest alternatives for unhealthy foods
        alternatives = [f["name"] for f in random.sample(healthy_foods, 3)]
    
    # Return classification results
    result = {
        "food_name": food["name"],
        "confidence": food["confidence"],
        "category": food["category"],
        "is_healthy": is_healthy,
        "food_type": food_type,
        "alternatives": alternatives
    }
    
    return result

def get_nutrition_info(food_name):
    """
    Get nutrition information for a food
    
    Args:
        food_name: Name of the food
        
    Returns:
        Dictionary with nutrition information
    """
    # Common healthy foods nutrition data
    healthy_nutrition = {
        "Apple": {
            "calories": 95,
            "protein": 0.5,
            "carbs": 25,
            "fat": 0.3,
            "fiber": 4.4,
            "sugar": 19,
            "vitamins": ["Vitamin C", "Potassium"]
        },
        "Banana": {
            "calories": 105,
            "protein": 1.3,
            "carbs": 27,
            "fat": 0.4,
            "fiber": 3.1,
            "sugar": 14,
            "vitamins": ["Vitamin B6", "Potassium"]
        },
        "Broccoli": {
            "calories": 55,
            "protein": 3.7,
            "carbs": 11,
            "fat": 0.6,
            "fiber": 5.1,
            "sugar": 2.6,
            "vitamins": ["Vitamin C", "Vitamin K", "Folate"]
        },
        "Spinach": {
            "calories": 23,
            "protein": 2.9,
            "carbs": 3.6,
            "fat": 0.4,
            "fiber": 2.2,
            "sugar": 0.4,
            "vitamins": ["Vitamin K", "Vitamin A", "Iron"]
        },
        "Greek Yogurt": {
            "calories": 130,
            "protein": 17,
            "carbs": 6,
            "fat": 4.5,
            "fiber": 0,
            "sugar": 6,
            "vitamins": ["Calcium", "Probiotics", "Vitamin B12"]
        },
        "Salmon": {
            "calories": 206,
            "protein": 22,
            "carbs": 0,
            "fat": 13,
            "fiber": 0,
            "sugar": 0,
            "vitamins": ["Omega-3", "Vitamin D", "Selenium"]
        },
        "Quinoa": {
            "calories": 120,
            "protein": 4.4,
            "carbs": 21,
            "fat": 1.9,
            "fiber": 2.8,
            "sugar": 0.9,
            "vitamins": ["Magnesium", "Phosphorus", "Manganese"]
        },
        "Avocado": {
            "calories": 160,
            "protein": 2,
            "carbs": 8.5,
            "fat": 14.7,
            "fiber": 6.7,
            "sugar": 0.7,
            "vitamins": ["Vitamin K", "Folate", "Potassium"]
        },
        "Almonds": {
            "calories": 164,
            "protein": 6,
            "carbs": 6,
            "fat": 14,
            "fiber": 3.5,
            "sugar": 1.2,
            "vitamins": ["Vitamin E", "Magnesium", "Riboflavin"]
        },
        "Blueberries": {
            "calories": 84,
            "protein": 1.1,
            "carbs": 21,
            "fat": 0.5,
            "fiber": 3.6,
            "sugar": 15,
            "vitamins": ["Vitamin K", "Vitamin C", "Manganese"]
        }
    }
    
    # Common unhealthy foods nutrition data
    unhealthy_nutrition = {
        "French Fries": {
            "calories": 365,
            "protein": 3.4,
            "carbs": 48,
            "fat": 17,
            "fiber": 4.5,
            "sugar": 0.5,
            "concerns": ["High sodium", "Trans fats", "Acrylamide"]
        },
        "Cheeseburger": {
            "calories": 520,
            "protein": 25,
            "carbs": 40,
            "fat": 30,
            "fiber": 2,
            "sugar": 7,
            "concerns": ["Saturated fat", "Sodium", "Processed meat"]
        },
        "Chocolate Cake": {
            "calories": 395,
            "protein": 5,
            "carbs": 55,
            "fat": 18,
            "fiber": 2,
            "sugar": 36,
            "concerns": ["Added sugar", "Refined flour", "Trans fats"]
        },
        "Pizza": {
            "calories": 285,
            "protein": 12,
            "carbs": 39,
            "fat": 10,
            "fiber": 2.5,
            "sugar": 3.8,
            "concerns": ["Refined carbs", "Sodium", "Processed meat"]
        },
        "Ice Cream": {
            "calories": 273,
            "protein": 4.6,
            "carbs": 31,
            "fat": 14.5,
            "fiber": 0.7,
            "sugar": 28,
            "concerns": ["Added sugar", "Saturated fat", "Low nutrients"]
        },
        "Donut": {
            "calories": 253,
            "protein": 4,
            "carbs": 31,
            "fat": 14,
            "fiber": 1,
            "sugar": 10,
            "concerns": ["Trans fats", "Added sugar", "Refined flour"]
        },
        "Potato Chips": {
            "calories": 152,
            "protein": 2,
            "carbs": 15,
            "fat": 10,
            "fiber": 1.3,
            "sugar": 0.1,
            "concerns": ["Acrylamide", "Sodium", "Low nutrients"]
        },
        "Soda": {
            "calories": 140,
            "protein": 0,
            "carbs": 39,
            "fat": 0,
            "fiber": 0,
            "sugar": 39,
            "concerns": ["Added sugar", "No nutrients", "Tooth decay"]
        },
        "Candy Bar": {
            "calories": 235,
            "protein": 3,
            "carbs": 32,
            "fat": 11,
            "fiber": 1.5,
            "sugar": 29,
            "concerns": ["Added sugar", "Saturated fat", "Low nutrients"]
        },
        "Fried Chicken": {
            "calories": 320,
            "protein": 26,
            "carbs": 16,
            "fat": 19,
            "fiber": 0.9,
            "sugar": 0.3,
            "concerns": ["Saturated fat", "Sodium", "Trans fats"]
        }
    }
    
    # Check if food is in our database
    if food_name in healthy_nutrition:
        nutrition = healthy_nutrition[food_name]
        nutrition["health_score"] = random.randint(75, 95)
        nutrition["benefits"] = ["Nutrient-dense", "High in vitamins", "Supports overall health"]
    elif food_name in unhealthy_nutrition:
        nutrition = unhealthy_nutrition[food_name]
        nutrition["health_score"] = random.randint(20, 45)
        nutrition["risks"] = ["High in calories", "Low nutrient value", "May contribute to health issues"]
    else:
        # Generate default nutrition info for unknown foods
        is_healthy = random.random() > 0.5
        if is_healthy:
            nutrition = {
                "calories": random.randint(50, 200),
                "protein": round(random.uniform(1.0, 10.0), 1),
                "carbs": round(random.uniform(5.0, 25.0), 1),
                "fat": round(random.uniform(0.5, 5.0), 1),
                "fiber": round(random.uniform(1.0, 5.0), 1),
                "sugar": round(random.uniform(0.5, 10.0), 1),
                "health_score": random.randint(65, 85),
                "vitamins": ["Vitamin " + random.choice(["A", "B", "C", "D", "E", "K"]) for _ in range(2)],
                "benefits": ["Nutrient-dense", "High in vitamins", "Supports overall health"]
            }
        else:
            nutrition = {
                "calories": random.randint(200, 500),
                "protein": round(random.uniform(2.0, 15.0), 1),
                "carbs": round(random.uniform(20.0, 50.0), 1),
                "fat": round(random.uniform(10.0, 30.0), 1),
                "fiber": round(random.uniform(0.0, 2.0), 1),
                "sugar": round(random.uniform(5.0, 30.0), 1),
                "health_score": random.randint(20, 50),
                "concerns": ["High in calories", "Low nutrient value", "May contribute to health issues"]
            }
    
    nutrition["food_name"] = food_name
    return nutrition
