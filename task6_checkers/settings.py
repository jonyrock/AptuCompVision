
WIDTH = 800
HEIGHT = 448

VIDEO_PATH = 'Cam1_Outdoor.mp4'
CELL_MASK_PATH = 'resources/cellColorWeight.png'

xStep = WIDTH / 8
yStep = HEIGHT / 8

PLAY_SELLS = [(i, j) for i in range(0, 8) for j in range(0, 8) if (i + j) % 2 == 1]