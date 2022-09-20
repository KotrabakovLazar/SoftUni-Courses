divisor = int(input())
boundary = int(input())
# for current_number in range (divisor +1, bound +1):
#     if current_number % divisor == 0:
#         max_multiplier = current_number
# print(max_multiplier)
for current_number in range (boundary, divisor, -1 ):
    if current_number % divisor == 0:
        break
print(current_number)