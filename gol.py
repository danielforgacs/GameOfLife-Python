from PIL import Image
import random
import time
import datetime

DEAD = ' '
LIVE = 'o'
WIDTH = 32
HEIGHT = 32
MAX_GEN = 0

class Pixel:
    def __init__(self, x, y, is_live):
        self.x, self.y = x, y
        self.is_live = True if is_live == LIVE else False

    @property
    def color(self):
        return (255, 255, 255) if self.is_live else (0, 0, 0)

def gen_map():
    map_x = ()
    map_x_2 = ()
    for k in range(HEIGHT):
        map_y = ()
        map_y_2 = ()
        for j in range(WIDTH):
            map_y = map_y + (random.choice([DEAD, LIVE]), )
            life = random.choice([DEAD, LIVE])
            map_y_2 = map_y_2 + (Pixel(k, j, life),)
        map_x = map_x + (map_y,)
        map_x_2 = map_x_2 + (map_y_2,)
    return map_x, 0, map_x_2


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

def print_world(world, gen, world_2):
    print('gen: {} - dimensions: {} x {}: {}'.format(gen, WIDTH, HEIGHT, WIDTH*HEIGHT))
    lines = ''
    for k in world_2:
        line = ''
        for xy in k:
            line += DEAD if xy.is_live == DEAD else LIVE
        lines += line+'\n'
    print(lines)

def save_image(world, gen, world_2):
    img = Image.new('RGB', (WIDTH, HEIGHT))
    imgname = 'life.{:>04d}.png'.format(gen)
    for x in range(len(world)):
        for y in range(len(world[x])):
            # r = 0 if world[x][y] == DEAD else 255
            # img.putpixel((y, x), (r, r, r))
            # print(world_2[x][y].color, world_2[x][y].is_live)
            img.putpixel((y, x), world_2[x][y].color)
    img.save(imgname)
    return imgname

def main():
    world, gen, world_2 = gen_map()
    save_image(world, gen, world_2)
    print_world(world, gen, world_2)

    for k in range(MAX_GEN):
        time0 = datetime.datetime.now()
        world, gen = calc_time_step(world, gen)
        imagename = save_image(world, gen)
        print('gen: {}, image: {}, {}'.format(gen, imagename, datetime.datetime.now()-time0))

print('='*77)
main()
print('done.')
