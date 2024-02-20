B = int(input())

if B == 100:
    sea_level = 0
elif B > 100:
    sea_level = - 1
elif B < 100:
    sea_level = 1

print((5 * B) - 400)
print(sea_level)