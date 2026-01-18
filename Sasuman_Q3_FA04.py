names = ["Me", "Lia", "Jake"]

steps = [ 
    [4500, 5200, 4800, 5000, 5300],
    [400, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]]
total_steps = []
for person_steps in steps:
    total_steps.append(sum(person_steps))
for i in range(len(names)):
    print(names[i], "total steps:", total_steps[i])
highest = max(total_steps)
lowest = min(total_steps)
top_index = total_steps.index(highest)
top_performer = names[top_index]
print("\nTop Performer:", top_performer)
print("Highest total steps:", highest)
print("Lowest total steps:", lowest)
print("Difference between highest and lowest:", highest - lowest)
