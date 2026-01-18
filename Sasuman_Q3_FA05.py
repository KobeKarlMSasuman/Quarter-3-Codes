names = ["Me", "Lia", "Jake"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]]
daily_totals = []
for day_index in range(len(days)):
    day_total = 0
    for person_index in range(len(steps)):
        day_total += steps[person_index][day_index]
    daily_totals.append(day_total)
for i in range(len(days)):
    print(days[i], "total steps:", daily_totals[i])
highest_steps = max(daily_totals)
most_active_day = days[daily_totals.index(highest_steps)]
print("\nMost active day overall:", most_active_day)
print("Total steps on that day:", highest_steps)