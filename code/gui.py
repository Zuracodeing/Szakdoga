import tkinter as tk
from tkinter import filedialog, messagebox
from segmentation import segment_image
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Globális változó a kiválasztott fájl elérési útjának tárolására
selected_file = None

def open_file():
    global selected_file
    file_path = filedialog.askopenfilename(
        title="Kép megnyitása",
        filetypes=[("DICOM files", "*.dcm"), ("All files", "*.*")]
    )
    if file_path:
        selected_file = file_path
        print("Megnyitva:", file_path)
        messagebox.showinfo("Open", f"Fájl megnyitva: {file_path}")

def diagnose():
    global selected_file
    if not selected_file:
        messagebox.showerror("Hiba", "Előbb nyisd meg a képet!")
        return

    image, mask = segment_image(selected_file)
    if image is None or mask is None:
        messagebox.showerror("Hiba", "Sikertelen szegmentáció!")
        return

    # Új ablak létrehozása a szegmentáció eredményének megjelenítésére
    result_window = tk.Toplevel(root)
    result_window.title("Szegmentáció Eredménye")
    result_window.geometry("800x600")

    # Matplotlib ábra létrehozása a két képet tartalmazó subplot-okkal
    fig = Figure(figsize=(8, 6))
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.imshow(image, cmap='gray')
    ax1.set_title("Eredeti kép")
    ax1.axis('off')

    ax2 = fig.add_subplot(1, 2, 2)
    ax2.imshow(mask, cmap='gray')
    ax2.set_title("Szegmentáció")
    ax2.axis('off')

    # Az ábra beágyazása a Tkinter ablakba
    canvas = FigureCanvasTkAgg(fig, master=result_window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def save_file():
    global selected_file
    if not selected_file:
        messagebox.showerror("Hiba", "Előbb nyisd meg a képet!")
        return

    image, mask = segment_image(selected_file)
    if image is None or mask is None:
        messagebox.showerror("Hiba", "Sikertelen szegmentáció!")
        return

    # A maszk mentése PNG formátumban (0-255 skálára alakítva)
    file_path = filedialog.asksaveasfilename(
        title="Szegmentáció mentése",
        defaultextension=".png",
        filetypes=[("PNG", "*.png"), ("All files", "*.*")]
    )
    if file_path:
        import cv2
        cv2.imwrite(file_path, (mask * 255).astype('uint8'))
        messagebox.showinfo("Save", f"Szegmentáció elmentve: {file_path}")

# Fő GUI ablak beállítása
root = tk.Tk()
root.title("MRI/DICOM Tumor Szegmentáció")

window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
x = screen_width - window_width
y = 0
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Menü létrehozása
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
menu_bar.add_command(label="Open", command=open_file)
menu_bar.add_command(label="Diagnose", command=diagnose)
menu_bar.add_command(label="Save", command=save_file)

root.mainloop()
