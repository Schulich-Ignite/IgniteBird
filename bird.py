class Bird:
    def __init__(self, rect):
        self.rect = rect
        self.speed_x = 0
        self.speed_y = 0
        self.gravity = 0.6

    def update(self):
        self.move(self.speed_x, self.speed_y)
        self.speed_y += self.gravity
 
    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y
 
    def jump(self):
        self.speed_y = -10

