from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow Viewer")

# List of image paths (with commas added)
image_paths = [
    r"C:\Users\Admin\Pictures\Saved Pictures\pcwallpaperr-20241011-0004.jpg",
    r"C:\Users\Admin\Pictures\Saved Pictures\pcwallpaperr-20241011-0003.jpg",
    r"C:\Users\Admin\Pictures\Saved Pictures\4k_wallpaper_for_pc-20241011-0001.webp"
]

# Resize the images
image_size = (1080, 1080)
images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]

slideshow = cycle(photo_images)

label = tk.Label(root)
label.pack()

def update_image():
    photo_image = next(slideshow)
    label.config(image=photo_image)
    root.after(3000, update_image)  # call this function again after 3 seconds

play_button = tk.Button(root, text='Play Slideshow', command=update_image)
play_button.pack()

root.mainloop()
