from __future__ import division
import curses,threading,time,random

"""
  _____   _
 /o    \_/ |
[       _  |
 `-----' `-'
"""

bird = """ _    _____
| \_/    o\\
|  _       ]
'-` '-----`
"""







"""
HAYO MAU APA LU BOCAH?

MAU RECODE YA WKWKWKWK



GABISA BIKIN GAME JANGAN RECODE YA DEK
GW TAU KOK LU PUSING LIAT SOURCE CODE INI



YAHAHA BOCAH RECODE YAHAHA RECODE




KALO GAK MAMPU CODING,BELAJAR SONO.

SINI GW AJARIN BIAR LU GAK RECODE LAGI


WA : 0896 8200 9902
"""















score = 0
delay = False
adstop = False
obstacle = []
abuse = []


def running_text(slep):
    global abuse
    while True and not lose:
       abyss = {}
       for i in abuse[0]:
           if i-1 < abuse[1]:
              abyss[abuse[2]] = abuse[0][i]
           else:
              abyss[i-1] = abuse[0][i]
       abuse[0] = dict(abyss)
       time.sleep(slep)


def tredo(slep):
    global birdo,delay
    while not adstop and not lose:
       birdo = [(lambda x,n:[x+1,n])(i[0],i[1]) for i in birdo]
       if delay:
          time.sleep(delay)
          delay = False
       time.sleep(slep)

def tros(slep):
    global obstacle,score,abuse
    while True and not lose:
       for i in sorted(obstacle,key = lambda x:x[1]):
           if i[1] == 0:
              obstacle.remove(i)
              score += 1
       obstacle = [(lambda y,x,o:[x,y-1,o])(i[1],i[0],i[2]) for i in obstacle] #bikin rintangan berjalan
       time.sleep(slep)


def troda(slep,yy,xx):
    global obstacle
    while True and not lose:
       y = random.randint(10,yy-5)
       x = xx-5
       downside = range(y,yy-1) #bikin rintangan bagian bawah
       [downside.append(i) for i in range(2,y-8)[::-1]] #Bikin rintangan bagian atas
       obstacle.append([y,x,downside])
       time.sleep(slep)

birdo = []
lose = False
def cur(c):
    global birdo,delay,lose,abuse
    yy,xx = c.getmaxyx() # mengambil max y dan x di terminal
    wow = {}
    min = xx//2 - len("Coded by JustA Hacker")
    max = xx//2 + len("Coded by JustA Hacker")
    for n,i in enumerate("Coded by JustA Hacker"):
        wow[(xx//2 - (len("Coded by JustA Hacker") // 2)) + n] = i
    abuse.append(wow)
    abuse.append(min)
    abuse.append(max)
    birdo = [[yy//2-2,5],[yy//2-1,5],[yy//2,5],[yy//2+1,5]] #bikin koordinat badan burung
    for lost,saga in zip(bird.splitlines(),birdo):
        c.addstr(saga[0],saga[1],lost)
    curses.curs_set(0)
    curses.noecho()
    c.addstr(yy-1,0,"-"*(xx-1))
    c.addstr(1,0,"-"*(xx-1))
    c.addstr(yy//2,xx//2-len("Press 'space' or 'up' button to jump")//2,"Press 'space' or 'up' button to jump")
    c.refresh()
    while True:
       coki = c.getch()
       if coki == ord(" ") or coki == curses.KEY_UP:
          break
    trd = threading.Thread(target=tredo,args=(0.1,))
    trd.daemon = True
    trd.start()
    trd2 = threading.Thread(target=troda,args=(1.8,yy,xx))
    trd2.daemon = True
    trd2.start()
    trd3 = threading.Thread(target=tros,args=(0.05,)) 
    trd3.daemon = True
    trd3.start()
    trd4 = threading.Thread(target=running_text,args=(0.1,))
    trd4.daemon = True
    trd4.start()
    c.nodelay(1)
    kimi_no_nawa = 0
    while True:
       coki = c.getch()
       c.erase()
       if coki == ord(" ") or coki == curses.KEY_UP:
          birdo = [(lambda x,n:[x-2,n])(i[0],i[1]) for i in birdo]
          if not delay:
             delay = 0.3
          if kimi_no_nawa < 4:
             kimi_no_nawa += 1
             birdo = [(lambda x,n:[x-1,n])(i[0],i[1]) for i in birdo]
          else:
             kimi_no_nawa = 0
             coki = ""
             adstop = False
       [c.addstr(saga[0],saga[1],lost) for lost,saga in zip(bird.splitlines(),birdo)]
       c.addstr(yy-1,0,"-"*(xx-1))
       c.addstr(1,0,"-"*(xx-1))
       c.addstr(0,0,"Score : {}".format(score))
       for i in obstacle:
           c.addstr(i[0],i[1],"||||")
           [c.addstr(b,i[1],"||||") for b in i[2]]
       try:
         [c.addstr(0,i,abuse[0][i]) for i in sorted(abuse[0])]
       except:
         pass

       for n,z in enumerate(birdo):
          if z[0] == 1 or z[0] == yy-1 or (z[0] == obstacle[0][0] and z[1] == obstacle[0][1]) or (z[0] in obstacle[0][2] and obstacle[0][1] in range(z[1],z[1]+len(bird.splitlines()[n])+1)) :
             c.addstr(yy//2,xx//2 - len(" You lose ")//2," You lose ")
             c.addstr(yy//2+1,xx//2 - len("Press Q or q to quit the game")//2,"Press Q or q to quit the game")
             c.nodelay(0)
             lose = True
             while True:
                cus = c.getch()
                if cus  == ord("q") or cus == ord("Q"):
                   break
             break

       if lose:
          return
       c.refresh()
curses.wrapper(cur)
