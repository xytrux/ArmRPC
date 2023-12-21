# ArmRPC

so uh yeah, i decided to make another rpc client, except now, its tailored to my needs.

## usage

i didnt open source it for no reason. so here ya go:

1. download the bat and the python file
2. run the bat file
3. profit

## tailoring

sooo... you want to tailor it to YOUR needs huh? dont worry, ive got a guide for that too.

1. open the `main.py` file
2. see this chunk of code? you gotta edit this.

```py
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
```

3. to edit it, you gotta learn a bit of python. im too lazy to write a whole guide

## how to modify the values

ok so i decided to actually write a guide...

so you saw that big ahh chunk of code at the top right?

well, lets split it up into more chunks:

### program checks

so as you can see from this terrible code, this basically checks what programs are running, simply change what programs you want to check by looking for their location.

```py
# Check if VSCode or Steam is running
vscode_running = "Code.exe" in (p.name() for p in psutil.process_iter())
steam_running = "steam.exe" in (p.name() for p in psutil.process_iter())

# Get the title of the currently active window
active_window_title = gw.getActiveWindow().title
```
for me, i wanted to check steam and vscode. so here we are.

the bottom is self explanatory (i put a comment there!!!)

### default values

so this is basically just what you want the values to be when you arent running anything but discord.

```py
# Default values for details and state
details = "just chillin'"
state = "state of chillness"
```

just change these to whatever you want.

### checking programs pt. 2

so from this code chunk, it basically updates the details and state based on whether vscode or steam is running

```py
    if vscode_running and "Visual Studio Code" in active_window_title:
        details = "codin' shit"
        state = "state of programming"
    elif steam_running and "Steam" in active_window_title:
        details = "gamin'"
        state = "state of gamin' rage"
    elif vscode_running and steam_running:
        details = active_window_title if active_window_title else "Multitaskin'"
        state = "Multitaskin' on windows"
```

basically, if vscode isnt running, check if steam is, if both are, say you're multitasking.

simply edit these values to say what you want for each program.

### image and buttons

so basically, now you gotta change yo images.

if you havent already, make your app in the discord developer portal, i have made a guide for this already and i am NOT doing it again.

```py
RPC.update(
        large_image = "armature",
        large_text = "Follow me on GitHub",
        small_image = "verified",
        small_text = "Verified Developer",
        details = details,
        state = state,
        start = start,
        buttons = [{"label": "GitHub", "url": "https://github.com/armature64"}]
    )
```

so here, you basically wanna change your small and large images to the name of the art asset you want to use.

as for the text, thats just whatever you want it to say when hovered over the images.

for the buttons, you can add up to 2 buttons. I only have 1 because i don't know what other thing to link.

basically, the "label" is just what the button is gonna be, well, labeled. the url is just... the url.

to add another button, just add a comma to the end of the last curly bracket (`}`) and copy paste.

## contributors

me, myself, and i.