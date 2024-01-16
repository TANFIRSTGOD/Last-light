from renderMap import RenderMaps
import time
import os
import platform

inGame = True

while inGame:
    print(RenderMaps().render_current_map())
    if input(">>") == "quit()":
        inGame = False
    else:
        operatingSys = platform.system()
        match operatingSys:
            case "Windows":
                print("Windows")