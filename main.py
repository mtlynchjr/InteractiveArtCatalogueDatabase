import ui # Connect to ui.py module
import db # Connect to db.py module

while True:
    print('Please select an option from the menu below. Enter "Q" to quit.')
    print("1. Add Artist\n2. Add Artwork\n3. Search by Artist\n4. Delete Artwork\n5. Display Artist's Work\n6. Change Artwork Availablity")

    option = input("Enter your desired option: ")

    if option == "1":
        add_new_artist()
    elif task == "2":
        
