import tkinter as tk
from tkinter import colorchooser
import numpy as np
import cv2

def show_color_picker(current_color):
    """Open a color picker dialog and return the selected BGR color"""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    # Convert BGR to RGB for colorchooser
    rgb_color = (current_color[2], current_color[1], current_color[0])
    
    # Open color chooser dialog
    color_code = colorchooser.askcolor(
        title="Choose drawing color",
        initialcolor=rgb_color
    )
    
    if color_code[0] is None:  # User cancelled
        return None
    
    # Convert RGB to BGR for OpenCV
    selected_rgb = color_code[0]
    selected_bgr = (selected_rgb[2], selected_rgb[1], selected_rgb[0])
    return selected_bgr

def create_color_palette_window():
    """Alternative: Create a custom palette window with predefined colors"""
    root = tk.Tk()
    root.title("Color Palette")
    
    colors = [
        ("Red", (0, 0, 255)),
        ("Green", (0, 255, 0)),
        ("Blue", (255, 0, 0)),
        ("Yellow", (0, 255, 255)),
        ("Magenta", (255, 0, 255)),
        ("Cyan", (255, 255, 0)),
        ("Black", (0, 0, 0)),
        ("White", (255, 255, 255))
    ]
    
    selected_color = None
    
    def on_color_select(bgr_color):
        nonlocal selected_color
        selected_color = bgr_color
        root.destroy()
    
    for name, bgr in colors:
        # Convert BGR to hex for tkinter
        hex_color = '#%02x%02x%02x' % (bgr[2], bgr[1], bgr[0])
        btn = tk.Button(
            root,
            text=name,
            bg=hex_color,
            fg="white" if sum(bgr) < 382 else "black",
            command=lambda c=bgr: on_color_select(c),
            width=10,
            height=2
        )
        btn.pack(pady=2, padx=2, fill=tk.X)
    
    root.mainloop()
    return selected_color