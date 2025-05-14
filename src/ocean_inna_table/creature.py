from ocean_inna_table.segment import Segment
import pygame


class Creature:
    def __init__(self, surface):
        self.surface = surface
        self.segments = []
        self.joints = 4
        radius = 30
        for i in range(self.joints):
            self.segments.append(Segment((0 + i*radius, 0 + i*radius), radius, radius))

    def drawCreature(self):
        for i in self.segments:
            pygame.draw.circle(self.surface, (0, 200, 0), [self.segments[i].x, self.segments[i].y], self.segments[i].radius)
