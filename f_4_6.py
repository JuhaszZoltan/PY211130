szoveg = input('szoveg: ')

# c = 0
# for b in szoveg:
#     if b == 'e' or b == 'E':
#         c += 1

c = 0
for b in szoveg:
    if b in 'Ee': c += 1

print(f'{szoveg}-ben {c} db "e" betű van')