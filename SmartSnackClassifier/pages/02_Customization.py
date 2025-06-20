import streamlit as st
import time
import numpy as np
from utils.mood_recommender import get_mood_recommendations
from utils.recipe_recommender import get_recipe_by_ingredients

# Set page configuration
st.set_page_config(
    page_title="Customization - Smart Snack Predictor",
    page_icon="🎨",
    layout="wide",
)

# Page Title
st.title("🎨 Customize Your Experience")
st.markdown("Personalize your snack recommendations based on preferences, dietary needs, and mood.")

# Import the log_user_activity function from the database module
from utils.database import log_user_activity, get_user_preferences, update_user_preferences

# Function to log activity
def log_activity(activity_type, details):
    if "user" in st.session_state and st.session_state.user["logged_in"]:
        # Log to database if user is logged in
        user_id = st.session_state.user.get("id")
        if user_id:
            log_user_activity(user_id, activity_type, details)

# Initialize session state for preferences
if "dietary_preferences" not in st.session_state:
    st.session_state.dietary_preferences = {
        "vegetarian": False,
        "vegan": False,
        "gluten_free": False,
        "dairy_free": False,
        "nut_free": False,
    }

if "taste_preferences" not in st.session_state:
    st.session_state.taste_preferences = {
        "sweet": 50,
        "savory": 50,
        "spicy": 50,
    }

if "health_goals" not in st.session_state:
    st.session_state.health_goals = {
        "weight_loss": False,
        "muscle_gain": False,
        "heart_health": False,
        "energy_boost": False,
        "digestive_health": False,
    }

if "ingredients" not in st.session_state:
    st.session_state.ingredients = []
    
if "allergies" not in st.session_state:
    st.session_state.allergies = ""

# Load user preferences from database if user is logged in
if "user" in st.session_state and st.session_state.user.get("logged_in") and st.session_state.user.get("id"):
    user_id = st.session_state.user.get("id")
    
    # Get user preferences from database
    user_prefs = get_user_preferences(user_id)
    
    if user_prefs:
        # Load dietary restrictions
        if "dietary_restrictions" in user_prefs and user_prefs["dietary_restrictions"]:
            try:
                dietary = user_prefs["dietary_restrictions"]
                if isinstance(dietary, dict):
                    st.session_state.dietary_preferences.update(dietary)
            except:
                pass
                
        # Load health goals
        if "health_goals" in user_prefs and user_prefs["health_goals"]:
            try:
                goals = user_prefs["health_goals"]
                if isinstance(goals, dict):
                    st.session_state.health_goals.update(goals)
            except:
                pass
                
        # Load favorite foods (use as ingredients)
        if "favorite_foods" in user_prefs and user_prefs["favorite_foods"]:
            try:
                foods = user_prefs["favorite_foods"]
                if isinstance(foods, list):
                    st.session_state.ingredients = foods
            except:
                pass

# Create main sections
tab1, tab2, tab3 = st.tabs(["😊 Mood-Based", "🥗 Dietary Preferences", "🧪 Ingredient Selection"])

with tab1:
    st.markdown("### Mood-Based Recommendations")
    st.write("Get snack recommendations based on how you're feeling right now.")
    
    # Mood selection
    mood_options = ["Happy", "Sad", "Energetic", "Tired", "Stressed", "Relaxed", "Focused"]
    selected_mood = st.selectbox("How are you feeling today?", mood_options)
    
    # Time of day
    time_options = ["Morning", "Afternoon", "Evening", "Late Night"]
    selected_time = st.selectbox("What time of day is it?", time_options)
    
    # Intensity slider
    mood_intensity = st.slider("How intensely are you feeling this way?", 1, 10, 5)
    
    if st.button("Get Mood-Based Recommendations", key="mood_rec_btn"):
        with st.spinner("Analyzing your mood..."):
            # Get recommendations based on mood
            recommendations = get_mood_recommendations(selected_mood, intensity=mood_intensity, time_of_day=selected_time)
            
            # Display recommendations
            st.success(f"Based on your {selected_mood.lower()} mood, we recommend these snacks:")
            
            # Create columns for recommendations
            rec_cols = st.columns(3)
            
            for i, rec in enumerate(recommendations[:3]):
                with rec_cols[i]:
                    st.markdown(f"### {rec['name']}")
                    st.markdown(f"**Why it works:** {rec['reason']}")
                    st.markdown(f"**Nutrients:** {rec['nutrients']}")
                    if st.button(f"Get Recipe for {rec['name']}", key=f"recipe_btn_{i}"):
                        st.session_state.recipe_search = rec['name']
                        # Also set the current_recipe with the recipe id to display details directly
                        st.session_state.current_recipe = rec['id']
                        st.switch_page("pages/03_Recipes.py")
            
            # Log the activity
            log_activity("mood_recommendation", {
                "mood": selected_mood,
                "time": selected_time,
                "intensity": mood_intensity,
                "recommendations": [r['name'] for r in recommendations[:3]]
            })

with tab2:
    st.markdown("### Dietary Preferences and Health Goals")
    
    # Create two columns
    pref_col1, pref_col2 = st.columns(2)
    
    with pref_col1:
        st.subheader("Dietary Restrictions")
        
        # Dietary preferences checkboxes
        st.session_state.dietary_preferences["vegetarian"] = st.checkbox(
            "Vegetarian", value=st.session_state.dietary_preferences["vegetarian"])
        
        st.session_state.dietary_preferences["vegan"] = st.checkbox(
            "Vegan", value=st.session_state.dietary_preferences["vegan"])
        
        st.session_state.dietary_preferences["gluten_free"] = st.checkbox(
            "Gluten-Free", value=st.session_state.dietary_preferences["gluten_free"])
        
        st.session_state.dietary_preferences["dairy_free"] = st.checkbox(
            "Dairy-Free", value=st.session_state.dietary_preferences["dairy_free"])
        
        st.session_state.dietary_preferences["nut_free"] = st.checkbox(
            "Nut-Free", value=st.session_state.dietary_preferences["nut_free"])
        
        # Taste preference sliders
        st.subheader("Taste Preferences")
        
        st.session_state.taste_preferences["sweet"] = st.slider(
            "Sweet", 0, 100, st.session_state.taste_preferences["sweet"])
        
        st.session_state.taste_preferences["savory"] = st.slider(
            "Savory", 0, 100, st.session_state.taste_preferences["savory"])
        
        st.session_state.taste_preferences["spicy"] = st.slider(
            "Spicy", 0, 100, st.session_state.taste_preferences["spicy"])
    
    with pref_col2:
        st.subheader("Health Goals")
        
        # Health goals checkboxes
        st.session_state.health_goals["weight_loss"] = st.checkbox(
            "Weight Loss", value=st.session_state.health_goals["weight_loss"])
        
        st.session_state.health_goals["muscle_gain"] = st.checkbox(
            "Muscle Gain", value=st.session_state.health_goals["muscle_gain"])
        
        st.session_state.health_goals["heart_health"] = st.checkbox(
            "Heart Health", value=st.session_state.health_goals["heart_health"])
        
        st.session_state.health_goals["energy_boost"] = st.checkbox(
            "Energy Boost", value=st.session_state.health_goals["energy_boost"])
        
        st.session_state.health_goals["digestive_health"] = st.checkbox(
            "Digestive Health", value=st.session_state.health_goals["digestive_health"])
        
        # Allergy input
        st.subheader("Allergies")
        allergies = st.text_input("List any food allergies (comma-separated)")
    
    # Save preferences button
    if st.button("Save Preferences"):
        # Save preferences to session state
        st.session_state.allergies = allergies
        
        # Save to database if user is logged in
        if "user" in st.session_state and st.session_state.user.get("logged_in") and st.session_state.user.get("id"):
            user_id = st.session_state.user.get("id")
            
            # Prepare preferences object
            preferences = {
                "dietary_restrictions": st.session_state.dietary_preferences,
                "health_goals": st.session_state.health_goals,
                "favorite_foods": st.session_state.ingredients,
                "disliked_foods": allergies.split(",") if allergies else []
            }
            
            # Update preferences in database
            success = update_user_preferences(user_id, preferences)
            
            if success:
                st.success("Your preferences have been saved to your profile!")
            else:
                st.error("There was an error saving your preferences. Please try again.")
        else:
            st.warning("Please log in to save your preferences permanently.")
            st.success("Preferences have been saved for this session only.")
        
        # Log the activity
        log_activity("preferences_updated", {
            "dietary": st.session_state.dietary_preferences,
            "taste": st.session_state.taste_preferences,
            "health_goals": st.session_state.health_goals,
            "allergies": allergies if allergies else "None"
        })

with tab3:
    st.markdown("### Ingredient-Based Recommendations")
    st.write("Select ingredients you have available to get personalized recipe suggestions.")
    
    # Common ingredient categories
    ingredient_categories = {
        "Fruits": ["Apple", "Banana", "Orange", "Berries", "Grapes", "Mango"],
        "Vegetables": ["Carrot", "Cucumber", "Celery", "Spinach", "Kale", "Bell Pepper"],
        "Proteins": ["Chicken", "Turkey", "Tuna", "Eggs", "Tofu", "Greek Yogurt"],
        "Nuts & Seeds": ["Almonds", "Walnuts", "Cashews", "Chia Seeds", "Pumpkin Seeds"],
        "Grains": ["Oats", "Quinoa", "Brown Rice", "Whole Grain Bread", "Granola"],
        "Other": ["Honey", "Peanut Butter", "Hummus", "Dark Chocolate", "Avocado"]
    }
    
    # Create expandable sections for each category
    for category, ingredients in ingredient_categories.items():
        with st.expander(f"{category}"):
            cols = st.columns(3)
            for i, ingredient in enumerate(ingredients):
                with cols[i % 3]:
                    if st.checkbox(ingredient, ingredient in st.session_state.ingredients):
                        if ingredient not in st.session_state.ingredients:
                            st.session_state.ingredients.append(ingredient)
                    else:
                        if ingredient in st.session_state.ingredients:
                            st.session_state.ingredients.remove(ingredient)
    
    # Display selected ingredients
    st.markdown("### Your Selected Ingredients")
    if not st.session_state.ingredients:
        st.info("No ingredients selected yet. Check the boxes above to select ingredients.")
    else:
        # Display ingredients as chips in a horizontal layout
        ingredient_html = ""
        for ingredient in st.session_state.ingredients:
            ingredient_html += f'<span style="background-color:#f0f2f6; padding:5px 10px; margin:2px; border-radius:20px; display:inline-block">{ingredient}</span>'
        
        st.markdown(f"<div>{ingredient_html}</div>", unsafe_allow_html=True)
        
        # Get recipe recommendations based on ingredients
        if st.button("Find Recipes With These Ingredients"):
            with st.spinner("Searching for recipes..."):
                recipes = get_recipe_by_ingredients(st.session_state.ingredients)
                
                if recipes:
                    st.success(f"Found {len(recipes)} recipes with your ingredients!")
                    
                    # Show recipe previews
                    for i, recipe in enumerate(recipes[:3]):
                        st.markdown(f"### {recipe['name']}")
                        st.markdown(f"**Ingredients used:** {', '.join(recipe['ingredients_used'])}")
                        st.markdown(f"**Missing ingredients:** {', '.join(recipe['missing_ingredients'])}")
                        
                        if st.button(f"View Full Recipe", key=f"view_recipe_{i}"):
                            st.session_state.recipe_search = recipe['name']
                            # Also set the current_recipe id to display details directly
                            st.session_state.current_recipe = recipe['id']
                            st.switch_page("pages/03_Recipes.py")
                else:
                    st.warning("No recipes found with those ingredients. Try selecting more ingredients.")
                
                # Log the activity
                log_activity("ingredient_search", {
                    "ingredients": st.session_state.ingredients,
                    "recipes_found": len(recipes) if recipes else 0
                })

# Sidebar with navigation and information
with st.sidebar:
    st.title("Your Custom Profile")
    
    # Show user info if logged in
    if "user" in st.session_state and st.session_state.user["logged_in"]:
        st.info(f"Logged in as: {st.session_state.user['username']}")
    else:
        st.warning("Log in to save your preferences")
    
    # Navigation buttons
    st.markdown("---")
    st.markdown("### Navigation")
    
    if st.button("🏠 Home"):
        st.switch_page("app.py")
    
    if st.button("🔮 Snack Prediction"):
        st.switch_page("pages/01_Snack_Prediction.py")
    
    if st.button("🍽️ Recipes"):
        st.switch_page("pages/03_Recipes.py")
    
    # Profile completion
    st.markdown("---")
    st.markdown("### Profile Completion")
    
    # Calculate profile completion percentage
    completion_items = {
        "dietary": any(st.session_state.dietary_preferences.values()),
        "taste": st.session_state.taste_preferences != {"sweet": 50, "savory": 50, "spicy": 50},
        "health_goals": any(st.session_state.health_goals.values()),
        "ingredients": len(st.session_state.ingredients) > 0
    }
    
    completion_percentage = int(sum(completion_items.values()) / len(completion_items) * 100)
    
    # Display progress bar
    st.progress(completion_percentage / 100)
    st.write(f"Profile Completion: {completion_percentage}%")
    
    # Suggest next steps based on completion
    if completion_percentage < 100:
        missing_items = [k for k, v in completion_items.items() if not v]
        st.info(f"Complete your profile by setting: {', '.join(missing_items)}")
