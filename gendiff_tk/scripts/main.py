import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from gendiff_tk.gendiff import gendiff
import os


class DiffApp:
    def __init__(self, root, width=750, height=700):
        self.root = root
        self.root.title('MyDiffTXT')
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(True, True)

        self.file1 = None
        self.file2 = None

        self.create_widgets()

    def create_widgets(self):
        # Create frames
        self.top_frame = tk.Frame(self.root)
        self.top_frame.pack(pady=10)

        self.middle_frame = tk.Frame(self.root)
        self.middle_frame.pack(pady=10)

        self.bottom_frame = tk.Frame(self.root)
        self.bottom_frame.pack(pady=10, fill='both', expand=True)

        # Instruction label
        self.instruction_label = tk.Label(
            self.top_frame,
            text="Выберите два файла формата .txt для сравнения.")

        self.instruction_label.pack()

        # File selection buttons
        self.button1 = tk.Button(self.middle_frame,
                                 text="Открыть первый файл",
                                 command=self.load_file1)
        self.button1.grid(row=0, column=0, padx=10)

        self.button2 = tk.Button(self.middle_frame,
                                 text="Открыть второй файл",
                                 command=self.load_file2)
        self.button2.grid(row=0, column=1, padx=10)

        # File path status labels
        self.file1_label = tk.Label(self.middle_frame,
                                    text="Файл 1: Не выбран",
                                    anchor='w')
        self.file1_label.grid(row=1, column=0, pady=10)

        self.file2_label = tk.Label(self.middle_frame,
                                    text="Файл 2: Не выбран",
                                    anchor='w')
        self.file2_label.grid(row=1, column=1, pady=10)

        self.result_text = ScrolledText(self.bottom_frame, height=20,
                                        width=85, wrap='word')
        self.result_text.pack(pady=10, fill='both', expand=True)

        self.quit_button = tk.Button(self.root,
                                     text="Выход",
                                     command=self.exit_app)
        self.quit_button.pack(side='bottom', pady=10)

    def load_file1(self):
        file_path = self.open_file_dialog("Выберите первый файл")
        if file_path:
            self.file1 = file_path
            self.update_status(self.file1_label, "Файл 1: Загружен")
            self.update_diff()

    def load_file2(self):
        file_path = self.open_file_dialog("Выберите второй файл")
        if file_path:
            self.file2 = file_path
            self.update_status(self.file2_label, "Файл 2: Загружен")
            self.update_diff()

    def open_file_dialog(self, title):
        file_path = fd.askopenfilename(title=title,
                                       filetypes=[("TEXT files", "*.txt")])
        if not file_path:
            mb.showwarning("Ошибка", "Вы не выбрали файл.")
        return file_path

    def update_status(self, label, text):
        label.config(text=text)

    def update_diff(self):
        if self.file1 and self.file2:
            try:
                result_diff = gendiff(self.file1, self.file2)
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, result_diff)
            except Exception as e:
                mb.showerror("Ошибка", f"Не удалось сравнить файлы: {str(e)}")

    def exit_app(self):
        if mb.askyesno("Выход", "Может останетесь?"):
            self.root.destroy()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    if os.environ.get('DISPLAY', '') == '':
        print('no display found. Using :0.0')
        os.environ.__setitem__('DISPLAY', ':0.0')
    root = tk.Tk()
    app = DiffApp(root)
    app.run()
