szoveg = input('szöveg: ')

for i in range(len(szoveg)):
    print(szoveg[len(szoveg) - i - 1], end='\0')