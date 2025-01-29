import tkinter as tk
from tkinter import messagebox, ttk
import re
import requests
import hashlib

class PasswordGuardian:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Password Guardian")
        self.root.geometry("400x300")
        
        self.setup_ui()
        
    def setup_ui(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(main_frame, text="Enter a password to check:").pack(pady=10)
        
        self.password_entry = ttk.Entry(main_frame, show="*")
        self.password_entry.pack(pady=10, fill=tk.X)
        self.password_entry.bind('<Return>', self.on_check_password)
        
        self.show_password_var = tk.BooleanVar()
        ttk.Checkbutton(
            main_frame, 
            text="Show Password",
            variable=self.show_password_var,
            command=self.toggle_password_visibility
        ).pack(pady=5)
        
        ttk.Button(
            main_frame,
            text="Check Password",
            command=self.on_check_password
        ).pack(pady=20)

    def check_password_strength(self, password):
        if len(password) < 8:
            return "Weak: Password must be at least 8 characters long."
        if not re.search(r"\d", password):
            return "Weak: Password must contain at least one number."
        if not re.search(r"[A-Z]", password):
            return "Weak: Password must contain at least one uppercase letter."
        if not re.search(r"[a-z]", password):
            return "Weak: Password must contain at least one lowercase letter."
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return "Weak: Password must contain at least one special character."
        return "Strong: Password is strong."

    def check_password_pwned(self, password):
        try:
            sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
            prefix = sha1_password[:5]
            suffix = sha1_password[5:]
            url = f"https://api.pwnedpasswords.com/range/{prefix}"
            
            response = requests.get(url)
            if response.status_code != 200:
                return "Error: Unable to check password against Have I Been Pwned."

            hashes = (line.split(':') for line in response.text.splitlines())
            for h, count in hashes:
                if h == suffix:
                    return f"Warning: This password has been seen {count} times before."

            return "Safe: This password has not been found in any known data breaches."
        except requests.RequestException:
            return "Error: Unable to check password. Please check your internet connection."

    def on_check_password(self, event=None):
        password = self.password_entry.get()
        strength = self.check_password_strength(password)
        
        if "Weak" in strength:
            messagebox.showwarning("Password Check Result", strength)
        else:
            pwned_status = self.check_password_pwned(password)
            result = f"{strength}\n{pwned_status}"
            messagebox.showinfo("Password Check Result", result)

    def toggle_password_visibility(self):
        if self.show_password_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = PasswordGuardian()
    app.run()
