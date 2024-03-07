import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

def add_watermark(image_path, watermark_text, output_path):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    
    font = ImageFont.truetype("arial.ttf", 50)
    
    image_width, image_height = image.size
    
    text_width, text_height = draw.textsize(watermark_text, font)
    
    x = (image_width - text_width) // 2
    y = (image_height - text_height) // 2
    
    draw.text((x, y), watermark_text, fill="white", font=font)
    
    image.save(output_path)

def select_image():
    file_path = filedialog.askopenfilename()
    entry_path.delete(0, tk.END)
    entry_path.insert(0, file_path)

def select_save():
    file_path = filedialog.asksaveasfile()
    entry_output_path.delete(0, tk.END)
    entry_output_path.insert(0, file_path.name)

def apply_watermark():
    image_path = entry_path.get()
    output_path = entry_output_path.get()
    
    watermark_text = entry_watermark_text.get()
    
    add_watermark(image_path, watermark_text, output_path)
    
    label_status.config(text="Watermark added!")

root = tk.Tk()
root.title("Add a Watermark")

label_path = tk.Label(root, text="Chose a file:")
label_path.grid(row=0, column=0, padx=10, pady=5)

entry_path = tk.Entry(root, width=40)
entry_path.grid(row=0, column=1, padx=10, pady=5)

button_browse = tk.Button(root, text="Browse", command=select_image)
button_browse.grid(row=0, column=2, padx=10, pady=5)

label_watermark_text = tk.Label(root, text="Watermark Text:")
label_watermark_text.grid(row=1, column=0, padx=10, pady=5)

entry_watermark_text = tk.Entry(root, width=40)
entry_watermark_text.grid(row=1, column=1, padx=10, pady=5)

label_output_path = tk.Label(root, text="Path to save:")
label_output_path.grid(row=2, column=0, padx=10, pady=5)

entry_output_path = tk.Entry(root, width=40)
entry_output_path.grid(row=2, column=1, padx=10, pady=5)

button_save = tk.Button(root, text="Browse", command=select_save)
button_save.grid(row=2, column=2, padx=10, pady=5)

button_apply = tk.Button(root, text="Add watermark", command=apply_watermark)
button_apply.grid(row=3, column=1, padx=10, pady=5)

label_status = tk.Label(root, text="")
label_status.grid(row=4, column=1, padx=10, pady=5)



root.mainloop()
