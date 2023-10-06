import pyshorteners
import tkinter as tk
from tkinter import messagebox
import webbrowser

shortened_url = None  # To store the shortened URL

def shorten_url():
    global shortened_url
    url = url_entry.get()
    if url:
        try:
            s = pyshorteners.Shortener()
            shortened_url = s.tinyurl.short(url)
            result_label.config(text=f"Shortened URL: {shortened_url}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to shorten the URL. Reason: {e}")

def open_shortened_url():
    global shortened_url
    if shortened_url:
        webbrowser.open(shortened_url)
    else:
        messagebox.showinfo("Info", "Please shorten a URL first.")

app = tk.Tk()
app.title("URL Shortener")

url_label = tk.Label(app, text="Enter Long URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(app, width=50)
url_entry.pack(pady=10)

shorten_button = tk.Button(app, text="Shorten", command=shorten_url)
shorten_button.pack(pady=5)

open_link_button = tk.Button(app, text="Open Shortened Link", command=open_shortened_url)
open_link_button.pack(pady=5)

result_label = tk.Label(app, text="")
result_label.pack(pady=10)

app.mainloop()
