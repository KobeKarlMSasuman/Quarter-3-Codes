scores = [
    [85, 90, 88],  
    [78, 82, 80],   
    [92, 95, 94]    
]

print("=== Student Scores Summary ===\n")

for i in range(len(scores)):
    print("Student", i + 1, "scores:", scores[i])
    
    total = sum(scores[i])
    average = total / len(scores[i])
    
    print("Total:", total)
    print("Average:", average)
    print()
all_scores = []
for row in scores:
    for value in row:
        all_scores.append(value)

print("Highest score in dataset:", max(all_scores))
print("Lowest score in dataset:", min(all_scores))