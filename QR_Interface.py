# COPYRIGHT (C)2022-2023 ALL RIGHTS RESERVED
# SEE GITHUB REPO FOR LICENSE INFO

import tkinter as tk
from PIL import Image, ImageTk
import qrcode


# Declare empty var
img = qrcode.make(data=None)


# Generate qr image based on entry
def generate_qrcode():
    global img
    global QRImage
    input = entry.get()
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        #box_size = 20,
        #border = 5,
        )

    qr.add_data(input)
    qr.make(fit=True)
    img = qr.make_image(fill="black", backcolor="white")
    generatedimage = ImageTk.PhotoImage(img)
    label2.configure(image=generatedimage)
    label2.image = generatedimage

# Save Generated Image
def save_qr():
    global img
    url = entry.get()
    suffix = '.png'
    filename = 'QR'
    img.save(f'{filename}_{url}{suffix}')



# GUI

root = tk.Tk()
root.title("QR Generator")
root.geometry("400x500")
root.title("QR Generator v0.15 - (C)2023")

label1 = tk.Label(root, text="Enter your url and click Generate QR image", font=('Arial', 8))
label1.pack(pady=5)

entry = tk.Entry(root, textvariable="CustomUrl")
entry.pack(pady=5)

button1 = tk.Button(root, text = "Generate QR image", command=generate_qrcode)
button1.pack(pady=5)

button2 = tk.Button(root, text = "Save QR image", command=save_qr)
button2.pack(pady=5)

QRImage = ImageTk.PhotoImage(img)

label2 = tk.Label(root, image = QRImage)
label2.pack()



root.mainloop()






