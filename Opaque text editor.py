#hello
#I am bored so here's a text editor with opaque background cause why not

import tkinter as tk

def set_opacity(window, opacity):
    window.attributes('-alpha', opacity)

def main():
    root = tk.Tk()
    root.title("Basic text editor")
    
    set_opacity(root, 0.8)

    text_editor = tk.Text(root, wrap=tk.WORD)
    text_editor.pack(fill=tk.BOTH, expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()
