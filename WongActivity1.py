StudentList = {
    "Amara": {"Math": 89, "English": 94, "Science": 94},
}

def addStud(name, subject1, grade1, subject2, grade2, subject3, grade3):
    StudentList[name] = {subject1: grade1, subject2: grade2, subject3: grade3}

addStud("Leo", "Math", 89, "English", 81, "Science", 88)
addStud("Kyle", "Math", 82, "English", 85, "Science", 91)

for name, subjects in StudentList.items():
    print(f"{name}: {subjects}")

def getAvr(grades):
    return sum(grades.values()) / len(grades)

for name, grades in StudentList.items():
    avg = getAvr(grades)
    print(f"{name}'s average: {avg:.2f}")