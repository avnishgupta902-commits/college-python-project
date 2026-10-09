import json
import os

# ============================================================
# COLLEGE EVENT REGISTRATION SYSTEM
# ============================================================

registrations = []

events = [
    "Coding Competition",
    "Quiz Competition",
    "Dance Competition",
    "Singing Competition",
    "Debate Competition",
    "Poster Making",
    "Sports Event"
]


FILE_NAME = "registrations.json"


# ============================================================
# DISPLAY MAIN MENU
# ============================================================

def show_menu():
    print("\n")
    print("=" * 55)
    print("          COLLEGE EVENT REGISTRATION SYSTEM")
    print("=" * 55)
    print("1. Register Student")
    print("2. View Registrations")
    print("3. Search Student")
    print("4. Update Registration")
    print("5. Delete Registration")
    print("6. View Events")
    print("7. View Statistics")
    print("8. Save Data")
    print("9. Load Data")
    print("10. Clear All Registrations")
    print("11. Exit")
    print("=" * 55)


# ============================================================
# REGISTER STUDENT
# ============================================================

def register_student():

    print("\n")
    print("-" * 40)
    print("        STUDENT REGISTRATION")
    print("-" * 40)

    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    department = input("Enter department: ")
    year = input("Enter year: ")

    print("\nAvailable Events:")

    for i in range(len(events)):
        print(i + 1, ".", events[i])

    choice = input("Choose event number: ")

    if not choice.isdigit():
        print("Invalid event choice.")
        return

    choice = int(choice)

    if choice < 1 or choice > len(events):
        print("Invalid event choice.")
        return

    event = events[choice - 1]

    # Check duplicate roll number
    for student in registrations:

        if student["roll"] == roll:
            print("\nStudent with this roll number already exists.")
            return

    student = {
        "name": name,
        "roll": roll,
        "email": email,
        "phone": phone,
        "department": department,
        "year": year,
        "event": event
    }

    registrations.append(student)

    print("\nRegistration successful!")
    print("Student:", name)
    print("Event:", event)


# ============================================================
# VIEW REGISTRATIONS
# ============================================================

def view_registrations():

    print("\n")
    print("-" * 100)
    print("                         ALL REGISTRATIONS")
    print("-" * 100)

    if len(registrations) == 0:
        print("No registrations found.")
        return

    for i, student in enumerate(registrations, start=1):

        print("\nRegistration", i)
        print("Name       :", student["name"])
        print("Roll No    :", student["roll"])
        print("Email      :", student["email"])
        print("Phone      :", student["phone"])
        print("Department :", student["department"])
        print("Year       :", student["year"])
        print("Event      :", student["event"])

        print("-" * 50)


# ============================================================
# SEARCH STUDENT
# ============================================================

def search_student():

    print("\n")
    print("-" * 40)
    print("          SEARCH STUDENT")
    print("-" * 40)

    search = input(
        "Enter student name or roll number: "
    )

    found = False

    for student in registrations:

        if (
            search.lower() in student["name"].lower()
            or search.lower() == student["roll"].lower()
        ):

            print("\nStudent Found!")
            print("Name       :", student["name"])
            print("Roll No    :", student["roll"])
            print("Email      :", student["email"])
            print("Phone      :", student["phone"])
            print("Department :", student["department"])
            print("Year       :", student["year"])
            print("Event      :", student["event"])

            found = True

    if not found:
        print("\nNo student found.")


# ============================================================
# UPDATE REGISTRATION
# ============================================================

def update_student():

    print("\n")
    print("-" * 40)
    print("        UPDATE REGISTRATION")
    print("-" * 40)

    roll = input("Enter roll number to update: ")

    for student in registrations:

        if student["roll"] == roll:

            print("\nCurrent Details")
            print("Name:", student["name"])
            print("Email:", student["email"])
            print("Phone:", student["phone"])
            print("Department:", student["department"])
            print("Year:", student["year"])
            print("Event:", student["event"])

            print("\nEnter new details.")

            name = input("Enter new name: ")
            email = input("Enter new email: ")
            phone = input("Enter new phone: ")
            department = input("Enter new department: ")
            year = input("Enter new year: ")

            print("\nAvailable Events:")

            for i in range(len(events)):
                print(i + 1, ".", events[i])

            choice = input("Choose new event number: ")

            if choice.isdigit():

                choice = int(choice)

                if 1 <= choice <= len(events):
                    student["event"] = events[choice - 1]

            student["name"] = name
            student["email"] = email
            student["phone"] = phone
            student["department"] = department
            student["year"] = year

            print("\nRegistration updated successfully!")

            return

    print("\nStudent not found.")


# ============================================================
# DELETE REGISTRATION
# ============================================================

def delete_student():

    print("\n")
    print("-" * 40)
    print("        DELETE REGISTRATION")
    print("-" * 40)

    roll = input("Enter roll number: ")

    for student in registrations:

        if student["roll"] == roll:

            print("\nStudent found:")
            print("Name:", student["name"])
            print("Event:", student["event"])

            confirm = input(
                "Are you sure you want to delete? (yes/no): "
            )

            if confirm.lower() == "yes":

                registrations.remove(student)

                print("\nRegistration deleted successfully.")

            else:

                print("\nDeletion cancelled.")

            return

    print("\nStudent not found.")


# ============================================================
# VIEW EVENTS
# ============================================================

def view_events():

    print("\n")
    print("-" * 40)
    print("           COLLEGE EVENTS")
    print("-" * 40)

    for i, event in enumerate(events, start=1):

        print(i, ".", event)

    print("-" * 40)


# ============================================================
# VIEW STATISTICS
# ============================================================

def view_statistics():

    print("\n")
    print("-" * 45)
    print("          REGISTRATION STATISTICS")
    print("-" * 45)

    total = len(registrations)

    print("Total Registrations:", total)

    print()

    for event in events:

        count = 0

        for student in registrations:

            if student["event"] == event:
                count += 1

        print(event, ":", count)


# ============================================================
# SAVE DATA
# ============================================================

def save_data():

    try:

        with open(FILE_NAME, "w") as file:

            json.dump(
                registrations,
                file,
                indent=4
            )

        print("\nData saved successfully.")

    except Exception:

        print("\nError while saving data.")


# ============================================================
# LOAD DATA
# ============================================================

def load_data():

    global registrations

    if not os.path.exists(FILE_NAME):

        print("\nNo previous data found.")

        return

    try:

        with open(FILE_NAME, "r") as file:

            registrations = json.load(file)

        print("\nData loaded successfully.")

    except Exception:

        print("\nError while loading data.")

        registrations = []


# ============================================================
# CLEAR ALL REGISTRATIONS
# ============================================================

def clear_all():

    print("\n")
    print("-" * 40)
    print("       CLEAR ALL REGISTRATIONS")
    print("-" * 40)

    if len(registrations) == 0:

        print("There are no registrations.")

        return

    confirm = input(
        "Delete ALL registrations? (yes/no): "
    )

    if confirm.lower() == "yes":

        registrations.clear()

        save_data()

        print("\nAll registrations have been deleted.")

    else:

        print("\nOperation cancelled.")


# ============================================================
# PROGRAM INFORMATION
# ============================================================

def about():

    print("\n")
    print("=" * 50)
    print("        ABOUT THE PROGRAM")
    print("=" * 50)

    print("College Event Registration System")
    print()
    print("This program is used to manage")
    print("college event registrations.")
    print()
    print("Features:")
    print("- Student registration")
    print("- Search student")
    print("- Update registration")
    print("- Delete registration")
    print("- Event list")
    print("- Registration statistics")
    print("- Save and load data")
    print("=" * 50)


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    print("\n")
    print("=" * 55)
    print("       WELCOME TO COLLEGE EVENT REGISTRATION")
    print("=" * 55)

    load_data()

    while True:

        show_menu()

        choice = input(
            "Enter your choice: "
        )

        if choice == "1":

            register_student()

        elif choice == "2":

            view_registrations()

        elif choice == "3":

            search_student()

        elif choice == "4":

            update_student()

        elif choice == "5":

            delete_student()

        elif choice == "6":

            view_events()

        elif choice == "7":

            view_statistics()

        elif choice == "8":

            save_data()

        elif choice == "9":

            load_data()

        elif choice == "10":

            clear_all()

        elif choice == "11":

            print("\nSaving data...")
            save_data()

            print("\nThank you for using")
            print("College Event Registration System!")

            break

        elif choice.lower() == "a":

            about()

        else:

            print("\nInvalid choice.")
            print("Please enter a number from 1 to 11.")


# ============================================================
# START PROGRAM
# ============================================================

if __name__ == "__main__":

    main()