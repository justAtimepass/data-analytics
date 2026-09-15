student_info = {
    "name": "Aditya",
    "age": 20,
    "major": "Computer Science",
    "id": "1234"
}
print(f"\n Student Dictionary: {student_info}")
print(f"Student Name: {student_info['name']}")
student_info["age"] = 21
print(f"Updated age: {student_info['age']}")
print(f"All keys: {student_info.keys()}")
print(f"All values: {student_info.values()}")