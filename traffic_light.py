import time

class traffic_light:
    traffic_light_box = None
    canvas = None
    last_change_time = None
    colors = ["green", "red"]
    color_index = 0
    CHANGE_INTERVAL = 5  # seconds

    def __init__(self, box, canvas):
        self.canvas = canvas
        self.traffic_light_box = canvas.create_rectangle(
            box.x0,
            box.y0,
            box.x1,
            box.y1,
            fill=self.colors[0]
        )
        self.last_change_time = time.time()

    def update(self):
        current_time = time.time()
        time_differance = current_time - self.last_change_time
        if time_differance >= self.CHANGE_INTERVAL:
            print(time_differance)
            # Change to next color
            self.color_index += 1
            if self.color_index >= len(self.colors):
                self.color_index = 0

            self.canvas.itemconfig(
                self.traffic_light_box,
                fill = self.colors[self.color_index]
            )
            self.last_change_time = current_time