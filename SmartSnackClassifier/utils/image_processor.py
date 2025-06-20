import cv2
import numpy as np
from PIL import Image
import io

def preprocess_image(image_array):
    """
    Preprocess image for model input
    
    Args:
        image_array: Input image as numpy array
        
    Returns:
        Preprocessed image
    """
    # Resize to standard input size (224x224 is common for many models)
    image = cv2.resize(image_array, (224, 224))
    
    # Convert to RGB if grayscale
    if len(image.shape) == 2:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    elif image.shape[2] == 4:  # Handle RGBA
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
    
    # Normalize pixel values
    image = image.astype(np.float32) / 255.0
    
    return image

def enhance_image(image_array):
    """
    Enhance image for better visualization
    
    Args:
        image_array: Input image as numpy array
        
    Returns:
        Enhanced image
    """
    # Convert to LAB color space
    lab = cv2.cvtColor(image_array, cv2.COLOR_RGB2LAB)
    
    # Split channels
    l, a, b = cv2.split(lab)
    
    # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)
    
    # Merge channels
    limg = cv2.merge((cl, a, b))
    
    # Convert back to RGB
    enhanced = cv2.cvtColor(limg, cv2.COLOR_LAB2RGB)
    
    return enhanced

def convert_to_bytes(image_array):
    """
    Convert image array to bytes for displaying in Streamlit
    
    Args:
        image_array: Input image as numpy array
        
    Returns:
        Image bytes
    """
    # Convert to PIL Image
    pil_image = Image.fromarray(np.uint8(image_array * 255) if image_array.dtype == np.float32 else np.uint8(image_array))
    
    # Save to bytes
    img_byte_arr = io.BytesIO()
    pil_image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    
    return img_byte_arr.getvalue()

def detect_food_in_image(image_array):
    """
    Detect food items in an image
    
    Args:
        image_array: Input image as numpy array
        
    Returns:
        Bounding boxes and labels for detected food items
    """
    # In a real application, this would use object detection models
    # For this MVP, we'll simulate detection
    
    # Get image dimensions
    height, width = image_array.shape[:2]
    
    # Simulate a detection by creating a bounding box
    center_x, center_y = width // 2, height // 2
    box_width, box_height = int(width * 0.7), int(height * 0.7)
    
    x1 = max(0, center_x - box_width // 2)
    y1 = max(0, center_y - box_height // 2)
    x2 = min(width, center_x + box_width // 2)
    y2 = min(height, center_y + box_height // 2)
    
    # Return bounding box and generic "Food" label
    return [(x1, y1, x2, y2, "Food")]

def highlight_food_areas(image_array):
    """
    Create a visualization that highlights food areas in the image
    
    Args:
        image_array: Input image as numpy array
        
    Returns:
        Image with highlighted food areas
    """
    # Get food detections
    detections = detect_food_in_image(image_array)
    
    # Create a copy of the image for drawing
    vis_image = image_array.copy()
    
    # Draw bounding boxes
    for x1, y1, x2, y2, label in detections:
        # Draw rectangle
        cv2.rectangle(vis_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        # Draw label
        cv2.putText(vis_image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    return vis_image
