# Project Prompt Exporter

A simple and efficient tool to convert the entire structure and content of a project into a single text (`.txt`) file. This utility is specifically designed for developers who want to feed their entire project codebase as a single, comprehensive prompt to Large Language Models (LLMs) like GPT-4, Gemini, Claude, etc., to facilitate code analysis, review, or development.

[![Mehdi Shekari GitHub](https://img.shields.io/badge/GitHub-MehdiShekari-blue?style=flat-square&logo=github)](https://github.com/MehdiShekari)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## ✨ Features

* **Graphical User Interface (GUI):** Features a clean and elegant UI built with `Tkinter` that displays the live progress of the export process.
* **Automatic Path Detection:** The script intelligently scans the directory from which it is executed.
* **Tree-like Structure:** Displays the project's folder and file structure in a readable, indented tree format.
* **File Content Extraction:** Reads the content of all text-based files and appends them to the output file.
* **Binary File Exclusion:** Automatically ignores non-text files such as images (`.png`, `.jpg`), fonts (`.ttf`, `.woff`), and multimedia files to keep the output clean and relevant.
* **Single, Organized Output:** All information is saved into a single `.txt` file, timestamped for easy identification.

## 🖼️ Output Sample

When you run the application in a sample project, the output file will look like this:

```text
=== Project Folder Structure ===

my_project:
--------src:
----------------main.py
----------------utils.py
--------tests:
----------------test_main.py
--------.gitignore
--------README.md

=== File Contents ===

--- src\main.py ---

import tkinter as tk

def main():
    root = tk.Tk()
    root.title("My App")
    root.mainloop()

if __name__ == "__main__":
    main()

--- src\utils.py ---

def helper_function():
    return "Hello, World!"

--- tests\test_main.py ---

import unittest
from src.utils import helper_function

class TestUtils(unittest.TestCase):
    def test_helper(self):
        self.assertEqual(helper_function(), "Hello, World!")

--- .gitignore ---

__pycache__/
*.pyc

--- README.md ---

# My Awesome Project
This is a sample project.
```

## 🚀 How to Run

There are two ways to run this tool:

### 1. Using the Executable (`.exe`) - Recommended Method

This is the easiest way for Windows users, as it does not require Python or any dependencies to be installed.

1.  **Download:** Navigate to the [**Releases**](https://github.com/MehdiShekari/prompt-generator-for-ai/releases) page of the GitHub repository.
2.  **Get the File:** Download the latest version, which will be a `.zip` file.
3.  **Extract:** Unzip the downloaded file.
4.  **Copy:** Place the `main.exe` file into the **root directory** of the project you want to export.
5.  **Run:** Double-click the `.exe` file. The application window will open, and the scanning process will begin automatically.
6.  **Result:** Once finished, a new file named `project_prompt_YYYY-MM-DD_HH-MM-SS.txt` will be created in the same directory.

### 2. Running from Source (`.py`)

If you have Python installed, you can run the script directly.

1.  **Prerequisite:** Ensure you have Python 3 installed on your system.
2.  **Run the Script:** Open your terminal or Command Prompt in the project's root directory and run the following command:
    ```bash
    python main.py
    ```
    > **Note:** This script only uses standard Python libraries (`os`, `sys`, `tkinter`) and does not require any external packages to be installed.

## 🛠️ How to Build (Patch) the `.exe` File

If you have made changes to the source code and want to build your own `.exe` file, follow these steps:

1.  **Install PyInstaller:** This library is used to convert Python scripts into standalone executables. If you don't have it, install it using pip:
    ```bash
    pip install pyinstaller
    ```
2.  **Prepare the Icon:** Place an icon file with the `.ico` format (e.g., `icon.ico`) in the same directory as your Python script.
3.  **Build the Executable:** Open your terminal in the project directory and run the following command (assuming your script is named `main.py`):
    ```bash
    pyinstaller --onefile --windowed --icon=icon.ico --add-data "icon.ico;." main.py
    ```
    * `--onefile`: Bundles everything into a single executable file.
    * `--windowed` or `-w`: Prevents the black console window from appearing in the background, showing only the GUI.
    * `--icon="icon.ico"`: Sets your custom icon for the executable.

4.  **Find the Output:** After the command finishes, a `dist` folder will be created. Your final `.exe` file will be inside this folder.

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvement or encounter any issues, please open an [Issue](https://github.com/MehdiShekari/prompt-generator-for-ai/issues) or submit a [Pull Request](https://github.com/MehdiShekari/prompt-generator-for-ai/pulls).

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
