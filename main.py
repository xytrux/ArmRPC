from pypresence import Presence 
import time
import psutil
import pygetwindow as gw

start = int(time.time())
client_id = "1187134195017994312" #your application's client id
RPC = Presence(client_id)
RPC.connect()

while True: #infinite loop
    # Check if VSCode, Visual Studio, Pulsar, or Steam is running
    vscode_running = "Code.exe" in (p.name() for p in psutil.process_iter())
    visual_studio_running = "devenv.exe" in (p.name() for p in psutil.process_iter())
    pulsar_running = "Pulsar.exe" in (p.name() for p in psutil.process_iter())
    steam_running = "steam.exe" in (p.name() for p in psutil.process_iter())

    # Get the title of the currently active window
    active_window_title = gw.getActiveWindow().title

    # Default values for details and state
    details = "just chillin'"
    state = "state of chillness"

    # Update details and state based on whether VSCode, Visual Studio, Pulsar, or Steam is running
    if vscode_running and "Visual Studio Code" in active_window_title:
        details = "workin' in vscode"
        state = active_window_title if active_window_title else "state of programming"
    elif visual_studio_running and "Visual Studio" in active_window_title:
        details = "workin' in vs"
        state = active_window_title if active_window_title else "state of programming"
    elif pulsar_running and "Pulsar" in active_window_title:
        details = "workin' in pulsar/atom"
        state = active_window_title if active_window_title else "state of programming"
    elif steam_running and "Steam" in active_window_title:
        details = "gamin'"
        state = "state of gamin' rage"
    elif vscode_running and steam_running:
        details = active_window_title if active_window_title else "workin' a lot"
        state = "chillin' on windows"

    RPC.update(
        large_image = "armature",
        large_text = "Follow me on GitHub",
        small_image = "verified",
        small_text = "Verified Developer",
        details = details,
        state = state,
        start = start,
    )
    time.sleep(30)