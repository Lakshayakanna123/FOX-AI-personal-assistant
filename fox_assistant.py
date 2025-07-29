import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
import pyttsx3
import os
import pyautogui
import threading
import keyboard
import time
from openai import OpenAI  # ✅ OpenRouter-compatible client

# 🔐 OpenRouter API Setup
client = OpenAI(
    api_key="xxxxxxxxxxxxxxxxxxxxxx",
    base_url="https://openrouter.ai/api/v1"
)

# 🗣️ Text-to-Speech (TTS)
engine = pyttsx3.init()
engine.setProperty('rate', 165)  # More natural pace
engine.setProperty('volume', 1)

# 🔊 Speak with slight pause to feel human
def speak(text):
    log_output(f"Fox: {text}")
    for chunk in text.split('. '):
        engine.say(chunk)
        engine.runAndWait()
        time.sleep(0.3)

# 💬 GPT via OpenRouter
def ask_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        log_output(f"GPT Error: {e}")
        return "Sorry, I couldn't connect to GPT."

# 🎯 Command Handler
gpt_conversation_active = False

def handle_command(command):
    global gpt_conversation_active
    command = command.lower()

    if "open chatgpt" in command:
        speak("Opening ChatGPT")
        os.system("start chrome https://chat.openai.com")

    elif "open gemini" in command:
        speak("Opening Gemini")
        os.system("start chrome https://gemini.google.com")

    elif "open claude" in command:
        speak("Opening Claude")
        os.system("start chrome https://claude.ai")

    elif "open youtube" in command:
        speak("Opening YouTube")
        os.system("start chrome https://youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        os.system("start chrome https://google.com")

    elif "open notes" in command or "take a note" in command:
        speak("Opening Google Keep")
        os.system("start chrome https://keep.google.com")

    elif "open docs" in command:
        speak("Opening Google Docs")
        os.system("start chrome https://docs.google.com")

    elif "open sheets" in command:
        speak("Opening Google Sheets")
        os.system("start chrome https://sheets.google.com")

    elif "open gmail" in command:
        speak("Opening Gmail")
        os.system("start chrome https://mail.google.com")

    elif "open spotify" in command:
        speak("Opening Spotify")
        os.startfile(r"C:\Users\klaks\AppData\Roaming\Spotify\Spotify.exe")  # Update path if needed

    elif "type" in command:
        msg = command.replace("type", "").strip()
        pyautogui.write(msg)

    elif "search" in command:
        query = command.replace("search", "").strip()
        os.system(f"start chrome https://www.google.com/search?q={query}")
        speak(f"Searching for {query}")

    elif "ask gpt" in command:
        gpt_conversation_active = True
        speak("Sure, I’m now connected to GPT. You can start asking your questions.")
        prompt = command.replace("ask gpt", "").strip()
        if prompt:
            response = ask_gpt(prompt)
            speak(response)

    elif gpt_conversation_active:
        if "thank you" in command or "thanks" in command:
            speak("You're welcome. Ending GPT conversation.")
            gpt_conversation_active = False
        else:
            response = ask_gpt(command)
            speak(response)

    elif "shutdown" in command:
        speak("Shutting down. Goodbye!")
        root.quit()

    else:
        speak("I didn't understand that command.")

# 🎧 Speech Recognition
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        log_output("🎤 Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source, phrase_time_limit=6)
    try:
        command = r.recognize_google(audio)
        log_output(f"🗣️ You: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Network error.")
        return ""

def run_fox():
    speak("Fox is online.")
    while listening_flag.get():
        command = listen()
        if "fox" in command:
            command = command.replace("fox", "").strip()
            handle_command(command)

# 🎛️ GUI + Hotkey
def toggle_listening():
    if listening_flag.get():
        listening_flag.set(False)
        toggle_btn.config(text="Start Listening")
        log_output("🛑 Fox stopped listening.")
    else:
        listening_flag.set(True)
        toggle_btn.config(text="Stop Listening")
        log_output("🟢 Fox is now listening...")
        threading.Thread(target=run_fox, daemon=True).start()

def hotkey_listener():
    keyboard.add_hotkey("ctrl+space", toggle_listening)
    keyboard.wait()

def log_output(text):
    output_text.insert(tk.END, text + "\n")
    output_text.see(tk.END)

# 🖼️ GUI Window
root = tk.Tk()
root.title("🦊 Fox AI Assistant")
root.geometry("500x400")
root.configure(bg="#1e1e1e")

listening_flag = tk.BooleanVar(value=False)

title_label = tk.Label(root, text="Fox - Your Personal AI Assistant", font=("Arial", 16), bg="#1e1e1e", fg="#ffffff")
title_label.pack(pady=10)

toggle_btn = tk.Button(root, text="Start Listening", font=("Arial", 12), command=toggle_listening,
                       bg="#00aaff", fg="#ffffff", width=20)
toggle_btn.pack(pady=10)

output_text = scrolledtext.ScrolledText(root, font=("Consolas", 10), bg="#2d2d2d", fg="#00ffcc",
                                        wrap=tk.WORD, height=15)
output_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

log_output("[*] Fox is ready. Click 'Start Listening' or press Ctrl+Space to begin.")

# 🎯 Start global hotkey
threading.Thread(target=hotkey_listener, daemon=True).start()

root.mainloop()
