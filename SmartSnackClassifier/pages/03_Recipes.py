import streamlit as st
import time
import numpy as np
from utils.recipe_recommender import get_recipe_details, search_recipes
from utils.mood_recommender import get_mood_recommendations

# Set page configuration
st.set_page_config(
    page_title="Recipes - Smart Snack Predictor",
    page_icon="🍽️",
    layout="wide",
)

# Page Title
st.title("🍽️ Healthy Recipes")
st.markdown("Discover delicious and nutritious recipes for your snacks and meals.")

# Import the log_user_activity function from the database module
from utils.database import log_user_activity

# Function to log activity
def log_activity(activity_type, details):
    if "user" in st.session_state and st.session_state.user["logged_in"]:
        # Log to database if user is logged in
        user_id = st.session_state.user.get("id")
        if user_id:
            log_user_activity(user_id, activity_type, details)

# Check if a recipe search was requested from another page
search_term = ""
if "recipe_search" in st.session_state and st.session_state.recipe_search:
    search_term = st.session_state.recipe_search
    
    # If we have a direct recipe search term from customization page, 
    # we need to search for and display that recipe
    if not "current_recipe" in st.session_state:
        # Search for the recipe and set current_recipe if found
        with st.spinner("Searching for recipe..."):
            recipes = search_recipes(search_term, limit=3)
            if recipes and len(recipes) > 0:
                # Set the first matching recipe as current recipe
                st.session_state.current_recipe = recipes[0]['id']
                st.info(f"Found recipe for {search_term}")
            
    # Clear the search term so it doesn't persist across page reloads
    st.session_state.recipe_search = ""

# Search section
st.markdown("### Search Recipes")
col1, col2 = st.columns([3, 1])

with col1:
    search_query = st.text_input("Enter keywords, ingredients, or dish name", value=search_term)

with col2:
    search_button = st.button("Search", use_container_width=True)

# Recipe filters in expandable section
with st.expander("Recipe Filters"):
    filter_col1, filter_col2, filter_col3 = st.columns(3)
    
    with filter_col1:
        meal_type = st.multiselect(
            "Meal Type",
            ["Breakfast", "Snack", "Lunch", "Dinner", "Dessert"],
            default=["Snack"]
        )
        
        cooking_time = st.slider("Max Cooking Time (minutes)", 5, 60, 30)
    
    with filter_col2:
        dietary_filters = st.multiselect(
            "Dietary Restrictions",
            ["Vegetarian", "Vegan", "Gluten-Free", "Dairy-Free", "Nut-Free"],
            default=[]
        )
        
        calories = st.slider("Max Calories", 50, 800, 400)
    
    with filter_col3:
        difficulty = st.select_slider(
            "Difficulty Level",
            options=["Easy", "Medium", "Hard"],
            value="Easy"
        )
        
        sort_by = st.radio(
            "Sort Results By",
            ["Popularity", "Quick & Easy", "Nutritional Value"]
        )

# Search functionality
if search_query and (search_button or search_term):
    with st.spinner("Searching for recipes..."):
        # Get recipes matching the search criteria
        recipes = search_recipes(
            search_query, 
            meal_types=meal_type,
            max_time=cooking_time,
            dietary_restrictions=dietary_filters,
            max_calories=calories,
            difficulty=difficulty,
            sort_by=sort_by
        )
        
        if recipes:
            st.success(f"Found {len(recipes)} recipes matching your criteria!")
            
            # Log the activity
            log_activity("recipe_search", {
                "query": search_query,
                "filters": {
                    "meal_type": meal_type,
                    "cooking_time": cooking_time,
                    "dietary": dietary_filters,
                    "calories": calories,
                    "difficulty": difficulty
                },
                "results_count": len(recipes)
            })
            
            # Display recipe cards in a grid
            for i in range(0, len(recipes), 3):
                cols = st.columns(3)
                for j in range(3):
                    if i + j < len(recipes):
                        recipe = recipes[i + j]
                        with cols[j]:
                            st.markdown(f"### {recipe['name']}")
                            
                            # SVG placeholder for recipe image
                            svg_html = f'''
                            <svg width="100%" height="120" style="background-color: #f0f2f6; border-radius: 10px;">
                                <rect width="100%" height="120" fill="#f0f2f6" rx="10" ry="10"/>
                                <text x="50%" y="50%" font-family="Arial" font-size="14" fill="#555" text-anchor="middle" dominant-baseline="middle">
                                    {recipe['name']}
                                </text>
                                <circle cx="40" cy="40" r="15" fill="{recipe['color']}" opacity="0.7"/>
                                <circle cx="80%" cy="70%" r="20" fill="{recipe['color']}" opacity="0.5"/>
                            </svg>
                            '''
                            st.markdown(svg_html, unsafe_allow_html=True)
                            
                            st.markdown(f"⏱️ **Time:** {recipe['time']} minutes")
                            st.markdown(f"🔥 **Calories:** {recipe['calories']} kcal")
                            st.markdown(f"⭐ **Rating:** {recipe['rating']}/5")
                            
                            # Button to view full recipe
                            if st.button(f"View Recipe", key=f"view_recipe_{i+j}"):
                                st.session_state.current_recipe = recipe['id']
        else:
            st.warning("No recipes found matching your criteria. Try adjusting your search or filters.")

# Display full recipe if one is selected
if "current_recipe" in st.session_state and st.session_state.current_recipe:
    recipe_id = st.session_state.current_recipe
    recipe_details = get_recipe_details(recipe_id)
    
    if recipe_details:
        st.markdown("---")
        
        # Create a header section
        st.markdown(f"# {recipe_details['name']}")
        st.markdown(f"*{recipe_details['description']}*")
        
        # Recipe metadata
        meta_col1, meta_col2, meta_col3, meta_col4 = st.columns(4)
        with meta_col1:
            st.markdown(f"⏱️ **Prep Time:** {recipe_details['prep_time']} mins")
        with meta_col2:
            st.markdown(f"👨‍🍳 **Cook Time:** {recipe_details['cook_time']} mins")
        with meta_col3:
            st.markdown(f"👥 **Servings:** {recipe_details['servings']}")
        with meta_col4:
            st.markdown(f"🔥 **Calories:** {recipe_details['calories']} kcal")
        
        # Divider
        st.markdown("---")
        
        # Main content in two columns
        content_col1, content_col2 = st.columns([1, 1])
        
        with content_col1:
            st.markdown("## Ingredients")
            for ingredient in recipe_details['ingredients']:
                st.markdown(f"- {ingredient}")
            
            # Nutrition information in expandable section
            with st.expander("Nutrition Information"):
                nutrition = recipe_details['nutrition']
                
                # Display as metrics
                nut_col1, nut_col2 = st.columns(2)
                with nut_col1:
                    st.metric("Calories", f"{nutrition['calories']} kcal")
                    st.metric("Protein", f"{nutrition['protein']}g")
                    st.metric("Carbs", f"{nutrition['carbs']}g")
                with nut_col2:
                    st.metric("Fat", f"{nutrition['fat']}g")
                    st.metric("Fiber", f"{nutrition['fiber']}g")
                    st.metric("Sugar", f"{nutrition['sugar']}g")
        
        with content_col2:
            st.markdown("## Instructions")
            for i, step in enumerate(recipe_details['steps'], 1):
                st.markdown(f"**Step {i}:** {step}")
            
            # Healthiness score with explanation
            st.markdown("## Healthiness Score")
            score = recipe_details['health_score']
            
            # Create a progress bar based on health score
            st.progress(score / 100)
            st.markdown(f"**Score: {score}/100**")
            st.markdown(f"*{recipe_details['health_notes']}*")
        
        # Log the recipe view
        log_activity("recipe_view", {
            "recipe_id": recipe_id,
            "recipe_name": recipe_details['name']
        })
        
        # Button to clear current recipe and return to search
        if st.button("Back to Recipe Search"):
            st.session_state.current_recipe = None
            st.rerun()
    else:
        st.error("Recipe details could not be loaded.")
        st.session_state.current_recipe = None

# If no search or recipe is being viewed, show featured content
if not search_query and "current_recipe" not in st.session_state:
    st.markdown("## Featured Recipes")
    
    # Create tabs for different categories
    featured_tab1, featured_tab2, featured_tab3 = st.tabs(["🌟 Popular", "⏱️ Quick & Easy", "🥗 Super Healthy"])
    
    with featured_tab1:
        # Get popular recipes
        popular_recipes = search_recipes("", sort_by="Popularity", limit=6)
        
        # Display in a grid
        for i in range(0, len(popular_recipes), 3):
            cols = st.columns(3)
            for j in range(3):
                if i + j < len(popular_recipes):
                    recipe = popular_recipes[i + j]
                    with cols[j]:
                        st.markdown(f"### {recipe['name']}")
                        # SVG placeholder for recipe image
                        svg_html = f'''
                        <svg width="100%" height="100" style="background-color: #f0f2f6; border-radius: 10px;">
                            <rect width="100%" height="100" fill="#f0f2f6" rx="10" ry="10"/>
                            <text x="50%" y="50%" font-family="Arial" font-size="14" fill="#555" text-anchor="middle" dominant-baseline="middle">
                                {recipe['name']}
                            </text>
                            <circle cx="30%" cy="30%" r="15" fill="#ff9800" opacity="0.7"/>
                            <circle cx="70%" cy="70%" r="20" fill="#4caf50" opacity="0.5"/>
                        </svg>
                        '''
                        st.markdown(svg_html, unsafe_allow_html=True)
                        st.markdown(f"⏱️ **Time:** {recipe['time']} min | 🔥 **Calories:** {recipe['calories']} kcal")
                        if st.button(f"View Recipe", key=f"popular_{i+j}"):
                            st.session_state.current_recipe = recipe['id']
                            st.rerun()
    
    with featured_tab2:
        # Get quick recipes
        quick_recipes = search_recipes("", sort_by="Quick & Easy", max_time=15, limit=6)
        
        # Display in a grid
        for i in range(0, len(quick_recipes), 3):
            cols = st.columns(3)
            for j in range(3):
                if i + j < len(quick_recipes):
                    recipe = quick_recipes[i + j]
                    with cols[j]:
                        st.markdown(f"### {recipe['name']}")
                        # SVG placeholder for recipe image
                        svg_html = f'''
                        <svg width="100%" height="100" style="background-color: #f0f2f6; border-radius: 10px;">
                            <rect width="100%" height="100" fill="#f0f2f6" rx="10" ry="10"/>
                            <text x="50%" y="50%" font-family="Arial" font-size="14" fill="#555" text-anchor="middle" dominant-baseline="middle">
                                {recipe['name']}
                            </text>
                            <circle cx="30%" cy="70%" r="15" fill="#2196f3" opacity="0.7"/>
                            <circle cx="70%" cy="30%" r="20" fill="#ff5722" opacity="0.5"/>
                        </svg>
                        '''
                        st.markdown(svg_html, unsafe_allow_html=True)
                        st.markdown(f"⏱️ **Time:** {recipe['time']} min | 🔥 **Calories:** {recipe['calories']} kcal")
                        if st.button(f"View Recipe", key=f"quick_{i+j}"):
                            st.session_state.current_recipe = recipe['id']
                            st.rerun()
    
    with featured_tab3:
        # Get healthy recipes
        healthy_recipes = search_recipes("", sort_by="Nutritional Value", limit=6)
        
        # Display in a grid
        for i in range(0, len(healthy_recipes), 3):
            cols = st.columns(3)
            for j in range(3):
                if i + j < len(healthy_recipes):
                    recipe = healthy_recipes[i + j]
                    with cols[j]:
                        st.markdown(f"### {recipe['name']}")
                        # SVG placeholder for recipe image
                        svg_html = f'''
                        <svg width="100%" height="100" style="background-color: #f0f2f6; border-radius: 10px;">
                            <rect width="100%" height="100" fill="#f0f2f6" rx="10" ry="10"/>
                            <text x="50%" y="50%" font-family="Arial" font-size="14" fill="#555" text-anchor="middle" dominant-baseline="middle">
                                {recipe['name']}
                            </text>
                            <circle cx="30%" cy="40%" r="15" fill="#8bc34a" opacity="0.7"/>
                            <circle cx="70%" cy="60%" r="20" fill="#9c27b0" opacity="0.5"/>
                        </svg>
                        '''
                        st.markdown(svg_html, unsafe_allow_html=True)
                        st.markdown(f"⏱️ **Time:** {recipe['time']} min | 🔥 **Calories:** {recipe['calories']} kcal")
                        if st.button(f"View Recipe", key=f"healthy_{i+j}"):
                            st.session_state.current_recipe = recipe['id']
                            st.rerun()
    
    # Mood-based recipe suggestion section
    st.markdown("---")
    st.markdown("## Mood-Based Recipe Suggestions")
    st.write("Not sure what to cook? Let us suggest recipes based on your current mood!")
    
    mood_col1, mood_col2 = st.columns([3, 1])
    
    with mood_col1:
        moods = ["Energetic", "Stressed", "Happy", "Tired", "Focused", "Relaxed", "Hungry"]
        selected_mood = st.select_slider("How are you feeling right now?", options=moods)
    
    with mood_col2:
        mood_button = st.button("Get Suggestions", use_container_width=True)
    
    if mood_button:
        with st.spinner(f"Finding the perfect recipes for your {selected_mood.lower()} mood..."):
            # Get mood-based recommendations
            mood_recs = get_mood_recommendations(selected_mood, get_recipes=True)
            
            st.success(f"Here are recipes perfect for when you're feeling {selected_mood.lower()}:")
            
            # Display recommendations
            for i, rec in enumerate(mood_recs[:3]):
                st.markdown(f"### {rec['name']}")
                st.markdown(f"**Why it's perfect:** {rec['reason']}")
                
                # Display in columns: recipe info and "why it works"
                rec_col1, rec_col2 = st.columns([2, 3])
                
                with rec_col1:
                    # SVG placeholder for recipe image
                    svg_html = f'''
                    <svg width="100%" height="120" style="background-color: #f0f2f6; border-radius: 10px;">
                        <rect width="100%" height="120" fill="#f0f2f6" rx="10" ry="10"/>
                        <text x="50%" y="50%" font-family="Arial" font-size="14" fill="#555" text-anchor="middle" dominant-baseline="middle">
                            {rec['name']}
                        </text>
                        <circle cx="30%" cy="30%" r="15" fill="{rec['color']}" opacity="0.7"/>
                        <circle cx="70%" cy="70%" r="20" fill="{rec['color']}" opacity="0.5"/>
                    </svg>
                    '''
                    st.markdown(svg_html, unsafe_allow_html=True)
                    
                    st.markdown(f"⏱️ **Time:** {rec['time']} minutes")
                    st.markdown(f"🔥 **Calories:** {rec['calories']} kcal")
                
                with rec_col2:
                    st.markdown(f"**Key ingredients:** {', '.join(rec['key_ingredients'])}")
                    st.markdown(f"**Mood-boosting nutrients:** {rec['nutrients']}")
                    
                    if st.button(f"View Full Recipe", key=f"mood_recipe_{i}"):
                        st.session_state.current_recipe = rec['id']
                        st.rerun()
                
                st.markdown("---")
            
            # Log the activity
            log_activity("mood_recipe_recommendation", {
                "mood": selected_mood,
                "recipes": [r['name'] for r in mood_recs[:3]]
            })

# Sidebar with navigation
with st.sidebar:
    st.title("Recipe Book")
    
    # Navigation buttons
    st.markdown("### Navigation")
    
    if st.button("🏠 Home"):
        st.switch_page("app.py")
    
    if st.button("🔮 Snack Prediction"):
        st.switch_page("pages/01_Snack_Prediction.py")
    
    if st.button("🎨 Customization"):
        st.switch_page("pages/02_Customization.py")
    
    # Saved recipes section (if user is logged in)
    if "user" in st.session_state and st.session_state.user["logged_in"]:
        st.markdown("---")
        st.markdown("### Your Saved Recipes")
        
        # In a real app, these would be pulled from a database
        # For this MVP, we'll just show some placeholder data
        if st.button("Apple Cinnamon Overnight Oats"):
            # Set the recipe to view and refresh the page
            st.session_state.current_recipe = "recipe001"
            st.rerun()
        
        if st.button("Greek Yogurt Parfait"):
            st.session_state.current_recipe = "recipe002"
            st.rerun()
        
        if st.button("Roasted Chickpeas"):
            st.session_state.current_recipe = "recipe003"
            st.rerun()
    else:
        st.markdown("---")
        st.info("Log in to save your favorite recipes!")
    
    # Cooking tips
    st.markdown("---")
    st.markdown("### 💡 Cooking Tips")
    tips = [
        "Prep ingredients before starting to cook",
        "Use herbs at the end of cooking for maximum flavor",
        "Let meats rest before cutting",
        "Taste and adjust seasoning as you cook",
        "Sharp knives are safer than dull ones"
    ]
    st.info(tips[np.random.randint(0, len(tips))])
