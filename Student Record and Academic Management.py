# Student Record and Academic Management System

students = {}

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Average Marks")
    print("7. Find Highest Scorer")
    print("8. List Students by Department")
    print("9. Count Students")
    print("10. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        marks = float(input("Enter Marks: "))

        students[roll] = {
            "Name": name,
            "Department": dept,
            "Marks": marks
        }

        print("Student Added Successfully!")

    # Display Students
    elif choice == "2":
        if len(students) == 0:
            print("No Records Found!")
        else:
            for roll, data in students.items():
                print("\nRoll No:", roll)
                print("Name:", data["Name"])
                print("Department:", data["Department"])
                print("Marks:", data["Marks"])

    # Search Student
    elif choice == "3":
        roll = input("Enter Roll Number to Search: ")

        if roll in students:
            print("\nStudent Found")
            print("Name:", students[roll]["Name"])
            print("Department:", students[roll]["Department"])
            print("Marks:", students[roll]["Marks"])
        else:
            print("Student Not Found!")

    # Update Student
    elif choice == "4":
        roll = input("Enter Roll Number to Update: ")

        if roll in students:
            name = input("Enter New Name: ")
            dept = input("Enter New Department: ")
            marks = float(input("Enter New Marks: "))

            students[roll]["Name"] = name
            students[roll]["Department"] = dept
            students[roll]["Marks"] = marks

            print("Record Updated Successfully!")
        else:
            print("Student Not Found!")

    # Delete Student
    elif choice == "5":
        roll = input("Enter Roll Number to Delete: ")

        if roll in students:
            del students[roll]
            print("Record Deleted Successfully!")
        else:
            print("Student Not Found!")

    # Average Marks
    elif choice == "6":
        if len(students) == 0:
            print("No Records Available!")
        else:
            total = 0

            for data in students.values():
                total += data["Marks"]

            average = total / len(students)

            print("Average Marks =", average)

    # Highest Scorer
    elif choice == "7":
        if len(students) == 0:
            print("No Records Available!")
        else:
            highest_roll = max(students,
                               key=lambda x: students[x]["Marks"])

            print("\nHighest Scorer Details")
            print("Roll No:", highest_roll)
            print("Name:",
                  students[highest_roll]["Name"])
            print("Department:",
                  students[highest_roll]["Department"])
            print("Marks:",
                  students[highest_roll]["Marks"])

    # List by Department
    elif choice == "8":
        dept = input("Enter Department Name: ")

        found = False

        for roll, data in students.items():
            if data["Department"].lower() == dept.lower():

                print("\nRoll No:", roll)
                print("Name:", data["Name"])
                print("Marks:", data["Marks"])

                found = True

        if not found:
            print("No Students Found in this Department!")

    # Count Students
    elif choice == "9":
        print("Total Number of Students =", len(students))

    # Exit
    elif choice == "10":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")