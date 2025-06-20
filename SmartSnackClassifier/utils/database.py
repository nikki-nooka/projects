import sqlite3
import os
import hashlib
import time
import json

# Database setup
DB_PATH = "users.db"

def get_db_connection():
    """Create a database connection and return the connection object"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # This enables column access by name
    return conn

def init_db():
    """Initialize the database with required tables"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        email TEXT,
        created_at TEXT NOT NULL,
        last_login TEXT
    )
    ''')
    
    # Create user activity table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_activity (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        activity_type TEXT NOT NULL,
        details TEXT,
        timestamp TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    ''')
    
    # Create user preferences table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_preferences (
        user_id INTEGER PRIMARY KEY,
        dietary_restrictions TEXT,
        favorite_foods TEXT,
        disliked_foods TEXT,
        health_goals TEXT,
        theme TEXT,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    ''')
    
    conn.commit()
    conn.close()

def hash_password(password):
    """Hash a password for storing"""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password, email=None):
    """Register a new user in the database"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Check if user already exists
        cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
        if cursor.fetchone():
            conn.close()
            return False, "Username already exists"
        
        # Hash the password
        password_hash = hash_password(password)
        
        # Insert the new user
        cursor.execute(
            "INSERT INTO users (username, password_hash, email, created_at) VALUES (?, ?, ?, ?)",
            (username, password_hash, email, time.strftime("%Y-%m-%d %H:%M:%S"))
        )
        
        # Get the user ID
        user_id = cursor.lastrowid
        
        # Create default preferences
        cursor.execute(
            "INSERT INTO user_preferences (user_id) VALUES (?)",
            (user_id,)
        )
        
        conn.commit()
        conn.close()
        return True, user_id
    except Exception as e:
        conn.rollback()
        conn.close()
        return False, str(e)

def authenticate_user(username, password):
    """Authenticate a user and return user information if successful"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Hash the provided password
    password_hash = hash_password(password)
    
    # Look for matching user
    cursor.execute(
        "SELECT id, username FROM users WHERE username = ? AND password_hash = ?",
        (username, password_hash)
    )
    
    user = cursor.fetchone()
    
    if user:
        # Update last login time
        cursor.execute(
            "UPDATE users SET last_login = ? WHERE id = ?",
            (time.strftime("%Y-%m-%d %H:%M:%S"), user['id'])
        )
        conn.commit()
        
        # Get user data
        user_data = {
            "id": user['id'],
            "username": user['username'],
            "logged_in": True
        }
        
        conn.close()
        return True, user_data
    
    conn.close()
    return False, "Invalid username or password"

def log_user_activity(user_id, activity_type, details=None):
    """Log user activity to the database"""
    if not user_id:
        return False
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Convert details to JSON string if it's a dictionary
        if details and isinstance(details, dict):
            details = json.dumps(details)
        
        cursor.execute(
            "INSERT INTO user_activity (user_id, activity_type, details, timestamp) VALUES (?, ?, ?, ?)",
            (user_id, activity_type, details, time.strftime("%Y-%m-%d %H:%M:%S"))
        )
        
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        conn.rollback()
        conn.close()
        return False

def get_user_activity(user_id, limit=10):
    """Get recent user activity from the database"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT activity_type, details, timestamp FROM user_activity WHERE user_id = ? ORDER BY timestamp DESC LIMIT ?",
        (user_id, limit)
    )
    
    activities = []
    for row in cursor.fetchall():
        activity = {
            "activity": row['activity_type'],
            "timestamp": row['timestamp']
        }
        
        # Parse JSON details if present
        if row['details']:
            try:
                activity["details"] = json.loads(row['details'])
            except:
                activity["details"] = row['details']
        
        activities.append(activity)
    
    conn.close()
    return activities

def get_user_preferences(user_id):
    """Get user preferences from the database"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT * FROM user_preferences WHERE user_id = ?",
        (user_id,)
    )
    
    row = cursor.fetchone()
    conn.close()
    
    if not row:
        return {}
    
    preferences = dict(row)
    
    # Convert JSON strings to dictionaries
    for key in ['dietary_restrictions', 'favorite_foods', 'disliked_foods', 'health_goals']:
        if preferences[key]:
            try:
                preferences[key] = json.loads(preferences[key])
            except:
                pass
    
    return preferences

def update_user_preferences(user_id, preferences):
    """Update user preferences in the database"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Convert dictionaries to JSON strings
    for key in ['dietary_restrictions', 'favorite_foods', 'disliked_foods', 'health_goals']:
        if key in preferences and isinstance(preferences[key], (dict, list)):
            preferences[key] = json.dumps(preferences[key])
    
    # Update the preferences
    try:
        cursor.execute(
            """
            UPDATE user_preferences 
            SET dietary_restrictions = COALESCE(?, dietary_restrictions),
                favorite_foods = COALESCE(?, favorite_foods),
                disliked_foods = COALESCE(?, disliked_foods),
                health_goals = COALESCE(?, health_goals),
                theme = COALESCE(?, theme)
            WHERE user_id = ?
            """,
            (
                preferences.get('dietary_restrictions'),
                preferences.get('favorite_foods'),
                preferences.get('disliked_foods'),
                preferences.get('health_goals'),
                preferences.get('theme'),
                user_id
            )
        )
        
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        conn.rollback()
        conn.close()
        return False

# Initialize the database when the module is imported
init_db()