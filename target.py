import pygame
import random

from pygame.sprite import Sprite


class Target(Sprite):
    """管理游戏的射击目标。"""

    def __init__(self, ag_game):
        """初始化目标并设置其位置。"""
        super().__init__()
        self.settings = ag_game.settings
        self.screen = ag_game.screen
        self.screen_rect = ag_game.screen.get_rect()

        # 随机生成目标圆心的x和y坐标。
        self.target_x = random.randint(50, self.settings.screen_width - 50)
        self.target_y = random.randint(50, self.settings.screen_height - 50)
        self.target_radius = self.settings.target_origin_radius

    def draw(self):
        """在指定位置绘制目标。"""
        pygame.draw.circle(self.screen, self.settings.target_color, (self.target_x, self.target_y),
                           self.target_radius)

    def update(self):
        """更新目标的大小，每个目标都会随时间变大。"""
        self.target_radius *= self.settings.target_enlarge_scale

    def is_too_large(self):
        """判断目标是否过大。"""
        if self.target_radius > 50:
            return True
        return False
