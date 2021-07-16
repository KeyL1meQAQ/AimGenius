import sys

import pygame
import random
from settings import Settings
from target import Target


class AimGen:
    """管理游戏行为和资源的类。"""

    def __init__(self):
        """初始化游戏。"""
        self.settings = Settings()
        self.settings.reset_dynamic_settings()

        # 设置游戏全屏显示。
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Aim Genius")

        # 创建目标编组。
        self.targets = pygame.sprite.Group()

    def run_game(self):
        """启动游戏。"""
        while True:
            self._check_events()
            self._update_screen()

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕。"""
        self.screen.fill(self.settings.bg_color)
        self._manage_target()

        pygame.display.flip()

    def _check_events(self):
        """响应按键和鼠标事件。"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_hit(mouse_pos)

    def _check_keydown_events(self, event):
        """响应键盘按下事件。"""
        if event.key == pygame.K_q:
            sys.exit()

    def _check_hit(self, mouse_pos):
        """判断是否命中目标，此处判断目标的外接矩形与鼠标点击点是否发生碰撞。"""
        hit_count = 0
        for target in self.targets.sprites():
            target_limit_R = target.target_x + target.target_radius
            target_limit_L = target.target_x - target.target_radius
            target_limit_T = target.target_y + target.target_radius
            target_limit_B = target.target_y - target.target_radius
            if target_limit_R > mouse_pos[0] > target_limit_L and target_limit_T > mouse_pos[1] > target_limit_B:
                hit_count += 1
                self.targets.remove(target)

    def _manage_target(self):
        """管理目标。"""
        self._generate_target()
        self._draw_target()

    def _generate_target(self):
        """生成目标。"""
        flag = random.randint(0, 99)
        if flag == 1:
            new_target = Target(self)
            self.targets.add(new_target)

    def _draw_target(self):
        """在屏幕上绘制目标。"""
        for target in self.targets.sprites():
            if target.is_too_large():
                self.targets.remove(target)
            else:
                target.draw()
        self.targets.update()


if __name__ == "__main__":
    ag = AimGen()
    ag.run_game()
