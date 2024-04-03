import pygame
scrW = 1920
scrH = 1080
tileSize = 32
grdVpW = scrW//tileSize
grdVpH = scrW//tileSize
grdVpCX = grdVpW//2
grdVpCY = grdVpH//2

def gridVpToScrVp(r:pygame.Rect):
    return pygame.Rect(
        r.left*tileSize,
        r.top*tileSize,
        r.width*tileSize,
        r.height*tileSize
    )