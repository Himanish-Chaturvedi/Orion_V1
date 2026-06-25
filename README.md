# Orion_V1
Python-based voice assistant with wake-word activation, speech recognition, text-to-speech, news fetching, music playback, browser automation, and Gemini-powered AI responses.

# Orion – Python Voice Assistant

Orion is a **Python-based voice assistant** built as the capstone project of my Python learning phase. It combines **speech recognition, text-to-speech, browser automation, news fetching, music playback, and Gemini-powered AI responses** into a single assistant workflow.

The assistant listens for a wake word (**“Orion”**), processes voice commands, and performs tasks such as opening websites, playing songs from a custom music library, fetching news headlines, and answering general queries using Gemini API integration.

This project was built to move beyond tutorial-based learning and gain hands-on experience with **Python libraries, APIs, debugging, command processing, and real-world project integration**.

---

## Features

* **Wake-word based activation** using **“Orion”**
* **Speech recognition** for voice command input
* **Text-to-speech responses**
* Open websites such as **Google** and **YouTube**
* Play songs from a custom music library
* Fetch and read out **news headlines**
* Answer general queries using **Gemini API**
* Modular command handling through a `process_command()` workflow

---

## Tech Stack

* **Python**
* `speech_recognition`
* `gTTS`
* `pygame`
* `requests`
* `webbrowser`
* **Gemini API**

---

## Project Structure

```bash
Orion/
│── main.py              # Main Orion assistant script
│── musiclib.py          # Stores song names and links for music playback
│── README.md            # Project documentation
│── requirements.txt     # Python dependencies (optional but recommended)
```

> File names can be adjusted depending on how you organize the repo.

---

## How Orion Works

1. Orion starts and greets the user.
2. It listens for the wake word: **“Orion”**
3. Once the wake word is detected, Orion waits for the next command.
4. The command is passed to the `process_command()` function.
5. Depending on the command, Orion can:

   * open a website
   * play music
   * fetch news
   * answer a question using Gemini AI
6. Orion responds using text-to-speech.

---

## Supported Commands

Some example commands Orion can currently handle:

* **“Orion”** → activates the assistant
* **“open google”**
* **“open youtube”**
* **“play [song name]”**
* **“news”** / **“open news”**
* **general questions** like:

  * “Who is Virat Kohli?”
  * “What is machine learning?”
  * “Tell me about artificial intelligence”

---

## Installation & Setup

### 1) Clone the repository

```bash
git clone https://github.com/your-username/orion-voice-assistant.git
cd orion-voice-assistant
```

### 2) Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it:

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file yet, install the libraries manually:

```bash
pip install SpeechRecognition gTTS pygame requests google-genai pyttsx3
```

> Depending on your setup, you may also need **PyAudio** for microphone input with `speech_recognition`.

---

## API Setup

Orion currently uses:

* **Gemini API** for AI-powered responses
* **News API** for fetching headlines

### Gemini API

Create an API key from Google AI Studio and use it in your code.

### News API

Generate a News API key and place it in the `news_api` URL or store it securely as an environment variable.


## Example Workflow

### Wake Orion

```text
Orion
```

### Give a command

```text
open google
```

Or:

```text
play song (according to the musiclib)
```

Or:

```text
who is virat kohli
```

---

## What I Learned Through This Project

Building Orion helped me move beyond beginner Python syntax and work on a project involving:

* **speech recognition and voice-command flow**
* **text-to-speech systems**
* **API integration**
* **debugging package / environment issues**
* **command routing and control flow**
* **working with external libraries**
* **handling real project errors instead of only tutorial examples**

This project was one of the most valuable parts of my Python learning journey because it forced me to solve practical problems and integrate multiple components into one working application.

---

## Current Limitations

Some areas that can still be improved:

* Better wake-word handling
* More robust command parsing
* Support for additional websites / commands
* Improved AI response handling
* Better error handling for network/API failures
* Smarter music library management
* Cleaner project structure with separate modules for commands, AI, and speech

---

## Future Improvements

Planned or possible improvements for Orion:

* Add more commands (time, weather, reminders, etc.)
* Improve natural language understanding
* Add a GUI / desktop interface
* Store chat history
* Add support for multiple AI models
* Use environment variables for secrets and API keys
* Refactor the code into a more scalable structure
* Improve speech output and latency

--

Author

**Himanish Chaturvedi**
B.Tech Artificial Intelligence & Machine Learning student
Interested in software development, AI/ML, and building practical projects through hands-on learning.

--

Feedback

If you have suggestions for improving Orion — whether it’s architecture, features, code quality, or new ideas, feel free to share them. I’d genuinely appreciate feedback and would love to keep improving the project.
