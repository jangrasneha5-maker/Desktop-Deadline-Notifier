import time
import os
from plyer import notification
from PIL import Image

ICON_PATH = "notifier_icon.ico"

def create_icon():
    if not os.path.exists(ICON_PATH):
        img = Image.new('RGB', (64, 64), color=(0, 120, 215))
        img.save(ICON_PATH)

def start_notifier():
    create_icon()
    
    while True:
        print("\n--- Task Configuration ---")
        title = input("Task Name: ")
        msg = input("Task Details: ")
        
        # Choice for time unit
        print("\nChoose time unit:")
        print("1. Hours (h)")
        print("2. Minutes (m)")
        print("3. Seconds (s)")
        unit = input("Enter choice (h/m/s): ").lower()
        
        try:
            duration = float(input(f"Enter the number of {unit}: "))
            
            # Conversion Logic
            if unit == 'h' or unit == '1':
                seconds = duration * 3600
            elif unit == 'm' or unit == '2':
                seconds = duration * 60
            else:
                seconds = duration # Default is seconds
                
            print(f"\nTimer set for {duration} {unit}. Waiting...")
            time.sleep(seconds)
            
            notification.notify(
                title=f"REMINDER: {title}",
                message=msg,
                app_name="Custom Notifier",
                app_icon=ICON_PATH if os.path.exists(ICON_PATH) else None,
                timeout=10
            )
            print("Notification Sent!")
            
        except ValueError:
            print("Error: Please enter a valid number for time.")

        if input("\nSet another task? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    start_notifier()