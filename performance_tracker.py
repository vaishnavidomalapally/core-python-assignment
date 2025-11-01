def average_marks(student_data):
    avg = {}
    for name, marks in student_data.items():
        avg[name] = round(sum(marks) / len(marks), 2)
    return avg

def top_performer(avg_data):
    return max(avg_data, key=avg_data.get)

students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
averages = average_marks(students)
print("Average Marks:", averages)
print("Top Performer:", top_performer(averages))
