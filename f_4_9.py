kis =  'abcdefghijklmnopqrstuvwxyz'
nagy = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

szoveg = input('szöveg: ')

# for i in range(len(szoveg)):
#     if szoveg[i] in nagy:
#         print (kis[nagy.index(szoveg[i])], end='')
#     else: print(szoveg[i], end='')

print('csupa kisbetűvel:', end=' ')
print(szoveg.lower())
print('\ncsupa nagybetűvel:', end=' ')
print(szoveg.upper())