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
    return road   

road = draw_road(220)


root.mainloop()