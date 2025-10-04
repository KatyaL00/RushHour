import tkinter 

WIDTH, HEIGHT =800,600

root = tkinter.Tk()
root.title("Rush Hour") 
root.resizable(False, False)

canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg="pink")
canvas.pack()  




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
    return x0,y0,x1,y1

road_width = 220
x0,y0,x1,y1 = draw_road(road_width)

def draw_car(x0,y0,x1,y1):
    car_width = 30
    car_height = 40
    road_x = x0
    road_quater = (x1 - x0) // 4
    car_centre = road_x + road_quater 
    car_x = car_centre - car_width // 2
    car_y = y1 - car_height
    car_x1 = car_centre + car_width // 2
    car_y1 = y1 


    car = canvas.create_rectangle(
        car_x,
        car_y,
        car_x1,
        car_y1,
        fill="blue"
    )
    return car

car = draw_car(x0,y0,x1,y1)

def update():
    car_pos = canvas.coords(car)
    print("Car position:", car_pos)

    if car_pos[3] > 0:
        x0 = 0
        y0 = -10

        canvas.move(car, x0, y0)
        root.after(50, update)


update()
root.mainloop()