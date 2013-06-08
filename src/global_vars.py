#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import pygame
from pygame.locals import *

pygame.init()

# connection
gameEngine = None
soundEngine = None
tcpConn = None

# player variables
myIndex = None

# gameloop
inGame = False
isLogging = True
gameState = 0
connectionStatus = ""

canMoveNow = True

editor = None

# input
inpDIR_UP = False
inpDIR_DOWN = False
inpDIR_LEFT = False
inpDIR_RIGHT = False
inpSHIFT = False
inpCTRL = False

# used for improved looping
highIndex = 0
playersOnMapHighIndex = 0
playersOnMap = []

# used for draggin picture boxes
sOffsetX = 0
sOffestY = 0

# freeze controls when getting map
gettingMap = False

# mouse tile location
cursorX = 0
cursorY = 0

# maximum classes
maxClasses = 0

# path for data files
dataPath = os.path.join('..', 'data')

# --------------------

# general
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# sdl
screenSurface = None

gameSurface = pygame.Surface((480, 352))
bgSurface = None

guiSurface = pygame.Surface((800, 600))

# surfaces
gameSurfaceXOffset = 0
gameSurfaceYOffset = 0

guiSurfaceXOffset = 0
guiSurfaceYOffset = 0

clock = pygame.time.Clock()

# fonts
textFont = pygame.font.Font(dataPath + '/fonts/Minecraftia.ttf', 12)

# tiles
tileDimension = 32

# map
mapNames = []