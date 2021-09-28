import random
import time

WIDTH = 10

def gen_map():
    map_x = []
    for k in range(WIDTH):
        map_y = []
        for j in range(WIDTH):
            map_y.append(random.choice([0, 1]))

        map_x.append(map_y)

    return map_x

def calc_time_step(world):
    newworld = [[0]*WIDTH]*WIDTH
    for k in range(WIDTH):
        for j in range(WIDTH):
            neighbour_count = 0
            for x_n in [-1, 0, 1]:
                for y_n in [-1, 0, 1]:
                    n_current_x = k+x_n
                    n_current_y = j+y_n
                    if n_current_x < 0 or n_current_x > WIDTH-1:
                        continue
                    if n_current_y < 0 or n_current_y > WIDTH-1:
                        continue
                    if world[n_current_x][n_current_y] == 1:
                        neighbour_count += 1

            if world[k][j] == 1:
                if neighbour_count in [0, 1]:
                    newworld[k][j] = 0
                if neighbour_count in [2, 3]:
                    newworld[k][j] = 1
            else:
                if neighbour_count == 3:
                    newworld[k][j] = 1
    return newworld

def print_world(world):
    print()
    for k in range(WIDTH):
        print(world[k])
    time.sleep(1)

def main():
    world = gen_map()
    world = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    print_world(world)

    for k in range(1):
        world = calc_time_step(world)
        print_world(world)


main()
