from animation import kilppari

while True:
    #ask if user want to play
    ask = input('Do you want to run the animation? y/n: ').lower()
    if ask == 'n':
        print('Bye!')
        exit()
    elif ask == 'y':
        kilppari()
    else:
        print('y = Yes n = No')
        continue

