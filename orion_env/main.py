import time
from google import genai
import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclib
import requests
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()
ttsx = pyttsx3.init()

news_api = "apikey"

ttsx.setProperty('volume', 1.0)


def speak_old(text):
    ttsx.say(text)
    ttsx.runAndWait()
    
def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 
    
    

def aiProcess(command):
   try:
    client = genai.Client(api_key="Apikey")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
        You are a virtual assistant named Orion skilled in general tasks like Alexa and Google Assistant.
        Give responses precisely and relevant to the query.

        User Query: {command}
        """
    )
    
    print("Gemini Response:", response.text)

    return response.text

    except Exception as e:
        print("Gemini Error:", e)
        return "Sorry, the AI service is unavailable right now."


def process_command(command):

    print("Inside process_command:", repr(command))
    
    if "open youtube" in command:
        speak("Opening YouTube")
        time.sleep(1)
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        time.sleep(1)
        webbrowser.open("https://www.google.com")

    elif "exit" in command:
        speak("Goodbye!")
        exit()

    elif command.startswith("play"):

        try:
            song = command.split(" ", 1)[1]

            if song in musiclib.music:
                speak(f"Playing {song}")
                webbrowser.open(musiclib.music[song])

            else:
                speak("Sorry, I don't have that song.")

        except IndexError:
            speak("Please tell me which song to play.")

    elif "news" in command:

     print("NEWS BLOCK ENTERED")

     speak("Fetching today's news")

     print("Making request...")

     r = requests.get(news_api)

     print("Status Code:", r.status_code)

     if r.status_code == 200:

        print("Request successful")

        data = r.json()

        articles = data.get('articles', [])

        print("Articles found:", len(articles))

        if len(articles) == 0:
            speak("No news articles were found.")

        else:
            for article in articles[:5]:
                print(article['title'])
                speak(article['title'])
                
    elif command.startswith("ask"):

     query = command.split(" ", 1)[1]

     speak("Thinking...")

     response = aiProcess(query)

     print(response)

     speak(response)
    
    else:
        # Let OpenAI handle the request
        output = aiProcess(command)
        speak(output) 
    
        
    


if __name__ == "__main__":

    speak("Orion is now online. How can I assist you?")

    while True:

        try:

            with sr.Microphone() as source:

                print("Listening...")

                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=5
                )

            command = recognizer.recognize_google(audio).lower()

            print(f"You said: {command}")

            if command == "orion":

                print("Wake word detected")

                speak("I am listening")

                with sr.Microphone() as source:

                    print("Waiting for command...")

                    audio = recognizer.listen(
                        source,
                        timeout=5,
                        phrase_time_limit=5
                    )

                command = recognizer.recognize_google(audio).lower()

                print(f"Command: {command}")
                
                print("Calling process_command")
                process_command(command)
                print("Returned from process_command")

                

        except sr.UnknownValueError:

            speak("Sorry, I couldn't understand what you said. Please try again.")

        except sr.RequestError as e:

            speak(f"Could not request results: {e}")

        except Exception as e:

            print("Error:", e)