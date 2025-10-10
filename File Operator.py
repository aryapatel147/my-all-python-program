import os
from datetime import datetime

class JournalManager:
    def _init_(self, filename="journal.txt"):
        self.filename = filename

    def add_entry(self):
        entry = input("Enter your journal entry:\n")
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]\n")
        with open(self.filename, "a") as f:
            f.write(f"{timestamp}\n{entry}\n\n")
        print("Entry added!\n")

    def view_entries(self):
        try:
            with open(self.filename, "r") as f:
                print("\n--- Journal Entries ---")
                print(f.read())
        except FileNotFoundError:
            print("No journal found.\n")

    def search_entries(self):
        keyword = input("Enter a keyword or date to search: ").lower()
        try:
            with open(self.filename, "r") as f:
                content = f.read().strip().split("\n\n")
                found = False
                print("\nMatching Entries:")
                print("-" * 40)
                for entry in content:
                    if keyword in entry.lower():
                        print(entry.strip())
                        print()
                        found = True
                if not found:
                    print(f"No entries were found for the keyword: {keyword}\n")
        except FileNotFoundError:
            print("No journal found.\n")

    def delete_entries(self):
        if os.path.exists(self.filename):
            confirm = input("Are you sure you want to delete all entries? (yes/no): ")
            print("\noutput (if the file is deleted successfully):")
            if confirm.lower() == "yes":
                os.remove(self.filename)
                print("All journal entries have been deleted!\n")
            else:
                print("Cancelled.\n")
        else:
            print("No journal found.\n")


def main():
    jm = JournalManager()
    while True:
        print("Welcome to Personal Journal Manager!")
        print("\nPlease select an option:")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        choice = input("User Input: \n")

        if choice == "1":
            jm.add_entry()
        elif choice == "2":
            jm.view_entries()
        elif choice == "3":
            jm.search_entries()
        elif choice == "4":
            jm.delete_entries()
        elif choice == "5":
            print("Thank you for using Personal Journal Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid option from the menu.\n")

main()
       