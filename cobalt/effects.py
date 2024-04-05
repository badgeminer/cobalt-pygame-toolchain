import pygame,cobalt.graphics,pygame_shaders
import numpy as np
class effect:
    def __init__(self) -> None:
        self.arr = np.ndarray((1920,1080,3))
    def _done(self):
        self.image = pygame.surfarray.make_surface(self.arr)

class test(effect):
    def __init__(self) -> None:
        super().__init__()
        y = np.arange(0, 1080)
        y = y//8
        y = y%255
        y = np.tile(y, (1920, 1))
        self.arr[:,:,1] = y
        
        y = np.arange(0, 1920)
        y = y//8
        y = y%255
        y = np.tile(y, (1080, 1))
        y = np.rot90(y)
        self.arr[:,:,0] = y
        self.arr = np.flipud(self.arr)
        self._done()
class pain(effect):
    def __init__(self) -> None:
        super().__init__()
        y = np.arange(0, 1080)
        y = y//8
        y = y%255
        y = np.tile(y, (1920, 1))
        self.arr[:,:,0] = y
        
        #y = np.arange(0, 1920)
        #y = y//8
        #y = y%255
        #y = np.tile(y, (1080, 1))
        #y = np.rot90(y)
        #self.arr[:,:,0] = y
        self.arr = np.flipud(self.arr)
        self._done()

class testRot(effect):
    def __init__(self) -> None:
        super().__init__()
        y = np.arange(0, 1920)
        y = y//8
        y = y%255
        
        y = np.tile(y, (1080, 1))
        y = np.rot90(y)
        y = np.flipud(y)

        self.arr[:,:,1] = y
        
        y = np.arange(0, 1920)
        y = y//8
        y = y%255
        y = np.tile(y, (1080, 1))
        y = np.rot90(y)
        self.arr[:,:,0] = y
        self.arr = np.flipud(self.arr)
        self._done()
        
class testsin(effect):
    def __init__(self) -> None:
        super().__init__()
        y = np.arange(0, 1920)
        
        #y = y//5
        y = (np.sin(y)*255)//1
        y = abs(y)
        y = y%255
        
        y = np.tile(y, (1080, 1))
        y = np.rot90(y)
        y = np.flipud(y)
        

        self.arr[:,:,1] = y
        
        y = np.arange(0, 1920)
        y = y//8
        y = (np.sin(y)*8)//1
        y = abs(y)
        y = y%255
        y = np.tile(y, (1080, 1))
        y = np.rot90(y)
        self.arr[:,:,0] = y
        self.arr = np.flipud(self.arr)
        self._done()
        
class heat:
    def __init__(self,inp) -> None:
        surf = pygame.Surface((1920,1080))
        compute_shader = pygame_shaders.ComputeShader("compute.glsl")
        texture = pygame_shaders.Texture(surf, compute_shader.ctx)
        texture.bind(0)
        tin = pygame_shaders.Texture(inp, compute_shader.ctx)
        tin.bind(1)
        compute_shader.dispatch(600, 600, 1)
        self.image = texture.as_surface()
