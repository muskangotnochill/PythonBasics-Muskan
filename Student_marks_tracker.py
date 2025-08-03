student = {}

while True:
    name=input("Enter your name (or exit): ")
    if name == "exit":
        break
    marks = int(input("Enter your marks: "))
    student[name] = marks

print("\n-- Student Database--")
for name,marks in student.items():
    print(f"{name} scored {marks} marks.")