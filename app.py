import pygame
import game_config as gc
from ghost import Zombie
from pygame import display , event , image
from time import sleep

def find_index(x,y):
    row = y // gc.IMAGE_SIZE
    col = x // gc.IMAGE_SIZE
    index = row * gc.NUM_TILES_SIDE + col
    return index
#for initialize the pygame package.
pygame.init()

#display module for controlling display
#set_caption(): for changing the title of the gaming window
display.set_caption('Kill the Ghost')

#set_mode: to set the size of the game window and it also returns a 
#surface object which is a pygame object for representing image on screen
screen= display.set_mode((512,512))

#loading the killed image
killed = image.load('other_assets/killed.png')

#let us set running is True to set the game status
running=True
tiles = [Zombie(i) for i in range(0,gc.NUM_TILES_TOTAL)]
current_images=[]
while running:
    #pygame event module let's you capture all the mouse and keyboard inputs
    #with the help of get( and all the fetched inputs will be removed from the 
    #queue and return as a list.
    current_events=event.get()
    for x in current_events:
        if x.type==pygame.QUIT:
            running= False
        # If a key is pressed down .    
        if x.type==pygame.KEYDOWN:
            #If escape("Esc") is pressed than also the game will be quit.
            if x.type==pygame.K_ESCAPE:
                running=False
        # If a mouse is pressed down. 
        if x.type==pygame.MOUSEBUTTONDOWN:
            # Get the x and y axis of where the mouse is clicked.
            mouse_x, mouse_y = pygame.mouse.get_pos()
            #Get the index of the image by the x and y axis.
            index=find_index(mouse_x,mouse_y)
            if index not in current_images:
                current_images.append(index)
            # to load only less than two images from the total images,
            # we set it to below condition
            if len(current_images)>2:
                current_images=current_images[1:]
    screen.fill((255,255,255))

    total_skipped = 0   

    for _,tile in enumerate(tiles):
        image_i = tile.image if tile.index in current_images else tile.box 
        if not tile.skip :  
            screen.blit(image_i,(tile.col * gc.IMAGE_SIZE + gc.MARGIN ,tile.row * gc.IMAGE_SIZE + gc.MARGIN))
        else:
            total_skipped +=1

    display.flip()   

    if len(current_images)==2:
        #Checking that,if the two images with same name are same or not.
        idx1,idx2= current_images
        if tiles[idx1].name == tiles[idx2].name :
            tiles[idx1].skip = True
            tiles[idx2].skip = True
            sleep(0.5)
            screen.blit(killed,(0,0))
            display.flip()
            sleep(0.5)
            current_images=[]
    if total_skipped == len(tiles):
            running = False
    if total_skipped == len(tiles):
        running = False

print('Thanks for Playing')