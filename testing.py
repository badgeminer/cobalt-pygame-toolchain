import pygame,sys

import cobalt.graphics
import cobalt.map

pygame.init()
scr = pygame.display.set_mode((1920,1808),pygame.FULLSCREEN)
Map = cobalt.map.map(1920//30,1080//30)
mps = pygame.Surface(Map.space())
clk = pygame.time.Clock()
x,y = 15,15

print(Map.ViewPort(x,y))
Map.place(1,1,"test")
while True:
    x = pygame.math.clamp(x,0,Map.w)
    y = pygame.math.clamp(y,0,Map.h)
    scr.fill((0,0,0))
    mps.fill((0,0,0))
    Map.tiles.draw(mps)
    mps.blit(cobalt.graphics.ASSET_404,(x*32,y*32))
    vp = (cobalt.graphics.gridVpToScrVp(Map.ViewPort(x,y)))
    scr.blit(mps,(0,0),vp)
    pygame.display.flip()
    for e in pygame.event.get():
        match e.type:
            case pygame.KEYDOWN:
                match e.key:
                    case pygame.K_ESCAPE:
                        mps.fill((0,0,0))
                        Map.tiles.draw(mps)
                        sys.exit()
                    case pygame.K_w:
                        y -= 1
                    case pygame.K_s:
                        y += 1
                    case pygame.K_a:
                        x -= 1
                    case pygame.K_d:
                        x += 1
                    case pygame.K_SPACE:
                        Map.place(x,y,"test")
    clk.tick(60)