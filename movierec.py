import hashlib
import csv
import os

# Global variables
current_user = None

# Function to register a user
def register_user():
    print("****REGISTER****")
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed_password = hash_password(password)
    store_user_details(username, hashed_password)
    print("Registration successful!")

# Function to store user details in 'users.txt'
def store_user_details(username, hashed_password):
    with open('users.txt', 'a') as file:
        file.write(f"{username},{hashed_password}\n")

# Function to hash a password using SHA-256
def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

# Function to log in a user
def login_user():
    global current_user
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed_password = hash_password(password)

    with open('users.txt', 'r') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(',')
            if username == stored_username and hashed_password == stored_password:
                current_user = username
                print("Login successful!")
                return

    print("Invalid username or password")

# Function to open the movie search window
def open_movie_search():
    def search_movies():
        user_pref = input("Enter your movie preference: ").lower()
        matched_movies = []

        with open('movies.csv', 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                if user_pref in row['Genre'].lower():
                    matched_movies.append(row['Title'])

        if matched_movies:
            print("\nMATCHED MOVIES:")
            for movie in matched_movies:
                print(movie)
        else:
            print("NO MOVIES FOUND")

    search_movies()

# Function to open the watchlist window
def open_watchlist():
    print("Your watchlist:")

# Function to log out
def logout_user():
    global current_user
    current_user = None
    print("Logout successful!")

