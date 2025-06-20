import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io
import time
import traceback
from utils.food_classifier import classify_food, get_nutrition_info
from utils.image_processor import preprocess_image

# Enable debug mode - set to True to show detailed error information
DEBUG = True

# Set page configuration
st.set_page_config(
    page_title="Snack Prediction - Smart Snack Predictor",
    page_icon="🔮",
    layout="wide",
)

# Page Title
st.title("🔮 Snack Prediction")
st.markdown("Upload or capture a food image to analyze whether it's healthy.")

# Import the log_user_activity function from the database module
from utils.database import log_user_activity

# Function to log activity
def log_activity(activity_type, details):
    if "user" in st.session_state and st.session_state.user["logged_in"]:
        # Log to database if user is logged in
        user_id = st.session_state.user.get("id")
        if user_id:
            log_user_activity(user_id, activity_type, details)

# Function to process and analyze an image
def analyze_food_image(image_data):
    """Process and analyze a food image, returning classification results"""
    try:
        if DEBUG:
            st.info("Starting image analysis...")
        
        # Convert the image for processing
        img = Image.open(image_data)
        
        if DEBUG:
            st.info(f"Image opened. Format: {img.format}, Size: {img.size}, Mode: {img.mode}")
        
        img_array = np.array(img)
        
        # Check if image is valid
        if img_array.size == 0:
            st.error("Invalid image. Please try again.")
            return None, None
        
        if DEBUG:
            st.info(f"Image converted to array. Shape: {img_array.shape}, Type: {img_array.dtype}")
        
        # Process the image
        processed_img = preprocess_image(img_array)
        
        if DEBUG:
            st.info("Image preprocessed successfully. Getting classification...")
        
        # Get prediction and nutrition info
        prediction = classify_food(processed_img)
        
        if DEBUG:
            st.info(f"Image classified as: {prediction['food_name']}")
        
        nutrition = get_nutrition_info(prediction["food_name"])
        
        return prediction, nutrition
    
    except Exception as e:
        # Get detailed error information
        error_details = traceback.format_exc()
        
        if DEBUG:
            st.error(f"Error processing image: {str(e)}")
            st.code(error_details, language="python")
            
            # Add image info if available
            img_info = "No image data available"
            try:
                if 'img' in locals() and img is not None:
                    img_info = f"Format: {img.format}, Size: {img.size}, Mode: {img.mode}"
            except Exception:
                pass
            
            st.info(f"Image info: {img_info}")
        else:
            st.error(f"Error processing image. Please try again with a different image.")
        
        return None, None

# Initialize session state for image and results
if "prediction_image" not in st.session_state:
    st.session_state.prediction_image = None
if "prediction_result" not in st.session_state:
    st.session_state.prediction_result = None
if "nutrition_info" not in st.session_state:
    st.session_state.nutrition_info = None

# Create tabs for different input methods
input_tab1, input_tab2 = st.tabs(["📷 Camera Input", "🖼️ Upload Image"])

with input_tab1:
    st.markdown("### Capture Food Image")
    
    # Add camera instructions
    st.markdown("""
    📸 **Camera Tips:**
    - Make sure your browser has permission to access the camera
    - Position your food item in good lighting
    - Hold the device steady when taking the photo
    """)
    
    # Create a container to handle camera state
    camera_container = st.container()
    
    # Store camera state in session state
    if "camera_active" not in st.session_state:
        st.session_state.camera_active = False
    
    # Add buttons to control camera
    camera_col1, camera_col2 = st.columns(2)
    
    with camera_col1:
        if not st.session_state.camera_active:
            if st.button("Activate Camera", use_container_width=True):
                st.session_state.camera_active = True
                st.rerun()
    
    with camera_col2:
        analyze_button = st.button("Analyze Image", key="camera_analyze", 
                                  disabled=(not st.session_state.camera_active or "captured_image" not in st.session_state),
                                  use_container_width=True)
    
    # Display camera input if active
    if st.session_state.camera_active:
        with camera_container:
            # Use a key to force reload on every run
            camera_image = st.camera_input("Take a picture of your food", 
                                         key=f"camera_{time.time()}", 
                                         help="Take a clear photo of your food")
            
            # If image is captured, store it in session state
            if camera_image:
                st.session_state.captured_image = camera_image
                st.success("Image captured! Click 'Analyze Image' to process.")
                
                # Display the captured image
                st.image(camera_image, caption="Captured Image", width=300)
    
    # Show deactivate button if camera is active
    if st.session_state.camera_active:
        if st.button("Deactivate Camera"):
            st.session_state.camera_active = False
            if "captured_image" in st.session_state:
                del st.session_state.captured_image
            st.rerun()
    
    # Process image when analyze button is clicked
    if "captured_image" in st.session_state and analyze_button:
        # Store the image in session state
        st.session_state.prediction_image = st.session_state.captured_image
        
        # Display a processing message
        with st.spinner("Processing image..."):
            # Analyze the image
            prediction, nutrition = analyze_food_image(st.session_state.captured_image)
            
            if prediction and nutrition:
                # Store results in session state
                st.session_state.prediction_result = prediction
                st.session_state.nutrition_info = nutrition
                
                # Log the activity
                log_activity("food_prediction", {
                    "food": prediction["food_name"],
                    "healthy": prediction["is_healthy"],
                    "confidence": prediction["confidence"]
                })
                
                # Show success message
                st.success("Image successfully analyzed! See results below.")
            else:
                # Clear the error state
                st.session_state.prediction_image = None

with input_tab2:
    st.markdown("### Upload Food Image")
    
    # Add upload instructions
    st.markdown("""
    📁 **Upload Tips:**
    - Choose a clear, well-lit photo of your food
    - Supported formats: JPG, JPEG, PNG
    - Try to upload images with a single food item for best results
    """)
    
    # File uploader for images
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    analyze_button = st.button("Analyze Image", key="upload_analyze", disabled=(uploaded_file is None))
    
    if uploaded_file is not None and analyze_button:
        # Store the image in session state
        st.session_state.prediction_image = uploaded_file
        
        # Display a processing message
        with st.spinner("Processing image..."):
            # Analyze the image
            prediction, nutrition = analyze_food_image(uploaded_file)
            
            if prediction and nutrition:
                # Store results in session state
                st.session_state.prediction_result = prediction
                st.session_state.nutrition_info = nutrition
                
                # Log the activity
                log_activity("food_prediction", {
                    "food": prediction["food_name"],
                    "healthy": prediction["is_healthy"],
                    "confidence": prediction["confidence"]
                })
                
                # Show success message
                st.success("Image successfully analyzed! See results below.")
            else:
                # Clear the error state
                st.session_state.prediction_image = None

# Display results if available
if (st.session_state.prediction_image is not None and 
    st.session_state.prediction_result is not None and 
    st.session_state.nutrition_info is not None):
    
    st.markdown("---")
    st.markdown("## Analysis Results")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Display the image
        st.image(st.session_state.prediction_image, caption="Analyzed Food", use_column_width=True)
    
    with col2:
        prediction = st.session_state.prediction_result
        nutrition = st.session_state.nutrition_info
        
        # Display the prediction result with appropriate styling
        if prediction.get("is_healthy", False):
            st.success(f"✅ This appears to be a **healthy** choice: **{prediction.get('food_name', 'Unknown Food')}**")
        else:
            st.error(f"⚠️ This may not be the healthiest choice: **{prediction.get('food_name', 'Unknown Food')}**")
        
        st.write(f"**Confidence:** {prediction.get('confidence', 0):.2f}%")
        
        # Display nutrition information
        st.markdown("### Nutrition Information")
        
        # Create metrics for key nutrition facts
        metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
        with metric_col1:
            st.metric("Calories", f"{nutrition.get('calories', 0)} kcal")
        with metric_col2:
            st.metric("Protein", f"{nutrition.get('protein', 0)}g")
        with metric_col3:
            st.metric("Carbs", f"{nutrition.get('carbs', 0)}g")
        with metric_col4:
            st.metric("Fat", f"{nutrition.get('fat', 0)}g")
        
        # Show more detailed nutrition info
        with st.expander("View Detailed Nutrition Information"):
            st.json(nutrition)
        
        # Provide healthier alternatives if not healthy
        if not prediction.get("is_healthy", True):
            st.markdown("### Healthier Alternatives")
            alternatives = prediction.get("alternatives", [])
            if alternatives:
                for alt in alternatives:
                    st.write(f"• **{alt}**")
                
                if st.button("Get Recipes for Alternatives"):
                    st.session_state.recipe_search = alternatives[0]
                    st.switch_page("pages/03_Recipes.py")
            else:
                st.info("No specific alternatives available for this food.")

# Sidebar with additional options
with st.sidebar:
    st.title("Options")
    
    # Clear results button
    if st.button("Clear Results"):
        st.session_state.prediction_image = None
        st.session_state.prediction_result = None
        st.session_state.nutrition_info = None
        st.rerun()
    
    # Navigation buttons
    st.markdown("---")
    st.markdown("### Navigation")
    
    if st.button("🏠 Home"):
        st.switch_page("app.py")
    
    if st.button("🎨 Customization"):
        st.switch_page("pages/02_Customization.py")
    
    if st.button("🍽️ Recipes"):
        st.switch_page("pages/03_Recipes.py")
        
    # Health tips
    st.markdown("---")
    st.markdown("### 💡 Health Tips")
    tips = [
        "Snacks with protein keep you full longer",
        "Fruits make excellent natural sweet snacks",
        "Adding nuts to your diet provides healthy fats",
        "Avoid processed foods high in added sugars",
        "Vegetables with hummus make a perfect snack"
    ]
    st.info(tips[np.random.randint(0, len(tips))])