import pyautogui
import random
import time
import threading

def check_mouse_movement(stop_flag):
    last_position = pyautogui.position()

    while not stop_flag.is_set():
        time.sleep(1)
        current_position = pyautogui.position()

        if current_position != last_position:
            print("Mouse movement detected. Stopping script.")
            stop_flag.set()

        last_position = current_position

def main():
    text_list = [
        "Hello! 🌟 You're cordially invited to an exclusive event next Friday.",
        "As our VIP guest, your presence will make the evening truly special.",
        "Dress to impress, and get ready for an unforgettable night of celebration and joy.",
        "Can't wait to have you there! 🎉",
        "Join us for an enchanting night filled with music, laughter, and delightful surprises.",
        "Save the date and be prepared to experience a celebration like no other!",
        "An evening of glamour and elegance awaits you. RSVP now for the event of the year.",
        "Prepare for an extraordinary celebration! Your presence will make it even more memorable.",
        "Get ready to dance the night away at the most anticipated event of the season.",
        "Your VIP invitation includes access to an exclusive cocktail hour with our special guests.",
        "Indulge in a gourmet dining experience and savor the flavors of the evening.",
        "Experience the magic of the night with breathtaking performances and entertainment.",
        "As the night unfolds, you'll be surrounded by the company of friends, laughter, and joy.",
        "Don't miss this chance to be part of a truly spectacular event. RSVP today!",
        "We can't wait to welcome you to an evening of opulence and celebration.",
        "Celebrate with us as we create memories that will last a lifetime. Don't miss out!",
        "Experience the allure of the event that everyone will be talking about. RSVP now!",
        "An elegant affair awaits you. Join us for an evening of sophistication and delight.",
        "You're invited to an exclusive soirée that promises to be the highlight of the year.",
        "Toast to a night of joy, laughter, and camaraderie. Your presence is our pleasure.",
        "Get ready for an immersive experience that will leave you in awe. See you there!",
        "The stage is set, the lights are dimmed. Join us for a night of magic and wonder.",
        "Indulge in the extravagance of the evening. Your VIP pass awaits. Don't miss it!",
        "We're thrilled to extend this special invitation to you. Be part of the magic!",
        "Join us for an evening of glitz and glamour. Your presence will make it shine even brighter.",
        "An evening of elegance and charm awaits. RSVP now to secure your place at the event.",
        "Prepare for a night of celebration, laughter, and memories that will last a lifetime.",
        "The countdown to the event of the year has begun. Secure your spot now!",
        "You're invited to be part of a night that promises to be nothing short of extraordinary.",
        "Get ready for a night filled with surprises, laughter, and unforgettable moments."
        # Add more messages as needed
    ]

    start_delay = 10  # seconds
    iteration_delay = 100
    message_delay = 0.5  # seconds

    print(f"Program will start in {start_delay} seconds. Move the mouse to stop the script.")
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


