class traffic_light:
    traffic_light_box = None
    canvas = None

    def __init__(self, box, canvas):
        self.canvas = canvas
        self.traffic_light_box = canvas.create_rectangle(
            box.x0,
            box.y0,
            box.x1,
            box.y1,
            fill= "green"
        )

    def update(self):
        pass