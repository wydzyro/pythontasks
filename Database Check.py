user_added = False
username = "Ahmad"

if user_added == True:
        print("User is currently in the database.")
elif user_added == False:
        print("Adding user to database")
        user_added = True
        print(f"{username} has been added to the database.")
else:
        print(f"There has been an error adding {username} to the system")