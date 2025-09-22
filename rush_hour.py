import tkinter 

WIDTH, HEIGHT = 600,600

root = tkinter.Tk()
root.title("Rush Hour") 
root.resizable(False, False)


canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg="pink")

canvas.pack()  

root.mainloop()