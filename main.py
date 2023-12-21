from pypresence import Presence 
import time
import psutil
import pygetwindow as gw

start = int(time.time())
client_id = "1187134195017994312" #your application's client id
RPC = Presence(client_id)
RPC.connect()

while True: #infinite loop
    # Check if VSCode or Steam is running
    vscode_running = "Code.exe" in (p.name() for p in psutil.process_iter())
    steam_running = "steam.exe" in (p.name() for p in psutil.process_iter())

    # Get the title of the currently active window
    active_window_title = gw.getActiveWindow().title

    # Default values for details and state
    details = "just chillin'"
    state = "state of chillness"

    # Update details and state based on whether VSCode or Steam is running
    if vscode_running and "Visual Studio Code" in active_window_title:
        details = "codin' shit"
        state = "state of programming"
    elif steam_running and "Steam" in active_window_title:
        details = "gamin'"
        state = "state of gamin' rage"
    elif vscode_running and steam_running:
        details = active_window_title if active_window_title else "Multitaskin'"
        state = "Multitaskin' on windows"

    RPC.update(
        large_image = "armature",
        large_text = "Follow me on GitHub",
        details = details,
        state = state,
        start = start,
        buttons = [{"label": "GitHub", "url": "https://github.com/armature64"}]
    )
    time.sleep(15)