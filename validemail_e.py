# nev@domain.com -> jó
# nev@@domain.com -> nemjó   [x]
# @domain.com -> nemjó
# nev.nev@domain.com -> jó
# nev@domain.com.hu -> jó
# nev@.com -> nemjó
# nev.com -> nem jó          [x]
# nev@domain.c -> nem jó (minimum 2 betűs az utcsó tag)

email = input('e-mail cím: ')

kukacok_szama = 0
for c in email:
    if c == '@': kukacok_szama += 1

hiba_1 = kukacok_szama != 1

email.split('@', '')
