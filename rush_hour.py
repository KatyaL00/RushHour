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
    route = None
    canvas = None

    def __init__(self, canvas, road_box, car_box, route ):

        self.route = route
        self.canvas = canvas
        self.car_rectangle = canvas.create_rectangle(
            car_box.x0,
            car_box.y0,
            car_box.x1,
            car_box.y1,
            fill=self.color
        )

        if self.route == direction.UP_DOWN:
            move_x = road_box.x0 + (road_box.width() // 4) * 3 - (car_box.width() // 2)
            move_y = 0
            self.step = 10
            self.final_point = road_box.height() + car_box.height()
        else:
            move_x = road_box.x0 + (road_box.width() // 4) - (car_box.width() // 2)
            move_y = road_box.y1 - car_box.height()
            self.step = -10
            self.final_point = 0
        self.canvas.move(self.car_rectangle, move_x, move_y)

    def move(self) -> bool:
        """Move the car in its designated direction and return whether it should continue moving.
        
        Returns:
            bool: False if the car has reached its endpoint and should be removed, True otherwise
        """
        car_pos = self.canvas.coords(self.car_rectangle)
        current_y = car_pos[3]  # Bottom y-coordinate of the car
        
        # Check if car has reached its endpoint based on direction
        has_reached_endpoint = False
        if self.route == direction.UP_DOWN:
            if current_y > self.final_point:
                has_reached_endpoint = True
        else:  # direction.DOWN_UP
            if current_y < self.final_point:
                has_reached_endpoint = True
        
        if has_reached_endpoint:
            self.canvas.delete(self.car_rectangle)
            return False
            
        # Move the car one step in its direction
        self.canvas.move(self.car_rectangle, 0, self.step)
        return True

class trafic_light:
    trafic_light_box = None
    canvas = None

    def __init__(self, box, canvas):
        self.canvas = canvas
        self.trafic_light_box = canvas.create_rectangle(
            box.x0,
            box.y0,
            box.x1,
            box.y1,
            fill= "green"
        )

    def update(self):
        pass

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

    
    trafic_light_high = 40
    trafic_light_x0 = x0
    trafic_light_y0 = y1 // 2 - trafic_light_high // 2

    trafic_light_x1 = x1
    trafic_light_y1 = trafic_light_y0 + trafic_light_high 

    trafic_light_box = rectangle.create_from_points(
        trafic_light_x0,
        trafic_light_y0,
        trafic_light_x1,
        trafic_light_y1        
    )

    light = trafic_light(trafic_light_box, canvas)   

    return road_box, light

def spawn_car(road_box):
    # choose random width in [15,30] and height in [20,40]
    width = random.randint(15, 30)
    height = random.randint(20, 40)

    car_box = rectangle.create_from_size(width, height)
    number = random.random()
    if number < 0.5:
        item = car(canvas, road_box, car_box, direction.UP_DOWN)
    else:
        item = car(canvas, road_box, car_box, direction.DOWN_UP)
    cars.append(item)

def move_cars():
    for item in list(cars): 
        if item.move() == False:
            cars.remove(item)
        

def update():
    number = random.random()
    if number < 0.1:
        print("random number", number)
        spawn_car(road_box)
    light.update()
    move_cars()
    root.after(50, update)


if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Rush Hour") 
    root.resizable(False, False)

    canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg="pink")
    canvas.pack()  


    road_width = 220
    road_box, light = draw_road(road_width)
    

    cars = []
    spawn_car(road_box)

    update()
    root.mainloop()




