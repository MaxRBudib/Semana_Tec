"""Snake, classic arcade game.
Exercises
1.  La comida podrá moverse al azar un paso a la vez y no deberá de salirse de la ventana
2. Cada vez que se corra el juego, la víbora y la comida deberán tener colores diferentes entre sí, pero al azar, de una serie de 5 diferentes colores, excepto el rojo.
"""

from turtle import *
from random import randrange, randint
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
numero = randint(1,5)

def color(numero):
    if numero ==1:
        return "green"
    if numero ==2:
        return "blue"
    if numero ==3:
        return "purple"
    if numero ==4:
        return "black"
    if numero ==5:
        return "pink"

def color2(numero):
    if numero ==1:
        return "blue"
    if numero ==2:
        return "purple"
    if numero ==3:
        return "black"
    if numero ==4:
        return "pink"
    if numero ==5:
        return "green"

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190



def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-19, 18) * 10
        food.y = randrange(-19, 18) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, color(numero))

    square(food.x, food.y, 9, color2(numero))
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()