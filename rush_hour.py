import tkinter 
import random
from rectangle import rectangle
from car import car, direction
from traffic_light import traffic_light

WIDTH, HEIGHT =800,600

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

    
    traffic_light_high = 40
    traffic_light_x0 = x0
    traffic_light_y0 = y1 // 2 - traffic_light_high // 2

    traffic_light_x1 = x1
    traffic_light_y1 = traffic_light_y0 + traffic_light_high 

    traffic_light_box = rectangle.create_from_points(
        traffic_light_x0,
        traffic_light_y0,
        traffic_light_x1,
        traffic_light_y1        
    )

    light = traffic_light(traffic_light_box, canvas)   

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




