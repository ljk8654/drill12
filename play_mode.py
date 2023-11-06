import random

from pico2d import *
import game_framework

import game_world
from grass import Grass
from boy import Boy
from ball import Ball
from zombie import Zombie

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global grass
    global boy
    global zombies
    running = True

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    # fill here
    # 볼을 50개 바닥에
    global balls
    balls = [Ball(random.randint(0, 1600), 60, 0)for _ in range(50)]
    game_world.add_objects(balls, 1)

    #충돌 검사 필요 상황을 등록
    game_world.add_collision_pairs('boy:ball', boy,  None)
    for ball in balls:
        game_world.add_collision_pairs('boy:ball', None, ball)
    zombies = [Zombie() for _ in range(5)]
    game_world.add_objects(zombies, 1)

    game_world.add_collision_pairs('boy:ball', boy, None)
    for zombie in zombies:
        game_world.add_collision_pairs('boy:zombie', None, zombie)

    for zombie in zombies:
        game_world.add_collision_pairs('zombie:ball', zombie, None)
    for ball in balls:
        game_world.add_collision_pairs('boy:ball', None, ball)


def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    game_world.handle_collisions()
    # fill here
    for ball in balls.copy():
        if game_world.collide(boy, ball):
            print('COLLISION boy: ball')
            boy.ball_count += 1 # 소년관점의 충돌처리
            balls.remove(ball)
            game_world.remove_object(ball)
    for zombie in zombies.copy():
        if game_world.collide(boy, zombie):
            print('COLLISION zombie: ball')
            game_framework.quit()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

