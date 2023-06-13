import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img_r = pg.transform.flip(bg_img, True, False)
    bg_list = []
    koukaton = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(koukaton, True, False)
    kk_list = [kk_img]
    for i in range(1,10):
        kk_img2 = pg.transform.rotozoom(kk_img, i, 1.0)
        kk_list.append(kk_img2)
    for i in range(10,1,-1):
        print(i)
        kk_img2 = pg.transform.rotozoom(kk_img,i, 1.0)
        kk_list.append(kk_img2)
    print(len(kk_list))
    tmr = 0
    count = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        screen.blit(bg_img,[-count,0])
        screen.blit(bg_img_r,[1600-count,0])
        screen.blit(bg_img,[3200-count,0])
        screen.blit(kk_list[tmr%19],[300,200])
        pg.display.update()
        tmr += 1
        count += 1
        print(count)
        if count >= 3200:
            count = 0       
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()