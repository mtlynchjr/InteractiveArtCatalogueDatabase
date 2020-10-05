import ui # Connect to ui.py module
import db

while True:
    print("Welcome to the Interactive Art Catolouge!\n")
    print('Please select an option from the menu below: (Enter "Q" to Quit)')
    print("1. Add Artist\n2. Add Artwork\n3. Search by Artist\n4. Delete Artwork\n5. Display Artist's Work\n6. Change Artwork Availablity\n7. Display Artist's Available Artwork")

    option = input("Enter your desired option: ")

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
    elif option == "q" or option == "Q":
        good_bye()
        break

def add_new_artist():
    new_artist_name = ui.get_non_empty_string(input("What is the name of the artist you would like to add? ")) # Prompt useer for new artist's name
    new_artist_email = ui.get_non_empty_string(input("Please enter the e-mail address of the artist you would like to add: ")) # Prompt useer for new artist's e-mail address
    db.add_new_artist(new_artist_name, new_artist_email)

def add_new_artwork():
    new_artwork = ui.get_non_empty_string(input("What is the name of the artwork you would like to add? ")) # Prompt user for new artworks's name
    new_artist = ui.get_non_empty_string(input("What is the name of the artist attributed to that artwork? ")) # Prompt user for new artwork's artist
    new_price = ui.get_positive_float(float(input("How much does the artwork cost? $"))) # Prompt user for new artwork's price.
    new_avaiability = ui.get_non_empty_string(input("Is the artwork currently available for purchase? ")) # Prompt user for new artwork's availability
    db.add_new_artwork(new_artwork, new_artist, new_price, new_avaiability)

def search_by_artist():
    search_artist = ui.get_non_empty_string(input("What is the name of the artist whose available artworks you want to see? "))
    db.search_by_artist(search_artist, )

def delete_artwork():
    deleted_artwork = ui.get_non_empty_string(input("What is the name of the artwork you would like to remove? "))
    db.delete_artwork(deleted_artwork, )

# def change_availability():
    # available_update = ui.VALIDATION(input("What is the name of the artwork whose availability you would like to update? "))
    # db.change_availability(availabile_update, )

def available_artwork():
    available_artist = ui.get_non_empty_string(input("What is the name of the artist whose available artworks you want to see? "))
    db.available_artwork(available_artist, )

def good_bye():
    print("Good-bye!")

