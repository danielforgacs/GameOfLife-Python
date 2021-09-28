import random
import time

def gen_map():
    side = 4
    map_x = ()
    for k in range(side):
        map_y = ()
        for j in range(side):
            map_y = map_y + (random.choice([0, 1]), )
        map_x = map_x + (map_y,)
    return map_x, 0


def calc_time_step(world, gen):
    newworld = ()
    for x in range(len(world)):
        newline = ()
        for y in range(len(world[x])):
            neibours = 0
            if world[x][y] == 1:
                if neibours in [0, 1]:
                    newvalue = 0
                if neibours in [2, 3]:
                    newvalue = 1
            else:
                if neibours == 3:
                    newvalue = 1
                else:
                    newvalue = 0
            newline = newline+(newvalue,)
        newworld = newworld+ (newline,)
    return newworld, gen+1

def print_world(world, gen):
    print('gen:', gen)
    for k in world:
        print(k)

def main():
    world, gen = gen_map()
    world = (
        (0, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 0, 0),
        (0, 0, 0, 0),
    )
    print_world(world, gen)

    for k in range(1):
        world, gen = calc_time_step(world, gen)
        print_world(world, gen)


main()
