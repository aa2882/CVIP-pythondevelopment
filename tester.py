import tkinter as tk
import random
import time

class TypingSpeedTester:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Tester")

        self.random_text = ""
        self.word_list = ["agra", "bareilly", "chennai", "delhi", "ernakulam", "faridabad", "goa", "haldia", "karnataka",
                          "ladakh", "manipur", "orrisa", "pune", "queula", "ranchi", "shillong", "telangana",
                          "wayanad"]

        self.root.configure(bg="teal")  # Set background color to teal

        self.word_label = tk.Label(root, text=self.random_text, font=("Arial", 18), bg="teal", fg="white")
        self.word_label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Arial", 16))
        self.entry.pack(pady=10)

        self.start_button = tk.Button(root, text="Start", font=("Arial", 16), command=self.start_typing_test, bg="teal", fg="white", highlightbackground="teal")
        self.start_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.stop_button = tk.Button(root, text="Stop", font=("Arial", 16), command=self.stop_typing_test, bg="red", fg="white", highlightbackground="red", state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.reset_button = tk.Button(root, text="Reset", font=("Arial", 16), command=self.reset_typing_test, bg="orange", fg="white", highlightbackground="orange", state=tk.DISABLED)
        self.reset_button.pack(side=tk.RIGHT, padx=10, pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 16), bg="teal", fg="white")
        self.result_label.pack(pady=20)

        self.start_time = None

    def start_typing_test(self):
        if not self.start_time:
            self.random_text = " ".join(random.sample(self.word_list, 10))
            self.word_label.config(text=self.random_text)
            self.start_time = time.time()
            self.start_button.config(text="Submit", bg="red", fg="white", highlightbackground="red")
            self.stop_button.config(state=tk.NORMAL)
            self.reset_button.config(state=tk.NORMAL)
        else:
            typed_text = self.entry.get()
            elapsed_time = time.time() - self.start_time
            words = typed_text.split()
            correct_words = sum(1 for word1, word2 in zip(words, self.random_text.split()) if word1 == word2)
            wpm = int(correct_words / (elapsed_time / 60))
            self.result_label.config(text=f"Your typing speed is {wpm} WPM")
            self.start_button.config(text="Start", bg="teal", fg="white", highlightbackground="teal")
            self.stop_button.config(state=tk.DISABLED)
            self.reset_button.config(state=tk.NORMAL)
            self.start_time = None
            self.entry.delete(0, "end")

    def stop_typing_test(self):
        self.start_time = None
        self.start_button.config(text="Start", bg="teal", fg="white", highlightbackground="teal")
        self.stop_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.NORMAL)
        self.entry.delete(0, "end")

    def reset_typing_test(self):
        self.start_time = None
        self.random_text = ""
        self.word_label.config(text=self.random_text)
        self.entry.delete(0, "end")
        self.start_button.config(text="Start", bg="teal", fg="white", highlightbackground="teal")
        self.stop_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTester(root)
    root.mainloop()
