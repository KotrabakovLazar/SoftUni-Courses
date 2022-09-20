budget = float(input())
one_kg_flour_price = float(input())

easter_breads_counter = 0
colored_eggs = 0

eggs_price = one_kg_flour_price * 0.75
milk_price_per_easter_bread = one_kg_flour_price * 1.25 / 4
easter_bread_price = one_kg_flour_price + eggs_price + milk_price_per_easter_bread
while budget - easter_bread_price >= 0:
    budget -= easter_bread_price
    easter_breads_counter +=1
    colored_eggs += 3
    if easter_breads_counter % 3 == 0:
        colored_eggs -= easter_breads_counter - 2

print(f"You made {easter_breads_counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")