import random
import time

WIDTH = 4

def gen_map():
    map_x = []
    for k in range(WIDTH):
        map_y = []
        for j in range(WIDTH):
            map_y.append(random.choice([0, 1]))
        map_x.append(map_y)
    return map_x

def calc_neighbours(world, x, y):
    count = 0
    for k in [-1, 0, 1]:
        for i in [-1, 0, 1]:
            x2 = x + k
            y2 = y+ i
            if x == 0 or x == len(world[k])-1:
                continue
            if y == 0 or y == len(world[k])-1:
                continue
            if (x2, y2) == (x, y):
                continue
            if world[x2][y2] == 1:
                count += 1
    # print(count)
    return count


def calc_time_step(world):
    newworld = [[0]*WIDTH]*WIDTH
    for k in range(WIDTH):
        for j in range(WIDTH):
            neighbour_count = calc_neighbours(world, k, j)
            # print (neighbour_count)
            # if world[k][j] == 1:
            #     if neighbour_count in [0, 1]:
            #         newworld[k][j] = 0
            #     if neighbour_count in [2, 3]:
            #         newworld[k][j] = 1
            # else:
            #     if neighbour_count == 3:
            #         newworld[k][j] = 1
            newworld[k][j] = neighbour_count
    return newworld

def print_world(world):
    for k in range(WIDTH):
        print(world[k])
    time.sleep(0.1)
    print()

def main():
    gen = 0
    # world = gen_map()
    world = (
        (0, 0, 0, 0),
        (0, 0, 0, 0),
        (0, 0, 0, 0),
        (0, 0, 0, 0),
    )
    print('gen:', gen)
    print_world(world)

    for k in range(1):
        world = calc_time_step(world)
        gen += 1
        print('gen:', gen)
        print_world(world)


main()
