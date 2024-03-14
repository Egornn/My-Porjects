import tkinter as tk
import time

class TypingSpeedTestApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Speed Test")
        
        self.sample_text = "The quick brown fox jumps over the lazy dog."
        self.current_text = tk.StringVar()
        self.current_text.set(self.sample_text)
        
        self.start_time = None
        self.end_time = None
        self.elapsed_time = None
        
        self.words_typed = 0
        
        self.setup_ui()

    def setup_ui(self):
        self.text_label = tk.Label(self.master, textvariable=self.current_text, wraplength=400)
        self.text_label.pack(pady=10)
        
        self.entry = tk.Entry(self.master)
        self.entry.pack(pady=5)
        self.entry.focus_set()
        
        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack(pady=10)
        
        self.start_button = tk.Button(self.master, text="Start", command=self.start_test)
        self.start_button.pack(pady=5)
        
        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_test, state=tk.DISABLED)
        self.reset_button.pack(pady=5)
        
    def start_test(self):
        self.start_time = time.time()
        self.entry.bind("<KeyRelease>", self.check_typing)
        self.start_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.NORMAL)
        
    def check_typing(self, event):
        typed_text = self.entry.get()
        if typed_text == self.sample_text:
            self.end_test()
        else:
            self.words_typed = len(typed_text.split())
        
    def end_test(self):
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time
        words_per_minute = int((self.words_typed / self.elapsed_time) * 60)
        self.result_label.config(text=f"Your typing speed: {words_per_minute} words per minute")
        self.entry.unbind("<KeyRelease>")
        self.reset_button.config(state=tk.DISABLED)
        
    def reset_test(self):
        self.sample_text = "The quick brown fox jumps over the lazy dog."
        self.current_text.set(self.sample_text)
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.start_button.config(state=tk.NORMAL)
        self.words_typed = 0

def main():
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
