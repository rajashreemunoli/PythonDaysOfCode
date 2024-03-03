#Create a program that allows users to draw on a canvas using a GUI
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageGrab

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.canvas_width = 800
        self.canvas_height = 600
        background_color="white"
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg=background_color, bd=3, relief=tk.SUNKEN)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.setup_navbar()
        self.setup_tools()
        self.setup_events()
        self.prev_x = None
        self.prev_y = None

        # For undo/redo
        self.selected_tool = "pen"
        self.shapes = []
        self.undo_stack = []

    def setup_navbar(self):
        self.navbar = tk.Menu(self.root)
        self.root.config(menu=self.navbar)

        # File menu
        self.file_menu = tk.Menu(self.navbar, tearoff=False)
        self.navbar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Save Snapshot", command=self.take_snapshot)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        # Edit menu
        self.edit_menu = tk.Menu(self.navbar, tearoff=False)
        self.navbar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.undo)

    def setup_tools(self):
        self.selected_tool ="pen"
        self.colors = ["black", "red", "green", "blue", "yellow", "orange", "purple"]
        self.selected_color = self.colors[0]
        self.brush_sizes = [2, 4, 6, 8]
        self.selected_size = self.brush_sizes[0]
        self.pen_types = ["line", "round", "square", "arrow", "diamond"]
        self.selected_pen_type = self.pen_types[0]

        self.tool_frame = ttk.LabelFrame(self.root, text="Tools")
        self.tool_frame.pack(side=tk.RIGHT, padx=5, pady=5, fill=tk.Y)

        self.pen_button = ttk.Button(self.tool_frame, text="Pen", command=self.select_pen_tool)
        self.pen_button.pack(side=tk.TOP, padx=5, pady=5)

        self.eraser_button = ttk.Button(self.tool_frame, text="Eraser", command=self.select_eraser_tool)
        self.eraser_button.pack(side=tk.TOP, padx=5, pady=5)

        self.brush_size_label = ttk.Label(self.tool_frame, text="Brush Size:")
        self.brush_size_label.pack(side=tk.TOP, padx=5, pady=5)

        self.brush_size_combobox = ttk.Combobox(self.tool_frame, values=self.brush_sizes, state="readonly")
        self.brush_size_combobox.current(0)
        self.brush_size_combobox.pack(side=tk.TOP, padx=5, pady=5)
        self.brush_size_combobox.bind("<<ComboboxSelected>>", lambda event: self.select_size(int(self.brush_size_combobox.get())))

        self.color_label = ttk.Label(self.tool_frame, text="Color:")
        self.color_label.pack(side=tk.TOP, padx=5, pady=5)

        self.color_combobox = ttk.Combobox(self.tool_frame, values=self.colors, state="readonly")
        self.color_combobox.current(0)
        self.color_combobox.pack(side=tk.TOP, padx=5, pady=5)
        self.color_combobox.bind("<<ComboboxSelected>>", lambda event: self.select_color(self.color_combobox.get()))

        self.pen_type_label = ttk.Label(self.tool_frame, text="Pen Type:")
        self.pen_type_label.pack(side=tk.TOP, padx=5, pady=5)

        self.pen_type_combobox = ttk.Combobox(self.tool_frame, values=self.pen_types, state="readonly")
        self.pen_type_combobox.current(0)
        self.pen_type_combobox.pack(side=tk.TOP, padx=5, pady=5)
        self.pen_type_combobox.bind("<<ComboboxSelected>>", lambda event: self.select_pen_type(self.pen_type_combobox.get()))

        self.clear_button = ttk.Button(self.tool_frame, text="Clear Canvas", command=self.clear_canvas)
        self.clear_button.pack(side=tk.TOP, padx=5, pady=5)

    def setup_events(self):
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.release)

    def select_pen_tool(self):
        self.selected_tool = "pen"

    def select_eraser_tool(self):
        self.selected_tool = "eraser"
        
    def select_size(self, size):
        self.selected_size = size

    def select_color(self, color):
        self.selected_color = color

    def select_pen_type(self, pen_type):
        self.selected_pen_type = pen_type

    def draw(self, event):
        
    #If "Pen" button is selected,draw with choosen brush and color
        if self.selected_tool == "pen":
            if self.prev_x is not None and self.prev_y is not None:
                if self.selected_pen_type == "line":
                    shape_id = self.canvas.create_line(self.prev_x, self.prev_y, event.x, event.y, fill=self.selected_color,
                                            width=self.selected_size, smooth=True)
                elif self.selected_pen_type == "round":
                    x1 = event.x - self.selected_size
                    y1 = event.y - self.selected_size
                    x2 = event.x + self.selected_size
                    y2 = event.y + self.selected_size
                    shape_id = self.canvas.create_oval(x1, y1, x2, y2, fill=self.selected_color, outline=self.selected_color)
                elif self.selected_pen_type == "square":
                    x1 = event.x - self.selected_size
                    y1 = event.y - self.selected_size
                    x2 = event.x + self.selected_size
                    y2 = event.y + self.selected_size
                    shape_id = self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.selected_color, outline=self.selected_color)
                elif self.selected_pen_type == "arrow":
                    x1 = event.x - self.selected_size
                    y1 = event.y - self.selected_size
                    x2 = event.x + self.selected_size
                    y2 = event.y + self.selected_size
                    shape_id = self.canvas.create_polygon(x1, y1, x1, y2, event.x, y2, fill=self.selected_color,
                                               outline=self.selected_color)
                elif self.selected_pen_type == "diamond":
                    x1 = event.x - self.selected_size
                    y1 = event.y
                    x2 = event.x
                    y2 = event.y - self.selected_size
                    x3 = event.x + self.selected_size
                    y3 = event.y
                    x4 = event.x
                    y4 = event.y + self.selected_size
                    shape_id = self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, fill=self.selected_color,
                                               outline=self.selected_color)
                # Add to shapes list for undo/redo
                self.shapes.append(shape_id)
            self.prev_x = event.x
            self.prev_y = event.y

    #If "Eraser" button is selected,draw with choosen brush and WHITE color
        elif self.selected_tool == "eraser":
            if self.prev_x is not None and self.prev_y is not None:
                if self.selected_pen_type == "line":
                    shape_id = self.canvas.create_line(self.prev_x, self.prev_y, event.x, event.y, fill="white",
                                            width=self.selected_size, smooth=True)
                elif self.selected_pen_type == "round":
                    x1 = event.x - self.selected_size
                    y1 = event.y - self.selected_size
                    x2 = event.x + self.selected_size
                    y2 = event.y + self.selected_size
                    shape_id = self.canvas.create_oval(x1, y1, x2, y2, fill="white", outline="white")
                elif self.selected_pen_type == "square":
                    x1 = event.x - self.selected_size
                    y1 = event.y - self.selected_size
                    x2 = event.x + self.selected_size
                    y2 = event.y + self.selected_size
                    shape_id = self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="white")
                elif self.selected_pen_type == "arrow":
                    x1 = event.x - self.selected_size
                    y1 = event.y - self.selected_size
                    x2 = event.x + self.selected_size
                    y2 = event.y + self.selected_size
                    shape_id = self.canvas.create_polygon(x1, y1, x1, y2, event.x, y2, fill="white",
                                               outline="white")
                elif self.selected_pen_type == "diamond":
                    x1 = event.x - self.selected_size
                    y1 = event.y
                    x2 = event.x
                    y2 = event.y - self.selected_size
                    x3 = event.x + self.selected_size
                    y3 = event.y
                    x4 = event.x
                    y4 = event.y + self.selected_size
                    shape_id = self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, fill="white",
                                               outline="white")
                 # Add to shapes list for undo/redo
                self.shapes.append(shape_id)
            self.prev_x = event.x
            self.prev_y = event.y


    def release(self, event):
        self.prev_x = None
        self.prev_y = None

    def clear_canvas(self):
        self.canvas.delete("all")
        self.shapes = []
        self.undo_stack = []

    def take_snapshot(self):
        #self.canvas.postscript(file="snapshot.eps")
        x0 = self.canvas.winfo_rootx()
        y0 = self.canvas.winfo_rooty()
        x1 = x0 + self.canvas.winfo_width()
        y1 = y0 + self.canvas.winfo_height()
    
        im = ImageGrab.grab((x0, y0, x1, y1))
        im.save('snapshot.png')

    def undo(self):
        # items = self.canvas.find_all
        # print(items)
        # if items:
        #     self.canvas.delete(items[-1])
        if self.shapes:
            shape_id = self.shapes.pop()
            self.undo_stack.append(shape_id)
            self.canvas.delete(shape_id)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Paint Application")
    app = PaintApp(root)
    root.mainloop()