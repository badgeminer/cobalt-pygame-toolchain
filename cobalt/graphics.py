import numpy as np
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


def mktest(im):
    im = 255 * (im / im.max())
    w, h = im.shape
    ret = np.empty((w, h, 3), dtype=np.uint8)
    ret[:, :, 2] = ret[:, :, 1] = ret[:, :, 0] = im
    return ret
class loadScreen:
    def __init__(self) -> None:
        c = np.ndarray((1920,1080,3))
        y = np.arange(0, 1080)
        y = y//8
        y = y%255
        y = np.tile(y, (1920, 1))
        c[:,:,1] = y
        
        y = np.arange(0, 1920)
        y = y//8
        y = y%255
        y = np.tile(y, (1080, 1))
        y = np.rot90(y)
        c[:,:,0] = y
        c = np.flipud(c)
        
        #y = np.arange(0, 255)
        #y= y

        #X, Y = np.meshgrid(x, y)

        #Z = X + Y
        #Z = 1*Z
        #Z = mktest(Z)
        self.image = pygame.surfarray.make_surface(c)

def xyshdr(x,y,m=4):
    return (((x*m)%255),((y*m)%255),0)

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