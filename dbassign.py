
# Build a Dummy database for Slightly Techie (Name and class)
# Access database with the correct password else the user keeps trying till the correct password is given
# Have a menu to do the following
# Clear, update, and print out the database

# Brainstorm
# Setup up database
# password credetials
# print optins for the user
# Loop to handle user access.
# Print database
# take user input for option and password
# write logic to clear and update database


students = {"Ben":"Backend", "Gilbert":"Frontend","Sadiq":"Backend"}

password = '1234asdf'

print('Welcome to ST Database\n')
print("To get Access, Enter the Password")

entry = input("Enter Password: ")

while entry != password:
   
    entry = input("Wrong password. Try again: ")

print("Access Granted")
print("Choose a Number for an option")

def print_menu():
    print("\nChoose an option:")
    print("1. Clear")
    print("2. Update")
    print("3. Print Database")
    print("4. Remove an item")
    print("5. Change key or value of an item")
    print("6. Exit")

while True:
    print_menu()
    try:
         choice = int(input("Choose an option \n 1. Clear: \n 2. Update: \n 3. Print Database: \n 4. Exit"))
    except ValueError:
        print('Input is invalid. Enter a number instead.')
    continue

    if choice == 1:
        students.clear()
        print("Database Cleared")
    elif choice == 2:
        name = input("Enter name")
        class_name = input("Enter Class")
        students[name] = class_name
        print("Successfully Updated")
    elif choice == 3:
        print(students)
    elif choice == 4:
        print("All done")
        break
    else:
        print("Invalid choice. Select a valid option")
