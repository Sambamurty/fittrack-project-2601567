
student_name = input("Enter student name: ")
math_score = int(input("Enter Maths score: "))
science_score = int(input("Enter Science score: "))
english_score = int(input("Enter English score: "))

status = "Pass"
grade = ""

if(math_score < 0 or math_score > 100 or science_score < 0 or science_score > 100 or english_score < 0 or english_score > 100):
    print("Invalid marks entered")
else:
    total_score = math_score + science_score + english_score
    average_score = total_score / 3
    if math_score < 40 or science_score < 40 or english_score < 40:
        status = "Fail"
    else:
        if average_score >= 75:
            grade = "A"
        elif average_score >= 60:
            grade = "B"
        elif average_score >= 40:
            grade = "C"

    print(f"Student Name: {student_name}\nTotal Marks: {total_score}\nPercentage: {round(average_score, 2)}\nStatus: {status}\nGrade: {grade}")