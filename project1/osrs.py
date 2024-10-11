import subprocess
import tkinter as tk
from tkinter import messagebox
import sys


def launch_osrs_mobile():
    mobile_protocol_command = "open osrs://launch" # Mac

    try:
        print("Attempting to launch mobile OSRS with command:", mobile_protocol_command)
        result = subprocess.run(mobile_protocol_command, shell=True)

        if result.returncode != 0:
            messagebox.showerror("Error", f"Failed to launch mobile OSRS. Return code: {result.returncode}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to launch mobile OSRS: {e}")


def create_launcher():
    root = tk.Tk()
    root.title("OSRS Launcher")

    mobile_button = tk.Button(root, text="Launch Mobile OSRS", command=launch_osrs_mobile)
    mobile_button.pack(pady=20)

    exit_button = tk.Button(root, text="Exit", command=sys.exit)
    exit_button.pack(pady=10)

    root.geometry("300x150")  # Set window size
    root.mainloop()


if __name__ == "__main__":
    create_launcher()
