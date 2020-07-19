import os

import pygame
from pygame.math import Vector2
from math import sin, cos, radians, degrees, copysign
from src.mylogger import mylogger
from src.track import Track

logger = mylogger(__name__)
from src.car_state import CarState
from src.globals import SCREEN_WIDTH_PIXELS, SCREEN_HEIGHT_PIXELS, M_PER_PIXEL


class Car:
    """
    Local model of car. It has CarState() that is updated by remote server, and methods for drawing car and other static information related to car that is not transmitted over socket.
    """


    def __init__(self, track:Track=None): # TODO initialize at starting line with correct angle; this is job of model server
        self.car_state = CarState() # TODO change to init to starting line of track
        self.track=track # TODO for now just use default track TODO check if Track should be field of Car()
        # TODO change color of car to be unique, add name of car
        self.name = 'car' # TODO make part of constructor?

    def draw(self, screen):
        rotated = pygame.transform.rotate(self.image, -self.car_state.body_angle_deg)
        rect = rotated.get_rect()
        screen.blit(rotated, ((self.car_state.position_m/M_PER_PIXEL) - (int(rect.width / 2), int(rect.height / 2))))

    def locate(self):
        """ locates car on track and updates in the car_state"""
        # vs=self.track.vertices
        # minDist=None if self.closestTrackVertex==None else minDist=(self.closestTrackVertex-Vector2(vs[]))
        # for p in :

        pass

    def loadAndScaleCarImage(self):
        """ loads image for car and scales it to its actual length.
        Call only after car_state is filled by server
        """
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "../media/"+self.name+".png") # todo name of car and file should come from server
        self.image = pygame.image.load(image_path)  # load image of car

        # scale it to its length in pixels (all units are in pixels which are meters)
        # TODO use global scale of M_PER_PIXEL correctly here
        rect = self.image.get_rect()
        sc = self.car_state.length/(M_PER_PIXEL*rect.width)
        self.image = pygame.transform.scale(self.image, (int(sc * rect.width), int(sc * rect.height)))

    def reset(self):
        """ reset car to starting position"""
        x=0
        y=0
        if self.track:
            x=self.track.vertices[0][0]
            y=self.track.vertices[0][0]
        self.car_state.position_m = Vector2(x, y) # todo reset to start line of track