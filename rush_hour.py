import tkinter 
import random

WIDTH, HEIGHT =800,600

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
    def from_points(cls, x0, y0, x1, y1):
        return cls(x0, y0, x1, y1)

    @classmethod
    def from_size(cls, width, height):
        return cls(0, 0, width, height)

    def width(self):
        return self.x1 - self.x0    
    
    def height(self):
        return self.y1 - self.y0


def draw_road(width):
    x0 = WIDTH // 2 - width // 2
    y0 = 0

    x1 = x0 + width
    y1 = HEIGHT

    road = canvas.create_rectangle(
        x0, 
        y0, 
        x1, 
        y1, 
        fill="black"
    )
    road_box = rectangle.from_points(x0, y0, x1, y1)

    return road_box

def spawn_car(road_box):
    car_box = rectangle.from_size(30, 40)

    car = canvas.create_rectangle(
        car_box.x0,
        car_box.y0,
        car_box.x1,
        car_box.y1,
        fill="blue"
    )

    move_x = road_box.x0 + (road_box.width() // 4) - (car_box.width() // 2)
    move_y = road_box.y1 - car_box.height()
    canvas.move(car, move_x, move_y)

    cars.append(car)

def move_cars():
    for car in list(cars): 
        car_pos = canvas.coords(car)
        if car_pos[3] > 0:
            x0 = 0
            y0 = -10
            canvas.move(car, x0, y0)
        else:
            canvas.delete(car)
            cars.remove(car)


def update():
    number = random.random()
    if number < 0.1:
        print("random number", number)
        spawn_car(road_box)
    move_cars()
    root.after(50, update)


root = tkinter.Tk()
root.title("Rush Hour") 
root.resizable(False, False)

canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg="pink")
canvas.pack()  


road_width = 220
road_box = draw_road(road_width)
cars = []
spawn_car(road_box)

update()
root.mainloop()





