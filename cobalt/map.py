from abc import ABCMeta
from dataclasses import dataclass
from typing import Any

import pygame
import cobalt.graphics
from class_registry import ClassRegistry

tileRegistry = ClassRegistry("id")

class tile(pygame.sprite.DirtySprite,metaclass=ABCMeta):
    def __init__(self,x,y,img) -> None:
        pygame.sprite.DirtySprite.__init__(self)
        self.dirty = 2

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = img

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect:pygame.Rect = self.image.get_rect()
        self.rect.topleft = (x*cobalt.graphics.tileSize,y*cobalt.graphics.tileSize)
        self.grdrect:pygame.Rect = self.image.get_rect()
        self.grdrect.topleft = (x,y)
    def update(self, vp:pygame.Rect) -> None:
        self.visible = vp.colliderect(self.grdrect)
@tileRegistry.register
class testTile(tile):
    id = "test"
    def __init__(self, x, y) -> None:

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        image = pygame.Surface([32, 32])
        image.fill((0,0,0))
        super().__init__(x, y, image)

@tileRegistry.register
class voidTile(tile):
    id = "void"
    def __init__(self, x, y) -> None:

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        image = pygame.Surface([32, 32])
        #image.fill((0,0,0))
        image.fill(cobalt.graphics.xyshdr(x,y))
        super().__init__(x, y, image)


class map:
    def __init__(self,w,h) -> None:
        self.w,self.h = w,h
        self.sw,self.sh =self.space()
        self.grid = [[voidTile(x,y)for x in range(w)] for y in range(h)]
        self.tiles:pygame.sprite.LayeredDirty = pygame.sprite.LayeredDirty()
        for r in self.grid:
            for t in r:
                self.tiles.add(t)
    @property
    def tilesCount(self):
        return (self.w)*(self.h)
    def space(self):
        return (self.w*32,self.h*32)
    def place(self,x,y,typ):
        self.grid[y][x].kill()
        self.grid[y][x] = tileRegistry.get(typ,x,y)
        
    def ViewPort(self,x,y):
        vpSX = pygame.math.clamp((x)-cobalt.graphics.grdVpCX,0,(self.w)-(cobalt.graphics.grdVpW-12))
        vpSY = pygame.math.clamp((y)-cobalt.graphics.grdVpCY,0,(self.h)-(cobalt.graphics.grdVpH-6))
        r= pygame.Rect(vpSX,vpSY,cobalt.graphics.grdVpW,cobalt.graphics.grdVpH)
        #self.tiles.update(r)
        return r

@dataclass
class link:
    x1:int
    y1:int
    x2:int
    y2:int
    
@dataclass
class entity:
    x:int
    y:int

@dataclass
class MapSaved:
    grid:list[list[str]]
    links:list[link]
    entitys:list[entity]
    startX:int =1
    startY:int =1
    
    