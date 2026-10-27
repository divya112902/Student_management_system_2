students = []


def add_student(roll_no, name):
    student = {"roll_no": roll_no, "name": name}
    students.append(student)
    return student


def get_all_students():
    return students


if __name__ == "__main__":
    add_student(1, "Divya")
    add_student(2, "Ashriya")
    for s in get_all_students():
        print(s)