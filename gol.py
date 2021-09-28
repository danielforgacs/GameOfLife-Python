import random
import time

DEAD = ' '
LIVE = 'O'
WIDTH = 80
HEIGHT = 36
SLEEP = 1 / 24
MAX_GEN = 150

def gen_map():
    map_x = ()
    for k in range(HEIGHT):
        map_y = ()
        for j in range(WIDTH):
            map_y = map_y + (random.choice([DEAD, LIVE]), )
        map_x = map_x + (map_y,)
    return map_x, 0


def calc_time_step(world, gen):
    newworld = ()
    for x in range(len(world)):
        newline = ()
        for y in range(len(world[x])):
            neibours = 0

            for i in [-1, 0, 1]:
                for l in [-1, 0, 1]:
                    nx, ny = x+i, y+l
                    if nx < 0 or nx > len(world)-1:
                        continue
                    if ny < 0 or ny > len(world[x])-1:
                        continue
                    if (nx, ny) == (x, y):
                        continue
                    if world[nx][ny] == LIVE:
                        neibours += 1

            newvalue = DEAD
            if world[x][y] == LIVE:
                if neibours in [2, 3]:
                    newvalue = LIVE
                else:
                    newvalue = DEAD
            else:
                if neibours == 3:
                    newvalue = LIVE
            newline = newline+(newvalue,)
        newworld = newworld+ (newline,)
    return newworld, gen+1

def print_world(world, gen):
    print('gen:', gen)
    for k in world:
        line = ''
        for xy in k:
            line += DEAD if xy == DEAD else LIVE
        print(line)

def main():
    world = (
        ('.', '.', '.', '.', '.', '.', '.'),
        ('.', '.', 'x', '.', '.', '.', '.'),
        ('.', '.', 'x', 'x', '.', '.', '.'),
        ('.', '.', 'x', '.', '.', '.', '.'),
        ('.', '.', '.', '.', '.', '.', '.'),
        ('.', '.', '.', '.', '.', '.', '.'),
        ('.', '.', '.', '.', '.', '.', '.'),
    )
    world, gen = gen_map()
    print_world(world, gen)

    for k in range(MAX_GEN):
        world, gen = calc_time_step(world, gen)
        print_world(world, gen)
        time.sleep(SLEEP)


print('='*77)
main()
