import pyautogui
import random
import time
import threading
import tkinter as tk
from tkinter import messagebox
from messages import text_list

def show_start_delay_message(duration):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Script Starting", f"The script will start in {duration} seconds.")
    root.destroy()

def show_stop_message():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Script Stopped", "Mouse movement detected. The script has been stopped.")
    root.destroy()

def check_mouse_movement(stop_flag):
    last_position = pyautogui.position()

    while not stop_flag.is_set():
        time.sleep(1)
        current_position = pyautogui.position()

        if current_position != last_position:
            print("Mouse movement detected. Stopping script.")
            show_stop_message()
            stop_flag.set()

        last_position = current_position

def main():
    start_delay = 10  # seconds
    iteration_delay = 100
    message_delay = 0.5  # seconds

    show_start_delay_message(start_delay)
    time.sleep(start_delay)

    stop_flag = threading.Event()
    mouse_thread = threading.Thread(target=check_mouse_movement, args=(stop_flag,))
    mouse_thread.start()

    for i in range(1, 1001):
        if stop_flag.is_set():
            break

        random_text = random.choice(text_list)

        pyautogui.typewrite(random_text)
        pyautogui.press('enter')

        if i % iteration_delay == 0 and i != 1000:
            print(f"\nPausing for 30 seconds (Iteration: {i})...")
            time.sleep(30)

        time.sleep(message_delay)

    stop_flag.set()
    mouse_thread.join()

if __name__ == "__main__":
    main()
