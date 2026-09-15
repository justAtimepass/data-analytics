file_name = "introduction.txt"
introduction_text = "Hello! all"

with open(file_name, "w") as file:
    file.write(introduction_text)

print(f"Content successfully written to '{file_name}'")