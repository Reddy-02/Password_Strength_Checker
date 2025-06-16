import tkinter as tk
from tkinter import ttk, messagebox
import re
import os
import pyperclip
from PIL import Image, ImageTk

# -------------------------------
# Password strength checker (regex-based)
# -------------------------------
def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Include numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Include special characters (!@#$...).")

    if score >= 6:
        return "Strong", "#4CAF50", [] # Green
    elif score >= 4:
        return "Medium", "#FF9800", suggestions # Orange
    else:
        return "Weak", "#F44336", suggestions # Red

# -------------------------------
# GUI Functions
# -------------------------------
def evaluate():
    pwd = password_entry.get()
    if pwd == "Enter your password..." or not pwd: # Check if it's the placeholder or truly empty
        status_label.config(text="Too short", fg="#F44336") # Reset status label to 'Too short' and red
        suggestion_text.config(state="normal")
        suggestion_text.delete("1.0", tk.END)
        suggestion_text.insert(tk.END, "")
        suggestion_text.config(state="disabled")
        return

    strength, color, suggestions = check_password_strength(pwd)
    status_label.config(text=f"Strength: {strength}", fg=color)

    suggestion_text.config(state="normal")
    suggestion_text.delete("1.0", tk.END)
    if suggestions:
        for tip in suggestions:
            suggestion_text.insert(tk.END, f"- {tip}\n")
    else:
        suggestion_text.insert(tk.END, "Great password! No suggestions.")
    suggestion_text.config(state="disabled")

def toggle_password():
    if show_password_var.get():
        password_entry.config(show="")
        eye_button.config(image=eye_open_icon)
    else:
        password_entry.config(show="*")
        eye_button.config(image=eye_closed_icon)

def copy_password():
    pwd = password_entry.get()
    if pwd == "Enter your password..." or not pwd:
        messagebox.showwarning("Empty Password", "There is no password to copy.")
    else:
        pyperclip.copy(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

def clear_fields():
    password_entry.delete(0, tk.END)
    password_entry.config(fg="black", show="*") # Ensure it's ready for input, showing '*'
    show_password_var.set(False) # Reset eye button to closed
    eye_button.config(image=eye_closed_icon) # Update eye icon visually

    status_label.config(text="Enter your password...", fg="#333") # Reset status label
    suggestion_text.config(state="normal")
    suggestion_text.delete("1.0", tk.END)
    suggestion_text.config(state="disabled")
    # Set focus away from the entry to trigger the placeholder if empty
    root.focus_set()


# Placeholder text for the entry
PLACEHOLDER_TEXT = "Enter your password..."

def on_password_entry_click(event):
    if password_entry.get() == PLACEHOLDER_TEXT:
        password_entry.delete(0, tk.END)
        password_entry.config(fg="black", show="*") # Change color and show '*'
        show_password_var.set(False) # Ensure eye button is closed when user starts typing

def on_password_entry_leave(event):
    # Only show placeholder if the entry is actually empty
    if not password_entry.get():
        password_entry.insert(0, PLACEHOLDER_TEXT)
        password_entry.config(fg="grey", show="") # Show placeholder without '*'
        show_password_var.set(False) # Ensure eye button is closed when placeholder is active


# -------------------------------
# GUI Layout
# -------------------------------
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x550") # Slightly increased height for better spacing
root.resizable(False, False)
root.config(bg="#f0f0f0") # Light grey background for the root window

# Main Frame (for consistent padding and background)
main_frame = tk.Frame(root, bg="white", padx=20, pady=20, relief="flat", bd=0)
main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15) # Pad the frame inside the root

# --- Title Section ---
# Try to load the shield icon
base_path = os.path.dirname(__file__)
shield_icon_path = os.path.join(base_path, "shield_lock.png") # Assuming you have this file
shield_icon = None
try:
    shield_icon = ImageTk.PhotoImage(Image.open(shield_icon_path).resize((50, 50)))
    icon_label = tk.Label(main_frame, image=shield_icon, bg="white")
    icon_label.pack(pady=(10, 5))
except FileNotFoundError:
    # Fallback if icon is not found
    print("Warning: 'shield_lock.png' not found. Using text-based icon.")
    icon_label = tk.Label(main_frame, text="🔒", font=("Segoe UI Symbol", 30), bg="white", fg="#007BFF") # Unicode lock
    icon_label.pack(pady=(10, 5))


title_label = tk.Label(main_frame, text="Password Strength Checker", font=("Segoe UI", 16, "bold"), bg="white", fg="#333")
title_label.pack(pady=(0, 20))

# --- Password Entry Section ---
password_label = tk.Label(main_frame, text="Password:", font=("Segoe UI", 12), bg="white", fg="#555")
password_label.pack(anchor="w", pady=(10, 0))

password_entry_frame = tk.Frame(main_frame, bg="white")
password_entry_frame.pack(fill="x", pady=5)

password_entry = tk.Entry(password_entry_frame, font=("Segoe UI", 12), show="", relief="solid", bd=1, highlightbackground="#ccc", highlightcolor="#007BFF", highlightthickness=1)
password_entry.pack(side="left", fill="x", expand=True, ipady=5) # ipady for internal padding
password_entry.insert(0, PLACEHOLDER_TEXT) # Initial placeholder text
password_entry.config(fg="grey") # Grey out placeholder text

# Bind events for placeholder behavior
password_entry.bind("<FocusIn>", on_password_entry_click)
password_entry.bind("<FocusOut>", on_password_entry_leave)

# Eye toggle icon
eye_closed_path = os.path.join(base_path, "eye_closed.png")
eye_open_path = os.path.join(base_path, "eye_open.png")
eye_closed_icon = None
eye_open_icon = None

try:
    eye_closed_icon = ImageTk.PhotoImage(Image.open(eye_closed_path).resize((24, 24)))
    eye_open_icon = ImageTk.PhotoImage(Image.open(eye_open_path).resize((24, 24)))
except FileNotFoundError:
    messagebox.showerror("Error", "Eye icons (eye_closed.png, eye_open.png) not found. Please ensure they are in the same directory.")
    # Fallback if icons are not found, use text
    eye_closed_icon = ImageTk.PhotoImage(Image.new('RGBA', (24, 24), (255, 255, 255, 0))) # Transparent
    eye_open_icon = ImageTk.PhotoImage(Image.new('RGBA', (24, 24), (255, 255, 255, 0))) # Transparent


show_password_var = tk.BooleanVar(value=False)
eye_button = tk.Checkbutton(password_entry_frame, image=eye_closed_icon, variable=show_password_var, command=toggle_password,
                           bg="white", activebackground="white", bd=0, highlightthickness=0, cursor="hand2")
eye_button.pack(side="right", padx=(5,0))

# --- Status Label (replaces result_label) ---
status_label = tk.Label(main_frame, text="Too short", font=("Segoe UI", 11), bg="white", fg="#F44336", anchor="w") # Initial state as 'Too short' and red
status_label.pack(fill="x", pady=(5, 10))

# --- Buttons ---
button_font = ("Segoe UI", 11, "bold") # Slightly bolder buttons

evaluate_button = tk.Button(main_frame, text="Check Strength", bg="#007BFF", fg="white", font=button_font, command=evaluate,
                           relief="flat", bd=0, activebackground="#0069D9", activeforeground="white", padx=10, pady=8)
evaluate_button.pack(fill="x", pady=5)

copy_button = tk.Button(main_frame, text="Copy Password", bg="#28A745", fg="white", font=button_font, command=copy_password,
                       relief="flat", bd=0, activebackground="#218838", activeforeground="white", padx=10, pady=8)
copy_button.pack(fill="x", pady=5)

clear_button = tk.Button(main_frame, text="Clear", bg="#DC3545", fg="white", font=button_font, command=clear_fields,
                        relief="flat", bd=0, activebackground="#C82333", activeforeground="white", padx=10, pady=8)
clear_button.pack(fill="x", pady=5)

# --- Suggestions Text Box ---
suggestion_text = tk.Text(main_frame, height=5, wrap=tk.WORD, font=("Segoe UI", 10), bd=1, relief="solid", bg="#f8f8f8", fg="#333", highlightbackground="#ccc", highlightcolor="#007BFF")
suggestion_text.pack(fill="x", pady=(10, 0))
suggestion_text.config(state="disabled")

# Start the Tkinter event loop
root.mainloop()
