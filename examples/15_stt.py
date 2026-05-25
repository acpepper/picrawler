#!/usr/bin/env python3
from robot_hat.stt import STT

# Speech recognition demo using sunfounder_voice_assistant STT module
# Press Ctrl+C to exit

# Configure language: "en-us", "zh-cn", etc.
LANGUAGE = "en-us"

def main():
    print("=== PiCrawler Speech-to-Text Demo ===")
    print(f"Language: {LANGUAGE}")
    print("Press Ctrl+C to exit")
    print()

    stt = STT(language=LANGUAGE)

    try:
        while True:
            print("Listening... (speak now)")
            text = stt.listen()
            if text:
                print(f">>> {text}")
            else:
                print("(no speech detected)")
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()
