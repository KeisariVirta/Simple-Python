import random
def vali():
    print('')

def noppa():
    while True:
        maara = input('Montako noppaa haluat heittaa?: ')
        if maara.isdigit():
            maara = int(maara)
            if maara <= 0:
                vali()
                print('Syota vahintaan numero 1!')
                vali()
                continue
            else:
                break
        else:
            vali()
            print('Syota numero seuraavalla kerralla!')
            vali()
            continue
    yhteensa = 0
    while maara > 0:
        randomi = random.randint(1,6)
        print(randomi)
        yhteensa = yhteensa + randomi
        maara = maara - 1
    print('yhteensa:', yhteensa)
print('')


while True:
    inp = input('Haluatko heittaa noppaa K/E?: ').lower()
    if inp == 'e':
        print('Moro!')
        exit()
    elif inp == 'k':
        noppa()
    else:
        print('K = Kylla E = En')
        continue








