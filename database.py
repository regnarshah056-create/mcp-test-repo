import sqlite3


def get_user_data(username):
    """Fetches user data from the database."""
    conn = sqlite3.connect('app_data.db')
    cursor = conn.cursor()

    # Using parameterized queries to prevent SQL Injection
    query = "SELECT * FROM users WHERE username = ?"
    
    print(f"Executing: {query} with username = {username}")
    cursor.execute(query, (username,))
    
    data = cursor.fetchall()
    conn.close()
    return data

if __name__ == "__main__":
    # Simulate a hacker bypassing the login
    print(get_user_data("hacker' OR '1'='1"))