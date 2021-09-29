from PIL import Image
import random
import time
import datetime

DEAD = ' '
LIVE = 'o'
WIDTH = 16
HEIGHT = 16
MAX_GEN = 1

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
            img.putpixel((y, x), (r, r, r))
    img.save(imgname)
    return imgname

def main():
    world, gen, world_age = gen_map()
    save_image(world, gen, world_age)
    print_world(world, gen, world_age)
    sim = ((world, gen, world_age), )

    for k in range(MAX_GEN):
        time0 = datetime.datetime.now()
        world, gen = calc_time_step(world, gen)
        print_world(world, gen, world_age)
        sim = sim + ((world, gen, world_age), )
        imagename = save_image(world, gen, world_age)
        print('gen: {}, image: {}, {}'.format(gen, imagename, datetime.datetime.now()-time0))

print('='*77)
main()
print('done.')
