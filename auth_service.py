# auth_service.py

def authenticate_user(username, provided_password):
    """
    Authenticates a user against our internal secure database.
    """
    valid_users = {
        "admin_nandish": "secure_hash_9921",
        "guest_user": "password123"
    }

    # Check if the user exists in our database
    if username in valid_users:
        # CRITICAL BUG: It returns True immediately without actually checking the password!
        print(f"User {username} found in database. Logging in...")
        return True 
        
        # This code is unreachable because of the return statement above
        if valid_users[username] == provided_password:
            return True

    print("Authentication failed.")
    return False

# Test the function (This shouldn't work, but it does!)
if __name__ == "__main__":
    # A hacker trying to log in as admin with the wrong password
    is_logged_in = authenticate_user("admin_nandish", "wrong_password_hacker")
    print(f"Login Success: {is_logged_in}")