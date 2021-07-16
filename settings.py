class Settings:
    """存储游戏Aim Genius中所有设置的类。"""

    def __init__(self):
        """初始化静态设置。"""
        # 初始化屏幕静态设置。
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        # 初始化目标静态设置。
        self.target_color = (60, 120, 216)
        self.target_origin_radius = 10

    def reset_dynamic_settings(self):
        """初始化动态设置。"""
        # 初始化目标动态设置。
        self.target_enlarge_scale = 1.005
