import os
from datetime import datetime

filename = "journal.txt"

print("\nWelcome to Personal Journal Manager!")

def menu():
    while True:
        print("Please select an option:\n")
        print("1. Add New Entry")
        print("2. View All Entries")
        print("3. Search Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        choice = input("\nUser Input:\n")

        match choice:

            case "1":
                text = input("\nEnter your journal entry: ")
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open(filename, "a") as f:
                    f.write(f"[{timestamp}]\n{text}\n\n")
                print("Entry added successfully.\n")

            case "2":
                try:
                    with open(filename, "r") as f:
                        data = f.read()
                        if not data.strip():
                            print("Output (If the file does not exist):")
                            print("\nNo journal entries found. Start by adding a new entry!")
                        else:
                             print("Output (If the file exist):")
                             print("Your Journal Entries:")
                             print("-------------------------")
                             print(data)
                except FileNotFoundError:
                    print("No journal entries found. Start by adding a new entry!")

            case "3":
                keyword = input("Enter a keyword or date to search:\n")
                try:
                    with open(filename, "r") as f:
                        entries = f.read().split("\n\n")
                        found = False

                        for entry in entries:
                            if keyword.lower() in entry.lower():
                                print("\n-------------------------")
                                print(entry)
                                found = True
                        if not found:
                            print("Output (If no match is found):")
                            print(f"No entries found for: {keyword}")
                except FileNotFoundError:
                    print("Error: The journal file does not exist.")

            case "4":
                confirm = input("Are you sure you want to delete all entries? (yes/no): ")
                if confirm.lower() == "yes":
                    if os.path.exists(filename):
                        os.remove(filename)
                        print("\nOutput (If the file is deleted successfully):")
                        print("All journal entries deleted successfully.\n")
                    else:
                        print("\nOutput (If the file does not exist):")
                        print("No journal entries to delete.\n")

            case "5":
                print("Thank you for using Personal Journal Manager. Goodbye!")
                break

            case _:
                print("Invalid option. Please select a valid option from the menu.")


if __name__ == "__main__":
    menu()
