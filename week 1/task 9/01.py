
student_records = {}
next_student_id = 1

def add_student():
    global next_student_id
    print("\n Add New Student ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")

    student_records[next_student_id] = {
        "name": name,
        "age": age,
        "grade": grade
    }
    print(f"Student {name} added with ID: {next_student_id}")
    next_student_id += 1

def display_all_students():
    print("\n All Student Records ")
    if not student_records:
        print("No student records found.")
        return

    for student_id, details in student_records.items():
        print(f"ID: {student_id}, Name: {details['name']}, Age: {details['age']}, Grade: {details['grade']}")

def search_student():
    print("\n Search Student by Name ")
    search_name = input("Enter the name of the student to search: ")
    found_students = [
        (student_id, details)
        for student_id, details in student_records.items()
        if search_name.lower() in details['name'].lower()
    ]

    if found_students:
        print("Found Student(s):")
        for student_id, details in found_students:
            print(f"ID: {student_id}, Name: {details['name']}, Age: {details['age']}, Grade: {details['grade']}")
    else:
        print(f"No student found with name containing '{search_name}'.")

def delete_student():
    print("\n Delete Student Record ")
    if not student_records:
        print("No student records to delete.")
        return

    display_all_students()
    try:
        student_id_to_delete = int(input("Enter the ID of the student to delete: "))
        if student_id_to_delete in student_records:
            deleted_name = student_records[student_id_to_delete]['name']
            del student_records[student_id_to_delete]
            print(f"Student '{deleted_name}' (ID: {student_id_to_delete}) deleted successfully.")
        else:
            print(f"Student with ID {student_id_to_delete} not found.")
    except ValueError:
        print("Invalid input. Please enter a number for the student ID.")