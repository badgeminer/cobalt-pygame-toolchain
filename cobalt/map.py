from abc import ABCMeta
from dataclasses import dataclass

import pygame
from class_registry import ClassRegistry

tileRegistry = ClassRegistry()

class tile(pygame.sprite.Sprite,metaclass=ABCMeta):
    def __init__(self,x,y,img) -> None:
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = img

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

class testTile(tile):
    def __init__(self, x, y, img) -> None:
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        image = pygame.Surface([32, 32])
        image.fill((255,0,0))
        super().__init__(x, y, image)


class map:
    def __init__(self,w,h) -> None:
        self.grid = [[testTile(x,y)for x in range(w)] for y in range(h)]