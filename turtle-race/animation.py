


def kilppari():
    #import turtle graphics
    import turtle
    #import random
    import random
    #import keyboard commands to exit
    import keyboard
    #turtle screen
    screen = turtle.Screen()
    screen.setup(width=1200, height=500)
    turtle.title('Turtle Race')
    #screen color
    screen.bgcolor('grey')


    #race track graphics
    j = turtle.Turtle()
    j.hideturtle()
    j.penup()
    j.speed(0)
    j.pensize(8)
    j.setheading(180)
    j.setpos(-570, 0)
    j.setheading(90)
    j.pendown()
    j.forward(180)
    j.setheading(0)
    j.forward(1100)
    j.setheading(270)
    j.forward(360)
    j.setheading(180)
    j.forward(1100)
    j.setheading(90)
    j.forward(240)
    j.setheading(0)
    j.forward(1100)
    j.setheading(270)
    j.forward(120)
    j.setheading(180)
    j.forward(1100)
    j.hideturtle()
    j.penup()


    #info texts
    e = turtle.Turtle()
    e.hideturtle()
    e.penup()
    e.speed(0)
    e.setpos(-570,185)
    e.write('E = Exit', font=('Arial', 20))
    e.setpos(-400,185)
    e.write('R Winrate(%):', font=('Arial', 20),)
    e.setpos(-100,185)
    e.write('Y Winrate(%):', font=('Arial', 20))
    e.setpos(200,185)
    e.write('G Winrate(%):', font=('Arial', 20))
    

    #live stats
    f = turtle.Turtle()
    f.speed(0)
    f.hideturtle()
    f.penup()
    f.setpos(-225,185)
    s = turtle.Turtle()
    s.speed(0)
    s.hideturtle()
    s.penup()
    s.setpos(75,185)
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.setpos(375,185)

    # a turtle's appearance
    a = turtle.Turtle()
    a.shape('turtle')
    a.shapesize(4.5, 4.5, 7.2)
    a.color('red')

    # b turtle's appearance
    b = turtle.Turtle()
    b.shape('turtle')
    b.shapesize(4.5, 4.5, 7.2)
    b.color('yellow')

    # c turtle's appearance
    c = turtle.Turtle()
    c.shape('turtle')
    c.shapesize(4.5, 4.5, 7.2)
    c.color('green')
    #pen up
    a.penup()
    b.penup()
    c.penup()

    #point and rounds to calculate winrate
    a_points = 0
    b_points = 0
    c_points = 0
    rounds = 0


    while True:
        #start positions
        a.speed(10)
        b.speed(10)
        c.speed(10)
        a.setpos(-520,120)
        b.setpos(-520,0)
        c.setpos(-520,-120)

        #maxium speed
        a.speed(0)
        b.speed(0)
        c.speed(0)
        #possible finish line coords
        if_a = ['(450.00,120.00)','(452.00,120.00)','(454.00,120.00)','(456.00,120.00)','(458.00,120.00)']
        if_b = ['(450.00,0.00)','(452.00,0.00)','(454.00,0.00)','(456.00,0.00)','(458.00,0.00)']
        if_c = ['(450.00,-120.00)','(452.00,-120.00)','(454.00,-120.00)','(456.00,-120.00)','(458.00,-120.00)']
        
        while True:
            #random "speed", using random.choice to select from the list
            a.forward(random.choice([2,4,6,10]))
            a_state = str(a.pos())
            b.forward(random.choice([2,4,6,10]))
            b_state = str(b.pos())
            c.forward(random.choice([2,4,6,10]))
            c_state = str(c.pos())
            #exit
            if keyboard.is_pressed('e'):
                exit()
            if a_state in if_a:
                rounds += 1
                a_points += 1
                break
            elif b_state in if_b:
                rounds += 1
                b_points += 1
                break
            elif c_state in if_c:
                rounds += 1
                c_points += 1
                break
            else: 
                continue
        #clear old stats
        f.clear()
        s.clear()
        t.clear()
        #write new stats
        f.write(round(a_points / rounds * 100,2), font=('Arial', 20))
        s.write(round(b_points / rounds * 100,2), font=('Arial', 20))
        t.write(round(c_points / rounds * 100,2), font=('Arial', 20))

