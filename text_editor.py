import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file(window, text_edit, word_count_label):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])
    if not filepath:
        return
    
    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
    window.title(f"Current File: {filepath}")
    update_word_count(text_edit, word_count_label)

def save_file(window, text_edit, word_count_label):
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt")])
    if not filepath:
        return
    
    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    window.title(f"Current File: {filepath}")
    update_word_count(text_edit, word_count_label)

def update_word_count(text_edit, word_count_label):
    content = text_edit.get(1.0, tk.END)
    words = content.split()
    word_count = len(words)
    word_count_label.config(text=f"Word Count: {word_count}")

def main():
    window = tk.Tk()
    window.title("Text Editor")
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=500)
    
    text_edit = tk.Text(window, font="Helvetica 18")
    text_edit.grid(row=0, column=1)
    
    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    save_button = tk.Button(frame, text="Save", command=lambda: save_file(window, text_edit, word_count_label))
    open_button = tk.Button(frame, text="Open", command=lambda: open_file(window, text_edit, word_count_label))
    
    save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_button.grid(row=1, column=0, padx=5, sticky="ew")
    frame.grid(row=0, column=0, sticky="ns")
    
    word_count_label = tk.Label(window, text="Word Count: 0")
    word_count_label.grid(row=1, column=1, padx=10, pady=10)
    
    window.bind("<Control-s>", lambda x: save_file(window, text_edit, word_count_label))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit, word_count_label))
    text_edit.bind("<KeyRelease>", lambda x: update_word_count(text_edit, word_count_label))
    
    window.mainloop()

main()
