class rectangle:
    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0

    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

    @classmethod
    def create_from_points(cls, x0, y0, x1, y1):
        return cls(x0, y0, x1, y1)

    @classmethod
    def create_from_size(cls, width, height):
        return cls(0, 0, width, height)

    def width(self):
        return self.x1 - self.x0    
    
    def height(self):
        return self.y1 - self.y0
