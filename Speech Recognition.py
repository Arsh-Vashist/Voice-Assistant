import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # female voice

# Speak function
def speak(audio):
    print("Assistant:", audio)
    engine.say(audio)
    engine.runAndWait()

# Wish user based on time
def wishme():
    hour = datetime.datetime.now().hour
    
    if hour >= 0 and hour < 12:
        speak("Good morning")
        
    elif hour >= 12 and hour < 16:
        speak("Good afternoon")
        
    else:
        speak("Good evening")

# Take voice command
def takecommand():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("\nListening...")
        r.adjust_for_ambient_noise(source)
        
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except:
            print("Listening timeout")
            return ""
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:", query)
        
    except Exception as e:
        print("Recognition error:", e)
        return ""
        
    return query.lower()

# Open website function
def open_website(query):
    
    if "open" in query:
        
        site_name = query.replace("open", "").strip().replace(" ", "")
        
        if site_name == "":
            speak("Please tell the website name")
            return
        
        url = f"https://www.{site_name}.com"
        
        print("Opening:", url)
        
        try:
            webbrowser.open(url)
            speak(f"Opening {site_name}")
            
        except Exception as e:
            print("Browser error:", e)
            speak("Unable to open website")

# Main program
if __name__ == "__main__":
    
    print("Program started")
    
    wishme()
    
    speak("Welcome. How can I help you?")
    
    while True:
        
        query = takecommand()
        
        if query == "":
            continue
        
        print("Command received:", query)
        
        if "open" in query:
            open_website(query)
        
        elif "time" in query:
            time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {time}")
        
        elif "exit" in query or "quit" in query or "stop" in query:
            speak("Goodbye")
            break
        
        else:
            speak("Command not recognized")