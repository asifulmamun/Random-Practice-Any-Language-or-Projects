import pyautogui
import random
import time
import threading
import tkinter as tk
from tkinter import messagebox
from messages import text_list
from command import conditions

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
    start_delay = conditions['start_delay']
    iteration_delay = conditions['iteration_delay']
    message_delay = conditions['message_delay']
    msg_count = conditions['msg_count']
    msg_type_system = conditions['msg_type_system']
    msg_type_system_delay = conditions['msg_type_system_delay']

    show_start_delay_message(start_delay)
    time.sleep(start_delay)

    stop_flag = threading.Event()
    mouse_thread = threading.Thread(target=check_mouse_movement, args=(stop_flag,))
    mouse_thread.start()

    for i in range(1, msg_count + 1):
        if stop_flag.is_set():
            break

        random_text = random.choice(text_list)

        pyautogui.typewrite(random_text)
        pyautogui.press('enter')
        
        if msg_type_system == 'random':
            time.sleep(random.uniform(0.1, msg_type_system_delay))
        elif msg_type_system == 'state':
            time.sleep(message_delay)

        if i % iteration_delay == 0 and i != msg_count:
            print(f"\nPausing for {msg_type_system_delay} seconds (Iteration: {i})...")


    stop_flag.set()
    mouse_thread.join()

if __name__ == "__main__":
    main()
