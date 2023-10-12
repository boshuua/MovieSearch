import hashlib
import csv
import os
import tkinter as tk
from tkinter import messagebox

# Global variables
current_user = None

# Create the main Tkinter window
root = tk.Tk()
root.title("Movies Watchlist System")


# Function to display a message in a pop-up window
def show_message(title, message):
  messagebox.showinfo(title, message)


# Function to register a user
def register_user():
  username = register_username_entry.get()
  password = register_password_entry.get()
  hashed_password = hash_password(password)
  store_user_details(username, hashed_password)
  show_message("Registration", "Registration successful!")


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
  username = login_username_entry.get()
  password = login_password_entry.get()
  hashed_password = hash_password(password)

  with open('users.txt', 'r') as file:
    for line in file:
      stored_username, stored_password = line.strip().split(',')
      if username == stored_username and hashed_password == stored_password:
        current_user = username
        show_message("Login", "Login successful!")
        return

  show_message("Login Error", "Invalid username or password")


def open_movie_search():

  def search_movies():
    user_pref = movie_search_entry.get().strip().lower()
    matched_movies = []

    with open('movies.csv', 'r') as file:
      reader = csv.DictReader(file)

      for row in reader:
        if user_pref in row['Title'].lower(
        ) or user_pref in row['Genre'].lower():
          matched_movies.append(row['Title'])

    if matched_movies:
      result_label.config(text="\nMATCHED MOVIES:")
      for movie in matched_movies:
        result_label.config(text=result_label.cget("text") + "\n" + movie)
    else:
      result_label.config(text="NO MOVIES FOUND")

  movie_search_window = tk.Toplevel(root)
  movie_search_window.title("Movie Search")

  movie_search_label = tk.Label(movie_search_window,
                                text="Enter a movie title or genre:")
  movie_search_label.pack()

  movie_search_entry = tk.Entry(movie_search_window)
  movie_search_entry.pack()

  search_button = tk.Button(movie_search_window,
                            text="Search",
                            command=search_movies)
  search_button.pack()

  result_label = tk.Label(movie_search_window, text="")
  result_label.pack()

  close_movie_search_button = tk.Button(movie_search_window,
                                        text="Close",
                                        command=movie_search_window.destroy)
  close_movie_search_button.pack()


# ...
# Add the movie search functionality here
# Function to open the movie search window
def open_movie_search():

  def search_movies():
    user_pref = movie_search_entry.get().lower()
    matched_movies = []

    with open('movies.csv', 'r') as file:
      reader = csv.DictReader(file)

      for row in reader:
        if user_pref in row['Genre'].lower():
          matched_movies.append(row['Title'])

    if matched_movies:
      result_label.config(text="\nMATCHED MOVIES:")
      for movie in matched_movies:
        result_label.config(text=result_label.cget("text") + "\n" + movie)
    else:
      result_label.config(text="NO MOVIES FOUND")

  movie_search_window = tk.Toplevel(root)
  movie_search_window.title("Movie Search")

  movie_search_label = tk.Label(movie_search_window,
                                text="Enter your movie preference:")
  movie_search_label.pack()

  movie_search_entry = tk.Entry(movie_search_window)
  movie_search_entry.pack()

  search_button = tk.Button(movie_search_window,
                            text="Search",
                            command=search_movies)
  search_button.pack()

  result_label = tk.Label(movie_search_window, text="")
  result_label.pack()

  close_movie_search_button = tk.Button(movie_search_window,
                                        text="Close",
                                        command=movie_search_window.destroy)
  close_movie_search_button.pack()

  # ...

  # Close the movie search window when done
  close_movie_search_button = tk.Button(movie_search_window,
                                        text="Close",
                                        command=movie_search_window.destroy)
  close_movie_search_button.pack()


# Function to open the watchlist window
def open_watchlist():
  watchlist_window = tk.Toplevel(root)
  watchlist_window.title("Watchlist")
  watchlist_label = tk.Label(watchlist_window, text="Your watchlist:")
  watchlist_label.pack()
  # Add the watchlist functionality here
  # ...
  # Close the watchlist window when done
  close_watchlist_button = tk.Button(watchlist_window,
                                     text="Close",
                                     command=watchlist_window.destroy)
  close_watchlist_button.pack()


# Function to log out
def logout_user():
  global current_user
  current_user = None
  show_message("Logout", "Logout successful!")


# Create and set up the registration frame
registration_frame = tk.Frame(root)
registration_frame.pack()
register_label = tk.Label(registration_frame, text="Register a new user")
register_label.pack()
register_username_label = tk.Label(registration_frame, text="Username:")
register_username_label.pack()
register_username_entry = tk.Entry(registration_frame)
register_username_entry.pack()
register_password_label = tk.Label(registration_frame, text="Password:")
register_password_label.pack()
register_password_entry = tk.Entry(registration_frame, show="*")
register_password_entry.pack()
register_button = tk.Button(registration_frame,
                            text="Register",
                            command=register_user)
register_button.pack()

# Create and set up the login frame
login_frame = tk.Frame(root)
login_frame.pack()
login_label = tk.Label(login_frame, text="Log in")
login_label.pack()
login_username_label = tk.Label(login_frame, text="Username:")
login_username_label.pack()
login_username_entry = tk.Entry(login_frame)
login_username_entry.pack()
login_password_label = tk.Label(login_frame, text="Password:")
login_password_label.pack()
login_password_entry = tk.Entry(login_frame, show="*")
login_password_entry.pack()
login_button = tk.Button(login_frame, text="Login", command=login_user)
login_button.pack()

# Create and set up the main menu
menu_label = tk.Label(root, text="Main Menu")
menu_label.pack()
movie_search_button = tk.Button(root,
                                text="Movie Search",
                                command=open_movie_search)
movie_search_button.pack()
watchlist_button = tk.Button(root, text="Watchlist", command=open_watchlist)
watchlist_button.pack()
logout_button = tk.Button(root, text="Logout", command=logout_user)
logout_button.pack()
exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack()

# Start the main Tkinter event loop
root.mainloop()
