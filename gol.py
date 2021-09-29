from PIL import Image
import random
import time
import datetime

DEAD = ' '
LIVE = 'o'
WIDTH = 1280
HEIGHT = 720
MAX_GEN = 250

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
    print('gen: {} - dimensions: {} x {}: {}'.format(gen, WIDTH, HEIGHT, WIDTH*HEIGHT))
    lines = ''
    for k in world:
        line = ''
        for xy in k:
            line += DEAD if xy == DEAD else LIVE
        lines += line+'\n'
    print(lines)

def save_image(world, gen):
    img = Image.new('RGB', (WIDTH, HEIGHT))
    imgname = 'life.{:>04d}.png'.format(gen)
    for x in range(len(world)):
        for y in range(len(world[x])):
            r = 0 if world[x][y] == DEAD else 255
            img.putpixel((y, x), (r, r, r))
    img.save(imgname)
    return imgname

def main():
    world, gen = gen_map()
    save_image(world, gen)

    for k in range(MAX_GEN):
        time0 = datetime.datetime.now()
        world, gen = calc_time_step(world, gen)
        imagename = save_image(world, gen)
        print('gen: {}, image: {}, {}'.format(gen, imagename, datetime.datetime.now()-time0))

print('='*77)
main()
print('done.')