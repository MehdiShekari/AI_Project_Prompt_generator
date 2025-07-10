import os
import sys
import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import webbrowser

# Detect base directory (adjusted for PyInstaller .exe or regular .py)
if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define binary file types that should not be opened
BINARY_EXTENSIONS = {
    '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.ico',
    '.ttf', '.woff', '.woff2', '.eot', '.otf', '.svg',
    '.mp3', '.mp4', '.webp', '.exe',
}

def is_binary_file(file_path):
    _, ext = os.path.splitext(file_path)
    return ext.lower() in BINARY_EXTENSIONS

class ProjectExporterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Project Prompt Exporter")

        # Center the window on screen
        window_width = 700
        window_height = 520
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.root.configure(bg="#2e2e2e")  # Elegant dark gray background

        # Set window icon
        icon_path = os.path.join(BASE_DIR, "icon.ico")
        if os.path.exists(icon_path):
            try:
                self.root.iconbitmap(icon_path)
            except Exception as e:
                print(f"Could not set icon: {e}")

        # Create a scrollable console-style text widget
        self.console = scrolledtext.ScrolledText(
            root,
            wrap=tk.WORD,
            font=("Consolas", 10),
            bg="#1e1e1e",
            fg="#ffffff",
            insertbackground="#ffffff"
        )
        self.console.pack(expand=True, fill="both", padx=15, pady=(15, 10))

        # Add GitHub credit label
        self.link_label = tk.Label(
            root,
            text="Written by MehdiShekari (GitHub)",
            fg="#66ccff",
            bg="#2e2e2e",
            cursor="hand2",
            font=("Arial", 10, "underline")
        )
        self.link_label.pack(pady=(0, 10))
        self.link_label.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/MehdiShekari/prompt-generator-for-ai"))

        # Start log and export process
        self.log("Starting export...", "#00ccff")  # cyan
        self.root.after(500, self.run_export)

    def log(self, message, color="#ffffff"):
        """Prints a colored log message to the GUI console."""
        self.console.insert(tk.END, message + "\n")
        self.console.tag_add(color, "end-2l", "end-1l")
        self.console.tag_config(color, foreground=color)
        self.console.see(tk.END)

    def run_export(self):
        """Scans the directory and generates the project structure prompt."""
        base_path = os.getcwd()
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_file = os.path.join(base_path, f"project_prompt_{timestamp}.txt")

        self.log(f"Scanning directory: {base_path}", "#33ff33")  # green

        structure_lines = []
        content_lines = []

        def walk_dir(path, prefix=""):
            for item in sorted(os.listdir(path)):
                item_path = os.path.join(path, item)
                relative_path = os.path.relpath(item_path, base_path)
                if os.path.isdir(item_path):
                    structure_lines.append(f"{prefix}{item}:")
                    walk_dir(item_path, prefix + "--------")
                else:
                    structure_lines.append(f"{prefix}{item}")
                    if is_binary_file(item_path):
                        self.log(f"Skipping binary file: {relative_path}", "#999999")  # gray
                        return
                    content_lines.append(f"\n--- {relative_path} ---\n")
                    try:
                        with open(item_path, "r", encoding="utf-8") as f:
                            content = f.read()
                        content_lines.append(content)
                        self.log(f"Added: {relative_path}", "#ffffff")  # white
                    except Exception as e:
                        content_lines.append(f"[Could not read file: {e}]")
                        self.log(f"Error reading {relative_path}: {e}", "#ff5555")  # red

        structure_lines.append(f"{os.path.basename(base_path)}:")
        walk_dir(base_path)

        with open(output_file, "w", encoding="utf-8") as out:
            out.write("=== Project Folder Structure ===\n\n")
            out.write("\n".join(structure_lines))
            out.write("\n\n=== File Contents ===\n")
            out.write("\n".join(content_lines))

        self.log(f"Export complete! File saved as:\n{output_file}", "#00ccff")  # cyan

if __name__ == "__main__":
    # Change working directory to ensure relative paths are correct
    if hasattr(sys, 'frozen'):
        os.chdir(os.path.dirname(sys.executable))
    else:
        os.chdir(os.getcwd())

    # Start GUI
    root = tk.Tk()
    app = ProjectExporterGUI(root)
    root.mainloop()
