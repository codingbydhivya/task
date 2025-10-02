students = [
    {"roll_no": 1, "name": "Dhivya",  "total_marks": 475},
    {"roll_no": 2, "name": "Meera",  "total_marks": 460},
    {"roll_no": 3, "name": "Hemakannan",  "total_marks": 456},
    {"roll_no": 4, "name": "Divyan",  "total_marks": 476},
    {"roll_no": 5, "name": "Anamika",  "total_marks": 458}
]

print("-------------Marks---------------")
for s in students:
    print(f"{s['roll_no']:7} | {s['name']:7} | {s['total_marks']:5}")

top = max(students, key=lambda x: x["total_marks"])
print(f"\nTop Student: {top['name']} with {top['total_marks']} marks.")

avg = sum(s["total_marks"] for s in students) / len(students)
print(f"Class Average Marks: {avg:.2f}")

"""
output:
-------------Marks---------------
      1 | Dhivya  |   475
      2 | Meera   |   460
      3 | Hemakannan |   456
      4 | Divyan  |   476
      5 | Anamika |   458

Top Student: Divyan with 476 marks.
Class Average Marks: 465.00

"""
