import tkinter as tk
from tkinter import messagebox
import sqlite3

# Initialize Database
def initialize_database():
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            feedback TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Database insertion function
def submit_feedback():
    name = name_entry.get()
    email = email_entry.get()
    feedback = feedback_text.get("1.0", tk.END)
    if name and email and feedback.strip():
        conn = sqlite3.connect('feedback.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO feedback (name, email, feedback) VALUES (?, ?, ?)", (name, email, feedback))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Feedback submitted!")
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        feedback_text.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

# Password-protected data retrieval
def retrieve_feedback():
    password = input("Enter password to retrieve data: ")
    correct_password = "Coffee247"  # Updated password
    if password == correct_password:
        conn = sqlite3.connect('feedback.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM feedback")
        feedback_entries = cursor.fetchall()
        for entry in feedback_entries:
            print(f"ID: {entry[0]}\nName: {entry[1]}\nEmail: {entry[2]}\nFeedback: {entry[3]}\n{'-'*40}\n")
        conn.close()
    else:
        print("Access denied. Incorrect password.")

# GUI setup
root = tk.Tk()
root.title("Customer Feedback")

# Layout Frames
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Name Field
tk.Label(frame, text="Name:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
name_entry = tk.Entry(frame, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=5)

# Email Field
tk.Label(frame, text="Email:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
email_entry = tk.Entry(frame, width=30)
email_entry.grid(row=1, column=1, padx=5, pady=5)

# Feedback Field
tk.Label(frame, text="Feedback:").grid(row=2, column=0, sticky="ne", padx=5, pady=5)
feedback_text = tk.Text(frame, height=5, width=30)
feedback_text.grid(row=2, column=1, padx=5, pady=5)

# Submit and Retrieve Buttons
submit_button = tk.Button(root, text="Submit", command=submit_feedback)
submit_button.pack(pady=5)

retrieve_button = tk.Button(root, text="Retrieve Feedback (Console)", command=retrieve_feedback)
retrieve_button.pack(pady=5)

# Initialize the database and run the application
initialize_database()
root.mainloop()
