import tkinter as tk
import time

class DangerousWritingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Dangerous Writing App - 5 seconds before the clear")
        
        self.text_box = tk.Text(self.master, height=10, width=50)
        self.text_box.pack(pady=10)
        
        self.start_time = time.time()
        self.text_box.bind("<Key>", self.reset_timer)
        
        self.check_timer()

    def reset_timer(self, event):
        self.start_time = time.time()

    def check_timer(self):
        current_time = time.time()
        if current_time - self.start_time > 5:
            self.text_box.delete('1.0', tk.END)
            self.start_time = current_time
        self.master.title(f"Dangerous Writing App - Timer: {int(5.4 - (current_time - self.start_time))} seconds")
        self.master.after(1000, self.check_timer)

def main():
    root = tk.Tk()
    app = DangerousWritingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
