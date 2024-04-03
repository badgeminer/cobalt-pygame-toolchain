import pygame
scrW = 1920
scrH = 1080
tileSize = 32
grdVpW = scrW//tileSize
grdVpH = scrH//tileSize
grdVpCX = grdVpW//2
grdVpCY = grdVpH//2

ASSET_404 = pygame.Surface((32,32))
ASSET_404.fill((0,0,0))
ASSET_404.fill((255,100,0),(0,0,16,16))
ASSET_404.fill((255,100,0),(16,16,32,32))

def xyshdr(x,y):
    return (((x*4)%255),0,((y*4)%255))

def gridVpToScrVp(r:pygame.Rect):
    return pygame.Rect(
        r.left*tileSize,
        r.top*tileSize,
        r.width*tileSize,
        r.height*tileSize
    )
def shift(r:pygame.Rect):
    return pygame.Rect(
        0-r.left,
        0-r.top,
        r.width,
        r.height
    )