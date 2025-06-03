from ocean_inna_table.segment import Segment
import pygame


class Creature:
    def __init__(self, surface):
        self.surface = surface
        self.segments = []
        self.joints = 4
        radius = 10
        for i in range(self.joints):
            self.segments.append(Segment((0 + i*radius, 0 + i*radius), radius, radius))

    def drawCreature(self):
        for segment in self.segments:
            pygame.draw.circle(self.surface, (0, 200, 0), [segment.x, segment.y], segment.radius)
