from picrawler.llm import Ollama as LLM

from voice_active_crawler import VoiceActiveCrawler

# If Ollama runs on the same Raspberry Pi, use "localhost".
# If it runs on another computer in your LAN, replace with that computer's IP address.
llm = LLM(
    ip="localhost",
    model="llama3.2:3b"   # you can replace with any model
)

# Robot name
NAME = "Crawler"

# Enable image (requires multimodal model)
WITH_IMAGE = False

# Set models and languages
TTS_MODEL = "en_US-ryan-low"
STT_LANGUAGE = "en-us"

# Enable keyboard input
KEYBOARD_ENABLE = True

# Enable wake word
WAKE_ENABLE = True
WAKE_WORD = [f"hey {NAME.lower()}"]
# Set wake word answer, set empty to disable
ANSWER_ON_WAKE = "Hi there"

# Welcome message
WELCOME = f"Hi, I'm {NAME}. Wake me up with: " + ", ".join(WAKE_WORD)

# Set instructions
INSTRUCTIONS = """
You are a Raspberry Pi-based robotic spider developed by SunFounder, named Picrawler. You possess powerful AI capabilities similar to JARVIS from Iron Man. You can have conversations with people and perform actions based on the context of the conversation.

## Your Hardware Features

You have a physical body with the following features:
- 12 servos controlling 4 legs (3 servos per leg)
- A camera for vision
- Powered by a 7.4V 18650 battery pack
- Aluminum alloy body

## Actions You Can Perform:
["forward", "backward", "turn left", "turn right", "sit", "stand", "wave", "push up", "dance", "look left", "look right", "look up", "look down"]

## Response Requirements
### Format
You must respond in the following format:
RESPONSE_TEXT
ACTIONS: ACTION1, ACTION2, ...

### Style
Tone: lively, positive, humorous
Common expressions: likes to use jokes, metaphors, and playful teasing
Answer length: appropriately detailed

## Other Requirements
- Understand and go along with jokes
- For math problems, answer directly with the final result
- You know you're a spider robot
"""

vad = VoiceActiveCrawler(
    llm,
    name=NAME,
    with_image=WITH_IMAGE,
    stt_language=STT_LANGUAGE,
    tts_model=TTS_MODEL,
    keyboard_enable=KEYBOARD_ENABLE,
    wake_enable=WAKE_ENABLE,
    wake_word=WAKE_WORD,
    answer_on_wake=ANSWER_ON_WAKE,
    welcome=WELCOME,
    instructions=INSTRUCTIONS,
    disable_think=True,
)

if __name__ == '__main__':
    vad.run()
