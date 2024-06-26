import unittest

import pygame

import cobalt.graphics
import cobalt.map

pygame.init()
class TestMap(unittest.TestCase):

    def test_space(self):
        map = cobalt.map.map(2,2)
        self.assertEqual(map.space(), (64,64))
    def test_fit(self):
        map = cobalt.map.map(1920//32,1080//32)
        w,h = map.space()
        self.assertLessEqual(w,1920)
        self.assertLessEqual(h,1080)
    def test_count(self):
        map = cobalt.map.map(1920//32,1080//32)
        self.assertGreaterEqual(map.tilesCount,1980)
        
    def test_place(self):
        map = cobalt.map.map(2,2)
        map.place(1,1,"test")
        self.assertEqual(map.grid[1][1].id,"test")
    def test_default(self):
        map = cobalt.map.map(2,2)
        self.assertEqual(map.grid[1][1].id,"void")
    def test_Scrview(self):
        map = cobalt.map.map(1920//16,1080//16)
        vp = cobalt.graphics.gridVpToScrVp(map.ViewPort(50,50))
        self.assertGreaterEqual(vp.top,0)
        self.assertGreaterEqual(vp.left,0)
        
        self.assertLessEqual(vp.top,1920)
        self.assertLessEqual(vp.left,1080)
        

if __name__ == '__main__':
    unittest.main()