diameter = None
length = None
max_speed = None
cam_mtx = [[94.861, 0, 119.506], [0, 119.511, 114.969], [0, 0, 1]]
mtx = [[108.8354211,   0.,        115.22432999],
           [  0.,        140.25241086, 78.99617583],
           [  0.,          0.,          1.,       ]]
newcameramtx = [[ 45.32413483,  0.,        138.37312359],
                [  0.,         77.69929504, 95.08531778],
                [  0.,          0.,          1.        ]]
dist = [[-0.28889063, 0.07566187, 0.01182208, 0.00057297,-0.00827746]]
AT_size = None

# -*- coding: utf-8 -*-
"""
 
 Title: Constants-File
 Author: Anton ELmiger
 Created: 2020-06-23

 Information: all parameters of the whole image processing are stored in this module
              and can be administrated and modified here

"""

######################### MODE CONSTS #########################
MODE = "video"                      # set mode: "camera" = live camera input, "video" = video input, "simulink" = simulink input
VISUALIZE = True                    #  set to True or False to visualize lane detection
WRITE_VIDEO = True                 # Write Video File after Execution
PRINT_TIME_PER_FRAME = False         # Print ms per loop in console
######################### PATH CONSTS #########################
PATH = ""  # path of the current directory ("workspace") 
VIDEO_FILE = PATH + "output.avi"    # filename of video file

######################### IMG  CONSTS #########################
IMAGE_WIDTH = 67
IMAGE_HEIGHT = 58

######################## LANE DETECTION #######################
LANE_WIDTH = 2.12                        # specify lane width. no specific unit
BOUNDARY_THRESH = .5                   # smaller value means a broader search area for boundary points
# HORIZON = 80.1                         # horizon in image pixel. NEEDS TO HAVE A DECIMAL PLACE TO AVOID DIVISION BY 0 (80 => 80.1)
HORIZON = 40.5
FILTER_STRENGTH = 1                    # number of frames where lane is smoothed with moving average
