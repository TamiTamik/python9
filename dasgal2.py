from function1 import create, remove, showMenu, Show

showMenu()

n = int(input('uildliin dugaar oruulna uu: '))

if n == 1:
    Show()
elif n == 2:
    create()
elif n == 3:
    remove()
elif n == 4:
    print('ta uur dugaar oruulna uu, ene uildel geriin daalgavar yumaa')
    n = int(input('uildliin dugaar oruulna uu: '))
else:
    print('ta programmas garlaa...')