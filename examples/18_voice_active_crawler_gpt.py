from picrawler.llm import OpenAI as LLM
from secret import OPENAI_API_KEY as API_KEY

from voice_active_crawler import VoiceActiveCrawler

# ── TTS engines ──────────────────────────────────────────────────────────
# Pick one. The VoiceAssistant accepts any TTS instance via the `tts=` parameter.

# Default: Piper — local neural TTS, offline, fast
from picrawler.tts import Piper
tts = Piper(model="en_US-ryan-low")

# EdgeTTS — free cloud TTS, 100+ voices, no API key
# from picrawler.tts import EdgeTTS
# tts = EdgeTTS(voice="en-US-AriaNeural")

# Espeak — compact offline TTS, robotic, fastest
# from picrawler.tts import Espeak
# tts = Espeak()

# Pico2Wave — compact offline TTS
# from picrawler.tts import Pico2Wave
# tts = Pico2Wave()

llm = LLM(
    api_key=API_KEY,
    model="gpt-4o-mini",
)

# Robot name
NAME = "Buddy"

# Enable image (requires multimodal model)
WITH_IMAGE = True

# Set models and languages
STT_LANGUAGE = "en-us"

# Enable keyboard input
KEYBOARD_ENABLE = True

# Enable wake word
WAKE_ENABLE = True
WAKE_WORD = ["hey buddy"]
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
    tts=tts,
    keyboard_enable=KEYBOARD_ENABLE,
    wake_enable=WAKE_ENABLE,
    wake_word=WAKE_WORD,
    answer_on_wake=ANSWER_ON_WAKE,
    welcome=WELCOME,
    instructions=INSTRUCTIONS,
)

if __name__ == '__main__':
    vad.run()
