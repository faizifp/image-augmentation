#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import random

from enum import Enum

### CONSTANTS MEANT TO BE EDITED ###

# default number of files given as output for each input image
N_FILES_OUTPUT    = 20

# allowed input images extensions
IMAGE_EXTENSIONS  = [ ".jpg",
                      ".jpeg",
                      ".png",
                      ".bmp",
                      ".jp2",
                      ".dib",
                      ".webp",
                      ".sr",
                      ".ras",
                      ".tiff",
                      ".tif",
                      ".pbm",
                      ".pgm",
                      ".ppm" ]

# default input images path
FILES_INPUT_PATH  = "./input/"

# default output images path
FILES_OUTPUT_PATH = "./output/"

'''
max number of transformations
that are randomly applied for each output image.
If N_TRANSFORMATIONS > total number of transformations
specified in the MaxTransformation field
N_TRANSFORMATIONS will be reset as:
min( sum_MaxTransformation_fields, N_TRANSFORMATIONS) )
'''
N_TRANSFORMATIONS = 200

'''
MaxTransformation contains, for each transformation,
the number of times that each transformation is performed.
Useful to apply some transformations more often ( n > 1 )
or to exclude them` altogether ( n = 0 )
'''
class MaxTransformation:
    SALT_PEPPER_NOISE   = 5
    SPECKLE_NOISE       = 5
    GAUSS_NOISE         = 5
    BLUR                = 5

    SHADOW              = 5
    ENHANCEMENTS        = 5
    SHADE_COLOR         = 5

    # The following transformations
    # will alter pixel coordinates
    SHEAR               = 5
    SKEW                = 5
    WARP                = 5
    ROTATION            = 5

# MIN/MAX AVG BLURRING
MIN_BLUR 		= 1
MAX_BLUR 		= 3

# MIN/MAX GAUSS NOISE
MIN_GAUSS_NOISE 	= 1
MAX_GAUSS_NOISE 	= 100

# MIN/MAX SALT AND PEPPER NOISE
MIN_SALT_PEPPER_NOISE 	= 0.0001
MAX_SALTPEPPER_NOISE 	= 0.001

# MIN/MAX SPECKLE
MIN_SPECKLE_NOISE 	= 0.01
MAX_SPECKLE_NOISE 	= 0.3

# MIN/MAX SHADOW
MIN_SHADOW       	= 0.3
MAX_SHADOW       	= 0.7

# MIN/MAX IMAGE BRIGHTNESS
MIN_BRIGHTNESS   	= 0.6
MAX_BRIGHTNESS   	= 1.4

# MIN/MAX IMAGE CONTRAST
MIN_CONTRAST   	        = 0.5
MAX_CONTRAST   	        = 1.7

# MIN/MAX IMAGE SHARPNESS
MIN_SHARPNESS   	= 0.1
MAX_SHARPNESS   	= 5.0

# MIN/MAX COLOR SHADING
MIN_COLOR_SHADE 	= 0.06
MAX_COLOR_SHADE 	= 0.35

# MAX SHEAR DISTORTION
MAX_SHEAR        	= 0.05

# MAX SKEW DISTORTION
MAX_SKEW        	= 0.05

# MIN/MAX WARP DISTORTION
MIN_WARP        	= 14
MAX_WARP        	= 50

# MIN/MAX ROTATION ANGLE
MAX_ANGLE        	= 0.02

# By default s&p and speckle noise
# is followed by blurring
ADD_BLUR_AFTER_SPECKLE_NOISE = False
ADD_BLUR_AFTER_SP_NOISE      = False

READ_IMAGE_AS_GRAYSCALE = False


### PAY ATTENTION BEFORE EDITING THE FOLLOWING CONSTANTS ###

BLACK       = 0
LIGHT_BLACK = 50
DARK_GRAY   = 100
GRAY        = 150
LIGHT_GRAY  = 200
DARK_WHITE  = 250
WHITE       = 255


class Enhancement(Enum):
    brightness  = 0
    contrast    = 1
    sharpness   = 2

    @staticmethod
    def get_random():
        return random.choice(list(Enhancement))


class Channels(Enum):
    bgr = 0
    hsv = 1
    hls = 2

    @staticmethod
    def get_random():
        return random.choice(list(Channels))
