quantity = int(input())
remaining_days = int(input())
total_sum = 0
total_spirit = 0
ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

for current_day in range(1, remaining_days + 1):
    if current_day % 11 == 0:
        quantity += 2
    if current_day % 2 == 0:
        total_sum += ornament_set * quantity
        total_spirit += 5
    if current_day % 3 == 0:
        total_sum += (tree_skirt + tree_garlands) * quantity
        total_spirit += 13
    if current_day % 5 == 0:
        total_sum += tree_lights * quantity
        total_spirit += 17
        if current_day % 3 == 0:
            total_spirit += 30
    if current_day % 10 == 0:
        total_spirit -= 20
        total_sum += tree_skirt + tree_garlands + tree_lights

if remaining_days % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_sum}")
print(f"Total spirit: {total_spirit}")
