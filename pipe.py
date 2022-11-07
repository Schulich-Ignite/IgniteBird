class Pipe:

    def __init__(self, rect):
        self.rect = rect
        self.speed = 5


    def update(self):
        self.rect.x -= self.speed
        if(self.rect.x < -self.rect.width):
            self.rect.x = 1000
            return True
        return False

