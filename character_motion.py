from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x, y = 400, 90
way = 0  # 방향 0: 오른쪽, 1: 위쪽, 2: 왼쪽, 3: 아래쪽
theta = 2 * math.pi
mode = 0 # 0: 사각형, 1: 원

while True:
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.01)

    if mode == 0:
        if way == 0:
            x += 2
            if x >= 800:
                x = 800
                way = 1
        elif way == 1:
            y += 2
            if y >= 600:
                y = 600
                way = 2
        elif way == 2:
            x -= 2
            if x <= 0:
                x = 0
                way = 3
        elif way == 3:
            y -= 2
            if y <= 90:
                y = 90
                way = 4
        elif way == 4:
            x += 2
            if x >= 400:
                x = 400
                way = 0
                mode = 1
                theta = 2 * math.pi

    elif mode == 1:
        radius = 210
        x = 400 + radius * math.cos(theta)
        y = 300 + radius * math.sin(theta)
        theta -= 0.02
        if theta <= 0:
            x, y = 400, 90
            mode = 0
            way = 0


close_canvas()
