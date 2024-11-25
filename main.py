import tkinter as tk
from tkinter import messagebox
import pyqrcode
from PIL import Image, ImageTk

def generate_qr_code():
    link = entry.get()
    if not link:
        messagebox.showwarning("Warning", "Please enter a link.")
        return

    qr = pyqrcode.create(link)
    qr.png("qrcode.png", scale=8)

    # Carregar a imagem do QR Code
    img = Image.open("qrcode.png")
    img = img.resize((250, 250), Image.ANTIALIAS)
    img_tk = ImageTk.PhotoImage(img)

    # Exibir a imagem na interface
    qr_code_label.config(image=img_tk)
    qr_code_label.image = img_tk  # Manter uma referência à imagem

# Criar a janela principal
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# Estilizar a interface
title_label = tk.Label(root, text="QR Code Generator", font=("Roboto", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

entry_label = tk.Label(root, text="Enter your social media link:", bg="#f0f0f0")
entry_label.pack(pady=5)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code, bg="#4CAF50", fg="white")
generate_button.pack(pady=10)

qr_code_label = tk.Label(root, bg="#f0f0f0")
qr_code_label.pack(pady=10)

# Iniciar o loop da interface
root.mainloop()