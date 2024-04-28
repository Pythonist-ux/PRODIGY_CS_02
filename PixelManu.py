import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class ImageEncryptionTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryption Tool")
        self.root.configure(bg="#333333")  # Set background color to dark grey

        self.im = None  # Variable to store the image being displayed
        self.original_im = None  # Variable to store the original image
        self.encryption_steps = []  # List to keep track of encryption steps

        self.tkimage = None  # Variable to store the image displayed on the canvas

        self.create_widgets()  # Create GUI widgets

    def create_widgets(self):
        # Create a canvas to display the image
        self.canvas = tk.Canvas(self.root, width=500, height=500, bg="#222222")
        self.canvas.grid(row=0, column=0, columnspan=4)

        # Button to select an image
        self.btn_select = tk.Button(self.root, text="Select Image",
                                    command=self.select_image, bg="#444444", fg="white")
        self.btn_select.grid(row=1, column=0, padx=5, pady=10)

        # Button to encrypt the image
        self.btn_encrypt = tk.Button(
            self.root, text="Encrypt Image", command=self.encrypt_image, bg="#444444", fg="white")
        self.btn_encrypt.grid(row=1, column=1, padx=5, pady=10)

        # Button to decrypt the image
        self.btn_decrypt = tk.Button(
            self.root, text="Decrypt Image", command=self.decrypt_image, bg="#444444", fg="white")
        self.btn_decrypt.grid(row=1, column=2, padx=5, pady=10)

        # Button to download the image
        self.btn_download = tk.Button(
            self.root, text="Download Image", command=self.download_image, bg="#444444", fg="white")
        self.btn_download.grid(row=1, column=3, padx=5, pady=10)

    def select_image(self):
        # Open a file dialog to select an image file
        path = filedialog.askopenfilename()
        if path:
            # Open the selected image file
            self.original_im = Image.open(path)
            # Resize the image to fit the canvas
            width, height = self.original_im.size
            aspect_ratio = width / height
            new_width = 500  # Width of the canvas
            new_height = int(new_width / aspect_ratio)
            self.im = self.original_im.copy().resize(
                (new_width, new_height), Image.ANTIALIAS)
            # Convert the image to a Tkinter PhotoImage and display it on the canvas
            self.tkimage = ImageTk.PhotoImage(self.im)
            self.show_image()

    def show_image(self):
        # Display the image on the canvas
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor='nw', image=self.tkimage)

    def encrypt_image(self):
        # Encrypt the image if it exists and has not been encrypted already
        if self.im and "Encrypted" not in self.encryption_steps:
            pixels = self.im.load()
            for i in range(self.im.size[0]):
                for j in range(self.im.size[1]):
                    r, g, b = pixels[i, j]
                    pixels[i, j] = (255-r, 255-g, 255-b)
            # Add "Encrypted" to the encryption steps
            self.encryption_steps.append("Encrypted")
            # Update the Tkinter PhotoImage and show the encrypted image
            self.tkimage = ImageTk.PhotoImage(self.im)
            self.show_image()

    def decrypt_image(self):
        # Decrypt the image if it exists and has not been decrypted already
        if self.im and "Decrypted" not in self.encryption_steps:
            pixels = self.im.load()
            for i in range(self.im.size[0]):
                for j in range(self.im.size[1]):
                    r, g, b = pixels[i, j]
                    pixels[i, j] = (255-r, 255-g, 255-b)
            # Add "Decrypted" to the encryption steps
            self.encryption_steps.append("Decrypted")
            # Update the Tkinter PhotoImage and show the decrypted image
            self.tkimage = ImageTk.PhotoImage(self.im)
            self.show_image()

    def download_image(self):
        # Download the image if it exists and has encryption steps
        if self.im and self.encryption_steps:
            # Ask for the file name and location to save the image
            filename = filedialog.asksaveasfilename(defaultextension=".png")
            if filename:
                # Save the image based on the last encryption step
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
