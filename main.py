import ui # Connect to ui.py module
import db # Connect to db.py module

while True:

    print('Please select an option from the menu below. Enter "Q" to quit.')
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
    elif option == "5":
        change_availability()
    elif option == "6":
        available_artwork()
    elif option == "q" or option == "Q":
        break
    else:
        print("You did not choose a valid option.")
        break

# add_new_artist()
# add_new_artwork()
# search_by_artist()
# delete_artwork()
# display_artist_artwork()
# change_availability()
# display_available_artwork()
