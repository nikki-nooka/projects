import streamlit as st
import time
from PIL import Image
import random
import base64
from utils.food_classifier import classify_food
from utils.recipe_recommender import get_recipe_recommendation
from utils.mood_recommender import get_mood_recommendations
from utils.database import (
    register_user, 
    authenticate_user, 
    log_user_activity, 
    get_user_activity,
    get_user_preferences, 
    update_user_preferences
)

# Set page configuration
st.set_page_config(
    page_title="Smart Snack Predictor",
    page_icon="🍎",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize session state for user tracking
if "user" not in st.session_state:
    st.session_state.user = {
        "logged_in": False,
        "username": "",
        "id": None,
    }

# Function to handle user login
def login(username, password):
    # Authenticate against the database
    success, result = authenticate_user(username, password)
    
    if success:
        # Update session state with user info
        st.session_state.user = result
        return True
    return False

# Function to handle user registration
def register(username, password, email=None):
    # Register user in the database
    success, result = register_user(username, password, email)
    return success, result

# Function to log user activity
def log_activity(activity_type, details):
    # First, log to session for immediate feedback
    if st.session_state.user["logged_in"]:
        # Log to database if user is logged in
        user_id = st.session_state.user.get("id")
        if user_id:
            log_user_activity(user_id, activity_type, details)

# Home Page
def home_page():
    st.title("🏠 Welcome to Smart Snack Predictor")
    
    # Create two columns for layout
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("""
        ### Your AI-Powered Nutrition Assistant
        
        Smart Snack Predictor helps you make healthier food choices by:
        
        - 🔍 **Analyzing** food images to determine nutritional value
        - 🧠 **Recommending** alternatives based on your preferences
        - 😊 **Suggesting** snacks that match your current mood
        - 👨‍🍳 **Providing** delicious and healthy recipes
        
        Get started by uploading an image or selecting a food category!
        """)
        
        # Call-to-Action Buttons
        cta_col1, cta_col2 = st.columns(2)
        with cta_col1:
            if st.button("🔮 Analyze Food", use_container_width=True):
                st.switch_page("pages/01_Snack_Prediction.py")
        
        with cta_col2:
            if st.button("🍽️ Browse Recipes", use_container_width=True):
                st.switch_page("pages/03_Recipes.py")
    
    with col2:
        # Display animated header image
        st.markdown("""
        <div style="display: flex; justify-content: center; align-items: center; height: 300px;">
            <svg width="300" height="300" viewBox="0 0 300 300">
                <!-- Plate circle -->
                <circle cx="150" cy="150" r="120" fill="#f5f5f5" stroke="#ddd" stroke-width="2"/>
                <!-- Healthy food items -->
                <circle cx="120" cy="120" r="30" fill="#8bc34a"/>  <!-- Green apple -->
                <circle cx="180" cy="130" r="25" fill="#ff9800"/>  <!-- Orange -->
                <circle cx="150" cy="170" r="20" fill="#f44336"/>  <!-- Tomato -->
                <path d="M90,160 Q150,200 210,160" stroke="#795548" fill="transparent" stroke-width="8"/> <!-- Bowl rim -->
                <!-- Fork icon -->
                <path d="M240,80 L255,65 M240,100 L255,85 M240,120 L255,105 M247,70 L247,125 L240,140 L240,190" stroke="#616161" stroke-width="4" fill="transparent"/>
            </svg>
        </div>
        """, unsafe_allow_html=True)
        
        # Mood-based recommendation teaser
        st.markdown("### How are you feeling today?")
        moods = ["Energetic", "Stressed", "Happy", "Tired", "Focused"]
        selected_mood = st.selectbox("Select your mood", moods)
        if st.button("Get Mood-Based Recommendations"):
            recommendations = get_mood_recommendations(selected_mood)
            # Extract just the food names from the recommendation objects
            food_names = [rec["name"] for rec in recommendations[:3]]
            st.success(f"Based on your {selected_mood} mood, we recommend: {', '.join(food_names)}")
            log_activity("mood_recommendation", {"mood": selected_mood, "recommendations": food_names})

    # Health Facts Section
    st.markdown("---")
    st.markdown("### 💡 Quick Health Facts")
    
    fact_col1, fact_col2, fact_col3 = st.columns(3)
    
    with fact_col1:
        st.markdown("""
        #### Hydration
        Drinking enough water can improve energy and brain function.
        """)
    
    with fact_col2:
        st.markdown("""
        #### Snack Timing
        Eating small, healthy snacks between meals can help maintain stable blood sugar.
        """)
    
    with fact_col3:
        st.markdown("""
        #### Nutrient Balance
        A balanced snack should include protein, healthy fats, and complex carbs.
        """)

    # Login Section in Sidebar
    with st.sidebar:
        st.title("User Area")
        
        if not st.session_state.user["logged_in"]:
            # Create tabs for login and registration
            login_tab, register_tab = st.tabs(["Login", "Register"])
            
            with login_tab:
                username = st.text_input("Username", key="login_username")
                password = st.text_input("Password", type="password", key="login_password")
                
                if st.button("Login", use_container_width=True):
                    if login(username, password):
                        st.success(f"Welcome, {username}!")
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.error("Invalid username or password")
            
            with register_tab:
                new_username = st.text_input("Choose Username", key="register_username")
                new_password = st.text_input("Choose Password", type="password", key="register_password")
                confirm_password = st.text_input("Confirm Password", type="password")
                email = st.text_input("Email (Optional)")
                
                if st.button("Create Account", use_container_width=True):
                    if not new_username or not new_password:
                        st.error("Username and password are required")
                    elif new_password != confirm_password:
                        st.error("Passwords do not match")
                    else:
                        success, result = register(new_username, new_password, email)
                        if success:
                            st.success("Account created successfully! Please login.")
                            # Automatically login the new user
                            if login(new_username, new_password):
                                time.sleep(1)
                                st.rerun()
                        else:
                            st.error(f"Registration failed: {result}")
        else:
            # User is logged in
            st.subheader(f"Welcome, {st.session_state.user['username']}!")
            
            # Get user activity from database
            user_id = st.session_state.user.get("id")
            if user_id:
                activities = get_user_activity(user_id, limit=5)
                
                st.markdown("### Recent Activity")
                if activities:
                    for activity in activities:
                        st.markdown(f"**{activity['activity']}** - {activity['timestamp']}")
                else:
                    st.info("No recent activity")
            
            # Add some user options
            st.markdown("---")
            st.markdown("### Options")
            
            if st.button("My Profile", use_container_width=True):
                st.session_state.active_page = "profile"
                st.switch_page("pages/02_Customization.py")
            
            if st.button("Logout", use_container_width=True):
                # Reset user session
                st.session_state.user = {
                    "logged_in": False,
                    "username": "",
                    "id": None
                }
                st.success("Logged out successfully!")
                time.sleep(1)
                st.rerun()

# Run the Home Page
home_page()
