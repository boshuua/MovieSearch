import hashlib
import csv
import os

# Global variables
current_user = None


def register_user():
    username = input("ENTER A USERNAME: ")
    password = input("ENTER A PASSWORD: ")
    hashed_password = hash_password(password)
    return username, hashed_password

def store_user_details(username, hashed_password):
    with open('users.txt', 'a') as file:
        file.write(f"{username},{hashed_password}\n")

def hash_password(password):
    # Hash the password using SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def login_user():
    global current_user
    username = input("ENTER USERNAME: ")
    password = input("ENTER PASSWORD: ")
    hashed_password = hash_password(password)

    with open('users.txt', 'r') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(',')
            if username == stored_username and hashed_password == stored_password:
                current_user = username
                print("LOGIN SUCCESSFUL!")
                return True

    print("INVALID, PLEASE TRY AGAIN")
    return False

def movie_search():
    if not current_user:
        print("###### PLEASE LOGIN TO ACCESS THE WATCHLIST ######")
        return
    previous_searches =[]
    while True:
        with open('movies.csv', 'r') as file:
            reader = csv.DictReader(file)
            genres = set()

            for row in reader:
                genres.add(row['Genre'])
        
        print("AVAILABLE GENRES:")
        for genre in genres:
            print(genre)
        user_pref = input("ENTER YOUR MOVIE PREFERENCE: ")
        
        with open('movies.csv', 'r') as file:
            reader = csv.DictReader(file)
            matched_movies = []

            for row in reader:
                if user_pref.lower() == row['Genre'].lower():
                    matched_movies.append(row['Title'])
        
        if matched_movies:
            print("\nMATCHED MOVIES:")
            for movie in matched_movies:
                print(movie)
        else:
            print("NO MOVIES FOUND")
        
        choice = input("1. SEARCH AGAIN\n2. BACK TO MAIN MENU\nENTER YOUR CHOICE: ")
        
        if choice == "1":
            continue
        elif choice == "2":
            break
        else:
            print("INVALID CHOICE, RETURNING TO MAIN MENU.")
            break

def watchlist():
    if not current_user:
        print("###### PLEASE LOGIN TO ACCESS THE WATCHLIST ######")
        return

    user_watchlist = []

    while True:
        print("\n#### WATCHLIST MENU ####")
        print("1. ADD MOVIE TO WATCHLIST")
        print("2. REMOVE MOVIES FROM WATCHLIST")
        print("3. VIEW WATCHLIST")
        print("4. SAVE WATCHLIST")
        print("5. BACK TO MAIN MENU")

        choice = input("ENTER YOUR CHOICE: ")

        if choice == "1":
            movie_title = input("ENTER MOVIE TITLE TO ADD: ")
            user_watchlist.append(movie_title)
            print(f"{movie_title} ADDED TO THE WATCHLIST.")
        elif choice == "2":
            movie_title = input("ENTER THE MOVIE TITLE TO REMOVE: ")
            if movie_title in user_watchlist:
                user_watchlist.remove(movie_title)
                print(f"{movie_title} REMOVED FROM WATCHLIST")
        elif choice == "3":
            if user_watchlist:
                print("MOVIES IN WATCHLIST:")
                for movie in user_watchlist:
                    print(movie)
            else:
                print("WATCHLIST IS EMPTY.")
        elif choice == "4":
            save_watchlist(user_watchlist)
        elif choice == "5":
            print("RETURNING TO THE MAIN MENU.")
            break
        else:
            print("INVALID, PLEASE TRY AGAIN")

def save_watchlist(watchlist):
    if not watchlist:
        print("NO MOVIES IN WATCHLIST TO SAVE.")
        return

    filename = f"{current_user}_watchlist.txt"

    with open(filename, 'w') as file:
        for movie in watchlist:
            file.write(movie + '\n')

    print("WATCHLIST SAVED SUCCESSFULLY!")


def logout_user():
    global current_user
    current_user = None
    print("LOGOUT SUCCESSFUL!")

def main_menu():
    print("#### WELCOME TO THE MOVIES WATCHLIST SYSTEM! ####")
    while True:
        print("\n1. REGISTER")
        print("2. LOGIN")
        print("3. LOGOUT")
        print("4. MOVIE SEARCH")
        print("5. WATCHLIST")
        print("6. EXIT")
        choice = input("ENTER YOUR CHOICE: ")

        if choice == "1":
            username, hashed_password = register_user()
            store_user_details(username, hashed_password)
            print("REGISTRATION SUCCESSFUL!")
        elif choice == "2":
            login_user()
        elif choice == "3":
            if current_user:
                logout_user()
            else:
                print("NO USER IS CURRENTLY LOGGED IN")
        elif choice == "4":
            movie_search()
        elif choice == "5":
            watchlist()
        elif choice == "6":
            print("THANK YOU FOR YOUR VISIT!")
            break
        else:
            print("INVALID, TRY AGAIN")

# Call the main_menu() function to start the program
main_menu()
