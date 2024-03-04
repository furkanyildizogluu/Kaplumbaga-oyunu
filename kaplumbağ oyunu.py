import turtle
import random
from turtle import Turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("white")
turtle_screen.title("TURTLE")
FONT = ('Arial', 30, 'normal')
skor = 0
turtle_list = []
game_over = False
sayac_turtle = turtle.Turtle()


# SKOR TABLOSU
def setup_score_turtle():
    global skore_turtle
    skore_turtle = turtle.Turtle()
    skore_turtle.hideturtle()
    skore_turtle.penup()
    skore_turtle.color("dark blue")

    top_height = turtle_screen.window_height() / 2
    y = top_height * 0.8
    skore_turtle.setpos(0, y)


    skore_turtle.hideturtle()
    skore_turtle.color("dark blue")





def make_turtle(x, y):
    t = turtle.Turtle()

    def turtle_tıklama(x, y):  # kaplumbağın üstüne her tıklandığında skoru arttırmak için kullanılır.
        global skor
        skor += 1
        skore_turtle.clear()  # her tıklanıldığında önceki sayıların bir birinin üstüne gelmesini engeller
        skore_turtle.write(arg="skor: {}".format(skor), move=False, align="center", font=FONT)
# turtleın özellikleri
    t.onclick(turtle_tıklama)
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("green")
    t.goto(x * 10, y * 10)
    turtle_list.append(t)

turtle.tracer(0)

x_kordinat = [-20, -10, 0, 10, 20]
y_kordinat = [20, 10, 0, -10]

for x in x_kordinat:
    for y in y_kordinat:
        make_turtle(x, y)

def gizleme_turtle():
    for t in turtle_list:
        t.hideturtle()




def show_turtles_randomly():
    if not game_over:
        gizleme_turtle()
        random.choice(turtle_list).showturtle()
        turtle.ontimer(show_turtles_randomly,1000)   #turtllerın ekranda 0.5 saniyede bir farklı yerlerde çıkmasını sağlar

def sayac(time):
    global game_over
    sayac_turtle.hideturtle()
    sayac_turtle.penup()
    sayac_turtle.color("dark blue")

    top_height = turtle_screen.window_height() / 2
    y = top_height * 0.8
    sayac_turtle.setpos(0, y-40)
    sayac_turtle.clear()
    if time > 0:
     sayac_turtle.clear()
     sayac_turtle.write(arg="sayac: {}".format(time), move=False, align="center", font=FONT)
     turtle.ontimer(lambda: sayac(time - 1),1000)
    else:
        game_over =  True
        sayac_turtle.clear()
        gizleme_turtle()
        sayac_turtle.write(arg="OYUN BİTTİ!".format(time), move=False, align="center", font=FONT)

def oyunu_başlat():
    setup_score_turtle()
    gizleme_turtle()
    show_turtles_randomly()
    sayac(30)
    turtle.tracer(1)
oyunu_başlat()
turtle.done()










