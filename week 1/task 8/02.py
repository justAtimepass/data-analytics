file_name = "introduction.txt"

with open(file_name, "r") as file:
    content = file.read()

print(f"\nContent of '{file_name}':\n---\n{content}--- ")