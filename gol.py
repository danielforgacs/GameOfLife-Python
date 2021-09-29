from PIL import Image
import random
import time
import datetime

DEAD = ' '
LIVE = 'o'
WIDTH = 1280
HEIGHT = 720
MAX_GEN = 250

WIDTH = 64
HEIGHT = 64
MAX_GEN = 50

def gen_map():
    map_x = ()
    map_x_life = ()
    for k in range(HEIGHT):
        map_y = ()
        map_y_life = ()
        for j in range(WIDTH):
            map_y = map_y + (random.choice([DEAD, LIVE]), )
            map_y_life = map_y_life + (0, )
        map_x = map_x + (map_y,)
        map_x_life = map_x_life + (map_y_life,)
    return map_x, 0, map_x_life


def calc_time_step(world, gen, world_age):
    newworld = ()
    newworld_age = ()
    for x in range(len(world)):
        newline = ()
        newworld_age_y = ()
        for y in range(len(world[x])):
            neibours = 0
            old_live = world[x][y]

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

            if old_live == DEAD and newvalue == LIVE:
                new_age = 0
            elif newvalue == DEAD:
                new_age = 0
            elif old_live == LIVE and newvalue == LIVE:
                new_age = world_age[x][y] + 1
            else:
                new_age = '?'

            newworld_age_y = newworld_age_y + (new_age,)

        newworld = newworld+ (newline,)
        newworld_age = newworld_age + (newworld_age_y,)
    return newworld, gen+1, newworld_age

def print_world(world, gen, world_age):
    print('gen: {} - dimensions: {} x {}: {}'.format(gen, WIDTH, HEIGHT, WIDTH*HEIGHT))
    lines = ''
    x = 0
    for k in world:
        line = ''
        for xy in k:
            line += DEAD if xy == DEAD else LIVE
        line += ' - '
        y = 0
        for xy in k:
            line += str(world_age[x][y])
            y += 1
        x += 1
        lines += line+'\n'
    print(lines)

def save_image(world, gen, world_age):
    img = Image.new('RGB', (WIDTH, HEIGHT))
    imgname = 'life.{:>04d}.png'.format(gen)
    for x in range(len(world)):
        for y in range(len(world[x])):
            r = 0 if world[x][y] == DEAD else 255
            g = world_age[x][y] * 10
            if g > 255:
                print(g)
            g = min(255, max(0, g))
            b = 0
            img.putpixel((y, x), (r, g, b))
    img.resize((0.2, 0.2))
    img.save(imgname)
    return imgname

def main():
    world, gen, world_age = gen_map()
    save_image(world, gen, world_age)
    # print_world(world, gen, world_age)

    for k in range(MAX_GEN):
        time0 = datetime.datetime.now()
        world, gen, world_age = calc_time_step(world, gen, world_age)
        # print_world(world, gen, world_age)
        imagename = save_image(world, gen, world_age)
        print('gen: {}, image: {}, {}'.format(gen, imagename, datetime.datetime.now()-time0))

print('='*77)
main()
print('done.')
