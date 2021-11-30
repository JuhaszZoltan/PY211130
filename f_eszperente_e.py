szoveg = input('szöveg: ')

njm = "aáiíoóöőuúüű"
i = 0
while i < len(szoveg) and szoveg[i] not in njm:
    i += 1
if(i < len(szoveg)): print('nem eszperente a szöveg')
else: print('eszperente nyelven van a szöveg')

# i = 0
# while i < len(szoveg) and szoveg[i] not in "aáiíoóöőuúüű":
#     i += 1
# if(i < len(szoveg)): print('nem eszperente a szöveg')
# else: print('eszperente nyelven van a szöveg')

# csak python:
for b in szoveg:
    if b in njm:
        print('NEM eszperente')
        break
else: print('eszperente a szöveg')