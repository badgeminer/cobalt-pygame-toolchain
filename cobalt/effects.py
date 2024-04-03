import pygame,cobalt.graphics
class effect(pygame.sprite.DirtySprite):
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

class arora(effect):
    def __init__(self, x, y) -> None:
        image = pygame.Surface([32*10, 32*10])
        
        super().__init__(x, y, image)