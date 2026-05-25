#!/usr/bin/env python3
from robot_hat.tts import Piper, Espeak

# Text-to-Speech demo using robot_hat TTS module
# Press Ctrl+C to exit

# Set USE_PIPER=True for high-quality neural TTS (Piper), False for Espeak
USE_PIPER = True

# Piper model: "en_US-ryan-low" (English), "zh_CN-huayan-x_low" (Chinese)
TTS_MODEL = "en_US-ryan-low"

def main():
    print("=== PiCrawler Text-to-Speech Demo ===")

    if USE_PIPER:
        print(f"Engine: Piper ({TTS_MODEL})")
        tts = Piper(model=TTS_MODEL)
    else:
        print("Engine: Espeak")
        tts = Espeak()

    print("Type text to speak, or 'quit' to exit")
    print()

    try:
        while True:
            text = input("Text to speak: ").strip()
            if text.lower() == 'quit':
                break
            if text:
                print(f"Speaking: {text}")
                tts.say(text)
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()
