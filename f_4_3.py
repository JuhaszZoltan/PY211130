nev = input('neved: ')

for i in range(len(nev)):
   print(f'{" " * i}{nev[i]}')

# nem csak pythonban:
# for i in range(len(nev)):
#     for j in range(i):
#         print(' ', end='\0')
#     print(nev[i])