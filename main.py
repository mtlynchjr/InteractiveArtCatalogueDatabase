import ui  # Import all from to ui.py module
import db # Import all from db.py module

def main(): # Create main function

    # While main function is active do the following ...
    while True:
        # Welcome and instruct the user
        print("Welcome to the Interactive Art Catolouge!\n")
        print('Please select an option from the menu below: (Enter "Q" to Quit)')
        print("1. Add Artist\n2. Add Artwork\n3. Search by Artist\n4. Delete Artwork\n5. Display Artist's Work\n6. Change Artwork Availablity\n7. Display Artist's Available Artwork\n")

        option = ui.get_non_empty_string(input("Enter your desired option: "))

        # Explain user options
        if option == "1":
            add_new_artist()
        elif option == "2":
            add_new_artwork()
        elif option == "3":
            search_by_artist()
        elif option == "4":
            delete_artwork()
        # elif option == "5":
            # change_availability()
        elif option == "6":
            available_artwork()
        # Provide option for user to quit
        elif option == "q" or option == "Q":
            good_bye()
        break

def add_new_artist(): # Create Add New Artist function
    # Prompt user for new artist's name
    new_artist_name = ui.get_non_empty_string(input(
        "What is the name of the artist you would like to add? "))
    # Prompt user for new artist's e-mail address
    new_artist_email = ui.get_non_empty_string(
        input("Please enter the e-mail address of the artist you would like to add: "))
    # Update database with values
    db.add_new_artist(new_artist_name, new_artist_email)

def add_new_artwork(): # Create Add New Artwork function
    # Prompt user for new artworks's name
    new_artwork = ui.get_non_empty_string(input(
        "What is the name of the artwork you would like to add? "))
    # Prompt user for new artwork's artist
    new_artist = ui.get_non_empty_string(
        input("What is the name of the artist attributed to that artwork? "))
    # Prompt user for new artwork's price
    new_price = ui.get_positive_float(
        float(input("How much does the artwork cost? $")))
    # Prompt user for new artwork's availability
    new_avaiability = ui.get_non_empty_string(
        input("Is the artwork currently available for purchase? Y/N: "))
    # Make yes True and no False
    if new_avaiability == "y" or "Y":
        True
    else:
        False
    # Update database with values
    db.add_new_artwork(new_artwork, new_artist, new_price, new_avaiability)

def search_by_artist(): # Create Search by Artist function
    # Prompt user for artist name
    search_artist = ui.get_non_empty_string(input(
        "What is the name of the artist whose available artworks you want to see? "))
    # Update database with values
    db.search_by_artist(search_artist, )

def delete_artwork(): # Create Delete Artwork function
    # Prompt user for artwork to be deleted
    deleted_artwork = ui.get_non_empty_string(
        input("What is the name of the artwork you would like to remove? "))
    # Update database with values
    db.delete_artwork(deleted_artwork, )

def available_artwork(): # Create Available Artwork function
    # Prompt user for artist's name
    available_artist = ui.get_non_empty_string(input(
        "What is the name of the artist whose available artworks you want to see? "))
    # Update database with values
    db.available_artwork(available_artist, )

def good_bye(): # Create good-bye/quit function
    print("Good-bye!")

# Run main
if __name__ == "__main__":
    main()
