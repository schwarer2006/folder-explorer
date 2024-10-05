import tkinter as tk
from tkinter import filedialog, Text, simpledialog, messagebox
import os

# Funktion zum Öffnen des Ordner-Explorers new
def open_folder():
    folder_path = filedialog.askdirectory()  # Zeigt den Ordnerdialog an
    if folder_path:
        folder_label.config(text=f"Ausgewählter Ordner: {folder_path}")
        show_files(folder_path)

# Funktion zum Anzeigen der Dateien im ausgewählten Ordner
def show_files(folder_path):
    # Lösche den bisherigen Inhalt in der Textbox
    file_list.delete(1.0, tk.END)
    
    # Liste alle Dateien im Ordner auf
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_list.insert(tk.END, os.path.join(root, filename) + '\n')

# Funktion zum Erstellen eines neuen Ordners
def create_new_folder():
    # Sicherstellen, dass ein Ordner ausgewählt wurde
    current_folder = folder_label.cget("text").replace("Ausgewählter Ordner: ", "")
    
    if not os.path.isdir(current_folder):
        messagebox.showerror("Fehler", "Bitte wähle zuerst einen Ordner aus.")
        return
    
    # Eingabedialog für den neuen Ordnernamen
    folder_name = simpledialog.askstring("Neuer Ordner", "Gib den Namen des neuen Ordners ein:")
    
    if folder_name:
        new_folder_path = os.path.join(current_folder, folder_name)
        
        try:
            os.makedirs(new_folder_path, exist_ok=True)
            messagebox.showinfo("Erfolg", f"Ordner '{folder_name}' wurde erstellt.")
            show_files(current_folder)  # Zeige die aktualisierte Ordnerstruktur an
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Erstellen des Ordners: {e}")

# Erstelle das Hauptfenster
root = tk.Tk()
root.title("Folder Explorer mit Ordnererstellung")

# Erstelle eine Schaltfläche zum Öffnen des Ordner-Explorers
open_button = tk.Button(root, text="Ordner öffnen", command=open_folder)
open_button.pack()

# Label, um den ausgewählten Ordner anzuzeigen
folder_label = tk.Label(root, text="Kein Ordner ausgewählt")
folder_label.pack()

# Textfeld zum Anzeigen der Dateien im Ordner
file_list = Text(root, height=20, width=80)
file_list.pack()

# Schaltfläche zum Erstellen eines neuen Ordners
new_folder_button = tk.Button(root, text="Neuen Ordner erstellen", command=create_new_folder)
new_folder_button.pack()

# Starte die Anwendung
root.mainloop()
