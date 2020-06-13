import os
import random
import game_config as gc

from pygame import image, transform

#creating a dictionary
zombie_count=dict((a,0)for a in gc.ASSETS_FILE)

def available_zombie():
    #returning those keys whose values are less than 2,because 
    # we have to match the images.
    return [ a for a,c in zombie_count.items() if c < 2 ]

class Zombie:
    def __init__(self,index):
        #index will be in range of 15(inclusive),because we are 
        # displaying a grid (4 x 4) images with zero-indexing.
        self.index = index
        self.row = index // gc.NUM_TILES_SIDE 
        self.col = index % gc.NUM_TILES_SIDE 
        self.name = random.choice(available_zombie())
        zombie_count[self.name] += 1
        self.image_path = os.path.join(gc.ASSET_DIR,self.name)
        self.image=image.load(self.image_path)
        self.image = transform.scale(self.image,(gc.IMAGE_SIZE-2*gc.MARGIN,gc.IMAGE_SIZE-2*gc.MARGIN))
        self.box=self.image.copy()
        self.box.fill((255,255,255))
        #if the zombie's are already matched then,we should skip it,
        # because that's removed from the gameboard.
        self.skip= False
