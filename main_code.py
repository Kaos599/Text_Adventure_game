# A simple text adventure game

# Define the rooms and items as strings
cell = "You are in a dark and dirty cell. There is a window to the north and a door to the east. You see a key on the floor."
hall = "You are in a long and narrow hall. There are doors to the east and west."
guard = "You are in a room with a sleeping guard. There is a door to the west and a window to the south. You see a gun on the table."
freedom = "You have escaped from the prison. You win!"

# Define the player's location as a string
location = cell

# Define the player's inventory as a list
inventory = []

# Start the game loop
while True:
    # Print the current location
    print(location)
    
    # Get the player's input
    choice = input("What do you want to do? ")
    
    # Handle the input based on the current location
    if location == cell:
        # If the player chooses to go east, check if they have the key
        if choice == "go east":
            if "key" in inventory:
                # If they have the key, move them to the hall
                location = hall
            else:
                # If they don't have the key, print an error message
                print("The door is locked.")
        # If the player chooses to take the key, add it to their inventory
        elif choice == "take key":
            inventory.append("key")
            print("You take the key.")
        # If the player chooses anything else, print an error message
        else:
            print("Invalid input.")
            
    elif location == hall:
        # If the player chooses to go east, move them to the guard room
        if choice == "go east":
            location = guard
        # If the player chooses to go west, move them back to the cell
        elif choice == "go west":
            location = cell
        # If the player chooses anything else, print an error message
        else:
            print("Invalid input.")
            
    elif location == guard:
        # If the player chooses to go west, move them back to the hall
        if choice == "go west":
            location = hall
        # If the player chooses to go south, check if they have the gun
        elif choice == "go south":
            if "gun" in inventory:
                # If they have the gun, move them to freedom and end the game
                location = freedom
                print(location)
                break
            else:
                # If they don't have the gun, print an error message
                print("The window is too high.")
        # If the player chooses to take the gun, add it to their inventory
        elif choice == "take gun":
            inventory.append("gun")
            print("You take the gun.")
        # If the player chooses anything else, print an error message
        else:
            print("Invalid input.")
