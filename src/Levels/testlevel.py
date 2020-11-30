"""
Тестовый уровень для нужд програмистов
TODO: чем-нибудь напольникть уровень
"""
import pygame
import pymunk

from Engine.Scene.game_objects import StaticRectangularObject, DynamicRectangularObject, DynamicCircularObject
from Engine.Scene.gamescene import SunnyField, Level
from Engine.Scene.physical_primitives import PhysicalRect


class TestLevel(Level):
    def __init__(self, game_app):
        super(TestLevel, self).__init__(game_app, SunnyField(), PhysicalRect(-16, -9, 32, 18))

        # Инициализация игрока
        self.init_player(0, 0.1, 0.96, 1.8, sprite=pygame.image.load('src/Levels/Boxer2_Idle_000.png'),
                         animations_config="src/Levels/test.yaml")

        # граница горизонта (чтобы человек не проваливался под землю)
        self.hl = pymunk.Segment(self.physical_space.static_body,
                            (self.border.x, 0),
                            (self.border.x + self.border.width, 0),
                            0)
        self.hl.friction = 1

        self.physical_space.add(self.hl)

        self.objects.append(StaticRectangularObject(2, 0, 1, 0.7, sprite=pygame.image.load('src/Levels/monalisa.jpg'),
                                                    physical_space=self.physical_space))
        self.objects.append(
            DynamicRectangularObject(2, 3, 1, 0.7, sprite=pygame.image.load('src/Levels/monalisa.jpg').convert_alpha(),
                                     physical_space=self.physical_space))

        self.objects.append(DynamicRectangularObject(2, 5, 1, 0.7, physical_space=self.physical_space, angle=0.8))
        self.objects.append(DynamicCircularObject(1, 5, 0.7, physical_space=self.physical_space))
        self.objects.append(DynamicCircularObject(1, 5, 0.7, physical_space=self.physical_space,
                                                  sprite=pygame.image.load(
                                                      'src/Levels/582ab5e93efcb_smaylik.png').convert_alpha()))
