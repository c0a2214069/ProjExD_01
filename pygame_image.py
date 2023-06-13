import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    koukaton = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(koukaton, True, False)
    kk_img2 = pg.transform.rotozoom(kk_img, 10, 1.0)
    kk_list = [kk_img,kk_img2]
    tmr = 0
    count = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        screen.blit(bg_img, [count, 0])
        screen.blit(kk_list[tmr%2],[300,200])
        pg.display.update()
        count += 1
        print(count)
        if count > 1599:
            count = 0
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()