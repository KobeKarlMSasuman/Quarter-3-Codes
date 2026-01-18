study_hours = [
    [2, 3, 2, 5, 3],
    [1, 2, 2, 3, 2],
    [3, 3, 4, 3, 4]]
def summarize_student(hours):
    total = sum(hours)
    average = total / len(hours)
    minimum = min(hours)
    maximum = max(hours)
    return total, average, minimum, maximum
names = ["My", "Friend 2", "Mark"]
for i, student in enumerate(names):
    total, avg, min_h, max_h = summarize_student(study_hours[i])
    print(f"{student} - Total Hours: {total} | Average: {avg:.1f} | Min: {min_h} | Max: {max_h}")