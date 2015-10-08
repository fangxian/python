import curses
from random import randint
from curses import KEY_LEFT,KEY_RIGHT,KEY_DOWN,KEY_UP
import time

screen=curses.initscr()
screen.keypad(1)
dims=screen.getmaxyx()

def game():
    screen.nodelay(1)
    head=[1,1]
    body=[head[:]]*5
    #dims=screen.getmaxyx()
    screen.border()
    direction=0 #0:right,1:down,2:left,3:up
    gameover=False
    deadcell=body[-1][:]
    foodmode=False
    score=0
    while not gameover:
        while not foodmode:
            y,x=randint(1,dims[0]-1),randint(1,dims[1]-1)
            if screen.inch(y,x)==ord(' '):
                foodmode=True
                screen.addch(y,x,ord('@'))

        if deadcell not in body:
            screen.addch(deadcell[0],deadcell[1],' ')
        screen.addch(head[0],head[1],'X')
        action=screen.getch()
        if action==KEY_UP and direction!=1:
            direction=3
        elif action==KEY_DOWN and direction!=3:
            direction=1
        elif action==KEY_LEFT and direction!=0:
            direction=2
        elif action==KEY_RIGHT and direction!=2:
            direction=0
        if direction==0:
            head[1]+=1
        if direction==2:
            head[1]-=1
        if direction==1:
            head[0]+=1
        if direction==3:
            head[0]-=1

        deadcell=body[-1][:]
        for z in range(len(body)-1,0,-1):
            body[z]=body[z-1][:]
        body[0]=head[:]
        if screen.inch(head[0],head[1])!=ord(' '):
            if screen.inch(head[0],head[1])==ord('@'):
                foodmode=False
                score+=1
                body.append(body[-1])
            else:
                gameover=True

        screen.refresh()
        time.sleep(0.1)

    screen.clear()
    screen.nodelay(0)
    #screen.refresh()
    screen.addstr(6,30,'GAMEOVER')
    screen.addstr(8,30,'SCORE:')
    screen.addstr(10,30,'Press enter to quit')
    screen.addstr(12,30,'Press space to play again')
    screen.refresh()
    q=0
    while q not in [32,10]:
        q=screen.getch()
    if q==32:
        screen.clear()
        game()
    elif q==10:
        pass
game()
curses.endwin()
