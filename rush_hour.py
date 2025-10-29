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
    def create_from_points(cls, x0, y0, x1, y1):
        return cls(x0, y0, x1, y1)

    @classmethod
    def create_from_size(cls, width, height):
        return cls(0, 0, width, height)

    def width(self):
        return self.x1 - self.x0    
    
    def height(self):
        return self.y1 - self.y0

class direction:
    UP_DOWN = 1
    DOWN_UP = 2

class car:
    car_rectangle = None
    color = "blue"
    step = 0
    final_point = 0

    def __init__(self, canvas, road_box, car_box, route ):
        self.car_rectangle = canvas.create_rectangle(
            car_box.x0,
            car_box.y0,
            car_box.x1,
            car_box.y1,
            fill=self.color
        )

        if self.route ==direction.UP_DOWN:
            move_x = road_box.x0 + (road_box.width() // 4) * 3 - (car_box.width() // 2)
            move_y = 0
            self.step = 10
            self.final_point = road_box.height() + car_box.height()
        else:
            move_x = road_box.x0 + (road_box.width() // 4) - (car_box.width() // 2)
            move_y = road_box.y1 - car_box.height()
            self.step = -10
            self.final_point = 0
        canvas.move(self.car_rectangle, move_x, move_y)

    @classmethod
    def create_car(cls, canvas, road_box, car_box, route):
        return cls(canvas, road_box, car_box, route)

    def move(self, canvas):
        car_pos = canvas.coords(self.car_rectangle)
        

        if car_pos[3] > self.final_point:
            x0 = 0
            y0 = self.step
            canvas.move(self.car_rectangle, x0, y0)
            return True
        else:
            canvas.delete(self.car_rectangle)
            return False

class car_down_up:
    car_rectangle = None
    color = "blue"

    def __init__(self, canvas, road_box, car_box):
        self.car_rectangle = canvas.create_rectangle(
            car_box.x0,
            car_box.y0,
            car_box.x1,
            car_box.y1,
            fill=self.color
        )

        move_x = road_box.x0 + (road_box.width() // 4) - (car_box.width() // 2)
        move_y = road_box.y1 - car_box.height()
        canvas.move(self.car_rectangle, move_x, move_y)

    @classmethod
    def create_car(cls, canvas, road_box, car_box):
        return cls(canvas, road_box, car_box)

    def move(self, canvas):
        car_pos = canvas.coords(self.car_rectangle)
        if car_pos[3] > 0:
            x0 = 0
            y0 = -10
            canvas.move(self.car_rectangle, x0, y0)
            return True
        else:
            canvas.delete(self.car_rectangle)
            return False


class car_up_down:
    car_rectangle = None
    color = "blue"

    def __init__(self, canvas, road_box, car_box):
        self.car_rectangle = canvas.create_rectangle(
            car_box.x0,
            car_box.y0,
            car_box.x1,
            car_box.y1,
            fill=self.color
        )

        move_x = road_box.x0 + (road_box.width() // 4) * 3 - (car_box.width() // 2)
        move_y = 0
        canvas.move(self.car_rectangle, move_x, move_y)

    @classmethod
    def create_car(cls, canvas, road_box, car_box):
        return cls(canvas, road_box, car_box)

    def move(self, canvas):
        car_pos = canvas.coords(self.car_rectangle)
        if car_pos[3] > 0:
            x0 = 0
            y0 = 10
            canvas.move(self.car_rectangle, x0, y0)
            return True
        else:
            canvas.delete(self.car_rectangle)
            return False



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
    road_box = rectangle.create_from_points(x0, y0, x1, y1)

    return road_box

def spawn_car(road_box):
    # choose random width in [15,30] and height in [20,40]
    width = random.randint(15, 30)
    height = random.randint(20, 40)

    car_box = rectangle.create_from_size(width, height)
    number = random.random()
    if number < 0.5:
        item = car.create_car(canvas, road_box, car_box, direction.UP_DOWN)
    else:
        item = car.create_car(canvas, road_box, car_box, direction.DOWN_UP)
    cars.append(item)

def move_cars():
    for item in list(cars): 
        if item.move(canvas) == False:
            cars.remove(item)
        

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





