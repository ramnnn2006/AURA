import webbrowser
import os
try:
    import pygame
    import pygame.camera
except:
    os.system(f'cmd /c "pip install pygame"')
    import pygame
    import pygame.camera
try:
    import speech_recognition as sr
except:
    os.system(f'cmd /c "pip install speechrecognition"')
    import speech_recognition as sr
try:
    from pyttsx3 import Engine
except:
    os.system(f'cmd /c "pip install pyttsx3"')
    from pyttsx3 import Engine
try:
    import pyautogui
except:
    os.system(f'cmd /c "pip install pyautogui"')
    import pyautogui
try:
    import pyaudio
except:
    os.system(f'cmd /c "pip install pyaudio"') 
    import pyaudio


def YoutubeSearch(txt):
    try:
        que=f"https://www.youtube.com/results?search_query={txt}"
        webbrowser.open(que)
        return "Top results are displayed on your browser"
    except Exception as e :
        print(f"Could not perform Function with Error Code {e}")
        return f"Could not perform Function with Error Code {e}"
def spotify(txt):
    try:
        url=f'https://open.spotify.com/search/{txt}'
        webbrowser.open(url)
        return "search result has been displayed"
    except Exception as e :
        print(f"Could not perform Function with Error Code {e}")
        return f"Could not perform Function with Error Code {e}"
def cmdpmt():
    os.system('cmd /k "date"') 
def gs(stxt):
    txt='+'.join(stxt.split())
    url=f"https://www.google.com/search?q={txt}&btnK=Google+Search & sca_esv = 584340551 & sxsrf = AM9HkKn5DKm4gJ9l1ljkOoR2s3zlgmY3Bw % 3A1700588748625 & source = hp & ei = zOxcZf69I4f_ptQPsJ6h2Aw & iflsig = AO6bgOgAAAAAZVz63I84HNY - j7T7bGOddo - Mkh2IHr5m"
    ''.join(url)
    webbrowser.open(url)
    return "search result has been displayed"
def take_screenshot(num):
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save(f"screenshot{num}.png")
        return "Screenshot Saved"
    except Exception as e :
        print(f"Could not perform Function with Error Code {e}")
        return f"Could not perform Function with Error Code {e}"
def anime(stxt):
    try:
        txt='+'.join(stxt.split())
        url=f'https://animension.to/search?search_text={txt}'
        webbrowser.open(url)
        return "search result has been displayed"
    except Exception as e :
        print(f"Could not perform Function with Error Code {e}")
        return f"Could not perform Function with Error Code {e}"
def Speak(text):
    engine = Engine()
    engine.say(text)
    engine.runAndWait()
    return
def listen(txt):
    recognizer = sr.Recognizer()
    Speak(txt)
    # Create a microphone object
    with sr.Microphone(device_index=1) as source:
        Speak("Listening")
        audio = recognizer.listen(source)
    # Transcribe the audio into text
    try:
        Speak("Recognizing")
        text = recognizer.recognize_google(audio)
        #print("You said: {}".format(text))
    except:
        text="Not Recognizable"
    return text
def openlist():
    f=open(r"AURA\todo.txt",'r')
    td=f.read()
    td=td.split('\n')
    f.close()
    res = [i for n, i in enumerate(td) if i not in td[:n]]
    return res
def closelist(lst):
    res = [i for n, i in enumerate(lst) if i not in lst[:n]]
    f=open(r'AURA\todo.txt','w')
    for i in res:
        f.write(i+'\n')
    f.close()
    return
def addtodo(task):
    try:
        td=openlist()
        td.insert(0,task)
        closelist(td)
        return f'{task} added to todo list'
    except Exception as e:
        return f'Error code {e}'
def viewtodo():
    try:
        td=openlist()
        Speak("Items from your Todo List")
        for i in td:
            Speak(i)
        closelist(td)
        return 'End of todo list'
    except Exception as e:
        return f'Error code {e}'
def deletetodo(task):
    try:
        td=openlist()
        if task in td:
            td.remove(task)
        closelist(td)
        return f'{task} removed from todo list'
    except Exception as e:
        return f'Error code {e}'
def capture_photo(num):
    # Initialize Pygame
    pygame.init()
    pygame.camera.init()

    # Get a list of available cameras
    cameras = pygame.camera.list_cameras()
    camera = pygame.camera.Camera(cameras[0])
    camera.start()   
    image = camera.get_image()

    pygame.image.save(image,f"CamPic{num}.jpg")

    camera.stop()
    pygame.quit()

    return "Photo has been captured"
