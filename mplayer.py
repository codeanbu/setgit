import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("300x200")
        pygame.mixer.init()
        self.current_song = ""
        self.paused = False
        self.load_button = tk.Button(self.root, text="Load Song", command=self.load_song)
        self.load_button.pack(pady=10)
        self.play_button = tk.Button(self.root, text="Play", command=self.play_song)
        self.play_button.pack(pady=10)
        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_song)
        self.pause_button.pack(pady=10)
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_song)
        self.stop_button.pack(pady=10)
        self.volume_scale = tk.Scale(self.root, from_=0, to=1, orient=tk.HORIZONTAL, resolution=0.1, label="Volume", command=self.change_volume)
        self.volume_scale.set(0.5)
        self.volume_scale.pack(pady=10)

    def load_song(self):
        self.current_song = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        if self.current_song:
            pygame.mixer.music.load(self.current_song)
            self.root.title(f"Playing: {self.current_song.split('/')[-1]}")
    def pause_song(self):
        if not self.paused:
            pygame.mixer.music.pause()
            self.paused = True
        else:
            pygame.mixer.music.unpause()
            self.paused = False
    def play_song(self):
        if self.current_song:
            pygame.mixer.music.play()
            self.paused = False
    def change_volume(self, value):
        pygame.mixer.music.set_volume(float(value))
    def stop_song(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
   
