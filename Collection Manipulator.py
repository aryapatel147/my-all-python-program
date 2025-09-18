print("Welcome to the student data organizer!\n")


stored = {}

while True:  
    print("\nSelect an option: ")
    print("1. Add student")
    print("2. Display all students")
    print("3. Update student information")
    print("4. Delete student")
    print("5. Display subjects offered")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        std_id = input("Student ID: ")
        name = input("Name: ")
        age = input("Age: ")
        grade = input("Grade: ")
        b_day = input("Date of birth (yyyy-mm-dd): ")
        subject = input("Subjects (comma-separated): \n")

        tup_stdid = (std_id, b_day)  

        stored[std_id] = {
            "name": name,
            "age": age,
            "grade": grade,
            "b_day": b_day,
            "subject": subject
        }

        print("Student added successfully")

    elif choice == 2:
        if not stored:
            print("No students available.")
        else:
            for sid in stored:
                info = stored[sid]
                print("\nID:", sid)
                print("Name:", info["name"])
                print("Age:", info["age"])
                print("Grade:", info["grade"])
                print("Birthday:", info["b_day"])
                print("Subjects:", info["subject"])

    elif choice == 3:
        sid = input("Enter the student ID to update: ")
        if sid in stored:
            name = input("New name: ")
            age = input("New age: ")
            grade = input("Enter grade: ")
            b_day = input("New date of birth (yyyy-mm-dd): ")
            subject = input("New subject: ")

            stored[sid] = {
                "name": name,
                "age": age,
                "grade": grade,
                "b_day": b_day,
                "subject": subject
            }
            print("Student updated successfully")
        else:
            print("Student not found")

    elif choice == 4:
        sid = input("Enter student ID to delete: ")
        if sid in stored:
            del stored[sid]
            print("Student deleted successfully")
        else:
            print("Student not found.")
#option 5 helping ai google for  understanding
    elif choice == 5:
        if not stored:
            print("No subjects yet.")
        else:
            print("Subjects offered:")
            for sid in stored:
                print("ID:", sid, "=>", stored[sid]["subject"])

    elif choice == 6:
        print("Exiting... Goodbye!")
        break  

    else:
        print("Invalid choice, try again.")
