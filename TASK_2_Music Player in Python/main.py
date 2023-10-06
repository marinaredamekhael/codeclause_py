import os
import tkinter as tk
from tkinter import font, messagebox
import pygame

# set the directory where the music files are located
MUSIC_DIR = "D:\\codeclause_py\\TASK_2_Music Player in Python\\song"

# create a list of music files
music_files = [os.path.join(MUSIC_DIR, file) for file in os.listdir(MUSIC_DIR) if file.endswith(".mp3")]

# initialize pygame
pygame.mixer.init()

# create the main window using tkinter
window = tk.Tk()
window.title("🎵Music Player")
window.geometry("600x500")
window.configure(bg='light grey')

# Custom fonts
btn_font = font.Font(size=12, weight="bold")
label_font = font.Font(size=14)

# Label for list of songs
label = tk.Label(window, text="Available Songs:", bg='light grey', font=label_font)
label.grid(row=0, column=0, pady=10, padx=20, sticky="w")

# Listbox for displaying the available songs
listbox = tk.Listbox(window, bg='white', width=45, height=10, font=btn_font)
for i, file in enumerate(music_files):
    listbox.insert(i, os.path.basename(file))
listbox.grid(row=1, column=0, padx=20, pady=10, columnspan=4)

# Functions and error handling for buttons
def play_song():
    try:
        pygame.mixer.music.load(music_files[listbox.curselection()[0]])
        pygame.mixer.music.play()
    except IndexError:
        messagebox.showerror("Error", "No song selected!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def next_song():
    try:
        # Logic to loop back to the first song when the last song is reached
        next_index = (listbox.curselection()[0] + 1) % len(music_files)
        pygame.mixer.music.load(music_files[next_index])
        pygame.mixer.music.play()
    except IndexError:
        messagebox.showerror("Error", "No song selected!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# create the buttons for controlling the music player
play_button = tk.Button(window, text="Play", command=play_song, bg='green', fg='white', font=btn_font)
play_button.grid(row=2, column=0, pady=10)

stop_button = tk.Button(window, text="Stop", command=pygame.mixer.music.stop, bg='red', fg='white', font=btn_font)
stop_button.grid(row=2, column=1, pady=10)

next_button = tk.Button(window, text="Next", command=next_song, bg='blue', fg='white', font=btn_font)
next_button.grid(row=2, column=2, pady=10)

pause_button = tk.Button(window, text="Pause", command=pygame.mixer.music.pause, bg='orange', fg='white', font=btn_font)
pause_button.grid(row=2, column=3, pady=10)

unpause_button = tk.Button(window, text="Unpause", command=pygame.mixer.music.unpause, bg='purple', fg='white', font=btn_font)
unpause_button.grid(row=3, column=0, pady=10, columnspan=2)

# create the volume control slider
volume_label = tk.Label(window, text="Volume Control:", bg='light grey', font=label_font)
volume_label.grid(row=3, column=2, pady=10, padx=10, sticky="w")

volume_slider = tk.Scale(window, from_=0, to=1, resolution=0.1, orient="horizontal", length=150,
                         command=lambda vol: pygame.mixer.music.set_volume(float(vol)), bg='light grey', troughcolor='BLUE')
volume_slider.set(0.5)
volume_slider.grid(row=3, column=3, pady=10)

window.mainloop()
