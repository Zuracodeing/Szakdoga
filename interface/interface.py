import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    file_path = filedialog.askopenfilename(
        title="Kép megnyitása",
        filetypes=[("Image files", "*.jpg;*.png;*.dcm"), ("All files", "*.*")]
    )
    if file_path:
        print("Megnyitva:", file_path)
        # Itt jelennek meg a képet az ablakban

def diagnose():
    print("Diagnose függvény meghívva")
    messagebox.showinfo("Diagnose", "Diagnosztika elindítva (placeholder)")

def save_file():
    file_path = filedialog.asksaveasfilename(
        title="Kép mentése",
        defaultextension=".png",
        filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("All files", "*.*")]
    )
    if file_path:
        print("Elmentve:", file_path)
        # Itt implementáljuk a kép mentésének logikáját

root = tk.Tk()
root.title("Daganat Diagnosztikai Interface")

# Ablak mérete és pozíciója: jobb felső sarok
window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
x = screen_width - window_width
y = 0
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# PNG ikon beállítása
icon = tk.PhotoImage(file="icon.png")  # Valami rendes icont keresni!
root.iconphoto(False, icon)

# Menü létrehozása
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
menu_bar.add_command(label="Open", command=open_file)
menu_bar.add_command(label="Diagnose", command=diagnose)
menu_bar.add_command(label="Save", command=save_file)

root.mainloop()
