import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import os


class ImageEncryptionTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryption Tool")
        self.root.configure(bg="#333333")  # Set background color to dark grey

        self.im = None
        self.original_im = None
        self.encryption_steps = []

        self.tkimage = None

        self.create_widgets()

    def create_widgets(self):
        # Set canvas background color to black
        self.canvas = tk.Canvas(self.root, width=500, height=500, bg="#222222")
        self.canvas.grid(row=0, column=0, columnspan=4)

        self.btn_select = tk.Button(self.root, text="Select Image",
                                    command=self.select_image, bg="#444444", fg="white")  # Set button colors
        self.btn_select.grid(row=1, column=0, padx=5, pady=10)

        self.btn_encrypt = tk.Button(
            self.root, text="Encrypt Image", command=self.encrypt_image, bg="#444444", fg="white")
        self.btn_encrypt.grid(row=1, column=1, padx=5, pady=10)

        self.btn_decrypt = tk.Button(
            self.root, text="Decrypt Image", command=self.decrypt_image, bg="#444444", fg="white")
        self.btn_decrypt.grid(row=1, column=2, padx=5, pady=10)

        self.btn_download = tk.Button(
            self.root, text="Download Image", command=self.download_image, bg="#444444", fg="white")
        self.btn_download.grid(row=1, column=3, padx=5, pady=10)

    def select_image(self):
        path = filedialog.askopenfilename()
        if path:
            self.original_im = Image.open(path)
            width, height = self.original_im.size
            aspect_ratio = width / height
            new_width = 500  # Width of the canvas
            new_height = int(new_width / aspect_ratio)
            self.im = self.original_im.copy().resize(
                (new_width, new_height), Image.ANTIALIAS)
            self.tkimage = ImageTk.PhotoImage(self.im)
            self.show_image()

    def show_image(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor='nw', image=self.tkimage)

    def encrypt_image(self):
        if self.im:
            pixels = self.im.load()
            for i in range(self.im.size[0]):
                for j in range(self.im.size[1]):
                    r, g, b = pixels[i, j]
                    pixels[i, j] = (255-r, 255-g, 255-b)
            self.encryption_steps.append("Encrypted")
            self.tkimage = ImageTk.PhotoImage(self.im)
            self.show_image()

    def decrypt_image(self):
        if self.im:
            pixels = self.im.load()
            for i in range(self.im.size[0]):
                for j in range(self.im.size[1]):
                    r, g, b = pixels[i, j]
                    pixels[i, j] = (255-r, 255-g, 255-b)
            self.encryption_steps.append("Decrypted")
            self.tkimage = ImageTk.PhotoImage(self.im)
            self.show_image()

    def download_image(self):
        if self.im and self.encryption_steps:
            filename = filedialog.asksaveasfilename(defaultextension=".png")
            if filename:
                if self.encryption_steps[-1] == "Encrypted":
                    im = self.im.convert("RGB")
                    im.save(filename)
                elif self.encryption_steps[-1] == "Decrypted":
                    im = self.im.convert("RGB")
                    im.save(filename)


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptionTool(root)
    root.mainloop()
