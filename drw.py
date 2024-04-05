import pygame,sys

import cobalt.graphics,cobalt.effects
import cobalt.map
pygame.init()

ld = cobalt.effects.test()
#o = cobalt.effects.heat(ld.image)
pygame.image.save(ld.image,"test.png")