import tkinter 

WIDTH, HEIGHT =800,600

root = tkinter.Tk()
root.title("Rush Hour") 
root.resizable(False, False)

canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg="pink")
canvas.pack()  


def draw_road(width):
    road_x = WIDTH // 2 - width // 2
    road = canvas.create_rectangle(
        road_x, 
        0, 
        road_x + width, 
        HEIGHT, 
        fill="black"
    )

road_width = 220
draw_road(road_width)

def draw_car():
    car_width = 30
    car_height = 40
    road_x = WIDTH // 2 - road_width // 2
    road_quater = road_width // 4
    car_centre = road_x + road_quater 
    car_x = car_centre - car_width // 2
    car_y = HEIGHT - car_height
    car_x1 = car_centre + car_width // 2
    car_y1 = HEIGHT 


    car = canvas.create_rectangle(
        car_x,
        car_y,
        car_x1,
        car_y1,
        fill="blue"
    )

draw_car()


root.mainloop()