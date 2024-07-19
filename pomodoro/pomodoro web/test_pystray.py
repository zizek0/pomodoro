from PIL import Image
import pystray
from pystray import MenuItem as item

def on_quit(icon, item):
    print("Quitting...")
    icon.stop()

print("Starting...")

# Load an image to use as the tray icon
image = Image.open("D:\GitHub\Pomodoro\pomodoro\pomodoro app\icon.png")
print("Image loaded.")

# Create the tray icon
icon = pystray.Icon('test', image, 'Pystray Test', pystray.Menu(
    item('Quit', on_quit)
))
print("Icon created.")

# Run the icon
icon.run()
print("Icon run.")
