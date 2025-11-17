# Name: Suhanee Gupta
# Date: 17-Nov-2025
# Project Title: Contact Book - File Handling System in Python



# Description:
# A Python-based Contact Management System that allows users to
# add, view, search, update, delete, and export contacts using
# CSV and JSON file handling with exception and error logging.


import csv
import json
import datetime

CSV_FILE = "contacts.csv"
JSON_FILE = "contacts.json"
ERROR_LOG = "error_log.txt"

def log_error(operation, error_msg):
    """Logs error messages with timestamp and operation name."""
    with open(ERROR_LOG, "a") as log:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{timestamp}] Operation: {operation} | Error: {error_msg}\n")


def welcome():                                  # Welcome in the contact manager that will help managing different contacts
    print("===========================================")
    print("          WELCOME TO CONTACT BOOK          ")
    print("===========================================")
    print("This tool helps you manage contacts using CSV and JSON files.")
    print("You can add, view, search, update, and delete contacts in this program\n")


def Contacts():                              # Here it will add contacts 
    try:
        name = input("Enter Name: ")
        phone = input("Enter Phone No. : ")
        email = input("Enter Email Address: ")

        contact = {"name": name, "phone": phone, "email": email}

        with open(CSV_FILE, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "phone", "email"])
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(contact)
        print(f"\n Contact {name} added successfully in data\n")

    except Exception as e:
        print(" Invalid contact....Contact is already there or cant add it .....try different NAME")
        log_error("Add Contact", str(e))


def show_contact():                         # will read and display the contact here
    try:
        with open(CSV_FILE, "r") as file:
            reader = csv.DictReader(file)
            contacts = list(reader)

            if not contacts:
                print("\n No contacts found...add some contact first \n")
                return

            print("\n===== CONTACT LIST =====")
            print(f"{'Name':<20}{'Phone':<15}{'Email'}")
            print("-" * 50)
            for c in contacts:
                print(f"{c['name']:<20}{c['phone']:<15}{c['email']}")
            print("-" * 50)

    except FileNotFoundError:
        print(" No contact file found-------> Add contacts first.")
        log_error("View Contacts", "File not found.")
    except Exception as e:
        print(" Error displaying contacts.")
        log_error("View Contacts", str(e))

def search_contact(name):                    # Here it will seacrh the conatct
    try:
        with open(CSV_FILE, "r") as file:
            reader = csv.DictReader(file)
            for c in reader:
                if c["name"].lower() == name.lower():
                    print("\nContact Found:")
                    print(f"Name: {c['name']}\nPhone: {c['phone']}\nEmail: {c['email']}")
                    return
        print("\n Contact not found.....try with different name\n")
    except Exception as e:
        log_error("Search Contact", str(e))


def update(name):                             # will update the conatact in data/ memory
    try:
        contacts = []
        found = False
        with open(CSV_FILE, "r") as file:
            reader = csv.DictReader(file)
            for c in reader:
                if c["name"].lower() == name.lower():
                    found = True
                    print("\nEnter new details (leave blank to keep existing):")
                    phone = input(f"New Phone ({c['phone']}): ") or c["phone"]
                    email = input(f"New Email ({c['email']}): ") or c["email"]
                    c["phone"], c["email"] = phone, email
                contacts.append(c)

        if found:
            with open(CSV_FILE, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["name", "phone", "email"])
                writer.writeheader()
                writer.writerows(contacts)
            print(f"\n Contact '{name}' updated successfully.\n")
        else:
            print("\n Contact not found.\n")

    except Exception as e:
        log_error("Update Contact", str(e))


def delete(name):                          # will delete the conatct
    try:
        contacts = []
        found = False
        with open(CSV_FILE, "r") as file:
            reader = csv.DictReader(file)
            for c in reader:
                if c["name"].lower() != name.lower():
                    contacts.append(c)
                else:
                    found = True

        if found:
            with open(CSV_FILE, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["name", "phone", "email"])
                writer.writeheader()
                writer.writerows(contacts)
            print(f"\n Contact '{name}' deleted successfully.\n")
        else:
            print("\n The conatct is already deleted it doesnt exist \n")

    except Exception as e:
        log_error("Delete Contact", str(e))

def export_to_json():                    #saving json file from csv
    try:
        with open(CSV_FILE, "r") as file:
            reader = csv.DictReader(file)
            contacts = list(reader)

        with open(JSON_FILE, "w") as json_file:
            json.dump(contacts, json_file, indent=4)
        print("\n✅ Contacts exported to contacts.json\n")

    except Exception as e:
        log_error("Export to JSON", str(e))


def import_from_json():
    try:
        with open(JSON_FILE, "r") as file:
            contacts = json.load(file)

        print("\n===== CONTACTS FROM JSON =====")
        print(f"{'Name':<20}{'Phone':<15}{'Email'}")
        print("-" * 50)
        for c in contacts:
            print(f"{c['name']:<20}{c['phone']:<15}{c['email']}")
        print("-" * 50)

    except FileNotFoundError:
        print("⚠️ No JSON file found.")
        log_error("Import from JSON", "File not found.")
    except Exception as e:
        log_error("Import from JSON", str(e))

def main():                                       # menu for whole operations
    welcome()
    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Export to JSON")
        print("7. Import from JSON")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            Contacts()
        elif choice == "2":
            show_contact()
        elif choice == "3":
            name = input("Enter name to search: ")
            search_contact(name)
        elif choice == "4":
            name = input("Enter name to update: ")
            update(name)
        elif choice == "5":
            name = input("Enter name to delete: ")
            delete(name)
        elif choice == "6":
            export_to_json()
        elif choice == "7":
            import_from_json()
        elif choice == "8":
            print("\nExiting Contact Book. Goodbye!")
            break
        else:
            print(" Your choice doesnt exists , please try again.")
if __name__ == "__main__":
    main()
