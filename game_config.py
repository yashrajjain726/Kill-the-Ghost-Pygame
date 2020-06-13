import os

IMAGE_SIZE=128
SCREEN_SIZE =512
NUM_TILES_SIDE=4
NUM_TILES_TOTAL=16

#Margin between two images from each side
MARGIN=4

ASSET_DIR='assets'

#create the list of all the assets by looping over them
ASSETS_FILE=[x for x in os.listdir(ASSET_DIR) if x[-3:].lower()=='png']

#counting the len of assets is equal to total assets
assert len(ASSETS_FILE)==8