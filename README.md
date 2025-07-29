🦊 Fox - Your Personal AI Assistant
Fox is a fully-featured AI voice assistant for Windows, equipped with speech-to-text, text-to-speech, and seamless OpenAI API integration via OpenRouter. Powered by a conversational GUI, hotkey control, smart web commands, and more, Fox lets you control your computer, get AI responses, and manage tasks using just your voice.

Features
🎤 Speech Recognition: Activate Fox and issue commands by voice—like "open YouTube," "search," or "type" messages.

🗣️ Text-to-Speech: Fox reads out responses and confirmations with a natural-sounding voice.

🤖 GPT AI Integration: Ask complex questions to OpenAI's GPT-3.5-Turbo (via OpenRouter) and hear the answers spoken back.

🌐 Web Commands: Instantly open ChatGPT, Gemini, Claude, Gmail, Docs, Sheets, YouTube, Google Search, and more.

📝 Typing Automation: Dictate messages, notes, and searches that Fox will type or Google for you.

🕹️ Global Hotkey: Press Ctrl+Space to start or stop listening from anywhere.

🔊 Customizable: Easily update app paths (e.g., Spotify) and tune TTS settings.

Installation
Clone the repository:

bash
git clone https://github.com/your-username/fox-ai-assistant.git
cd fox-ai-assistant
Install dependencies:

bash
pip install tkinter SpeechRecognition pyttsx3 openai pyautogui keyboard
Configure your OpenRouter API key:

Sign up at OpenRouter.ai

Copy your API key.

Replace "xxxxxxxxxxxxxxxxxxxxxx" in the script with your key.

[Optional] Update file paths for local apps (e.g., Spotify) if needed.

Usage
Run python fox.py to launch the GUI.

Click Start Listening or press Ctrl+Space to activate voice control.

Say "Fox" followed by your command:

"Fox, open YouTube"

"Fox, search latest AI news"

"Fox, type Meeting at 4PM"

"Fox, ask gpt Who won the World Cup in 2022?"

Fox will respond by voice, execute your command, and display the interaction in the GUI.

Supported Voice Commands
Command	Action
Open ChatGPT/Gemini/Claude	Launches the web service in Chrome
Open YouTube/Google/Notes/Docs	Opens respective page in browser
Open Gmail/Spotify/Sheets	Opens the app or web page
Search [query]	Google search for your query
Type [message]	Types out your dictated message
Ask GPT [question]	Sends question to GPT and reads reply aloud
Thank you/Thanks	Ends GPT conversation
Shutdown	Quits the app
Notes
Fox uses the default system microphone and Chrome browser.

Hotkey (Ctrl+Space) works globally—start or stop listening from any application.

API usage through OpenRouter may incur costs if quotas are exceeded.

For Spotify and other desktop apps, update the file path if your installation differs.

