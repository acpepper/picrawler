.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_tts:

16. TTS (Text-to-Speech)
==============================================

This example demonstrates how to use the TTS (Text-to-Speech) module to make
PiCrawler speak. It supports two engines: **Piper** (high-quality neural TTS)
and **Espeak** (lightweight classic TTS). Type any text and the robot will
read it aloud.

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 16_tts.py

After running the program, the engine type and model are displayed. Type any
sentence and press **Enter** — the robot speaks it. Type ``quit`` to exit, or
press **Ctrl+C**.

**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you
    need to go to source code path like ``picrawler\examples``. After modifying
    the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python

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


**How it works?**

#. Two TTS Engines Available

   .. code-block:: python

      from robot_hat.tts import Piper, Espeak

   The ``robot_hat`` package provides two TTS engines:

   - **Piper**: A neural-network-based engine that produces natural, high-quality
     speech. Requires a voice model file.
   - **Espeak**: A lightweight, rule-based engine that runs on minimal resources.

#. Choosing the Engine and Model

   .. code-block:: python

      USE_PIPER = True
      TTS_MODEL = "en_US-ryan-low"

   Set ``USE_PIPER`` to ``True`` for Piper or ``False`` for Espeak. When using
   Piper, ``TTS_MODEL`` selects the voice. Common models include:

   - ``"en_US-ryan-low"`` — American English male voice
   - ``"zh_CN-huayan-x_low"`` — Chinese female voice

#. Creating the TTS Instance

   .. code-block:: python

      if USE_PIPER:
          tts = Piper(model=TTS_MODEL)
      else:
          tts = Espeak()

   Based on the ``USE_PIPER`` flag, the appropriate engine is instantiated.
   Both engines share the same ``say()`` interface, so switching engines
   requires no other code changes.

#. The Input Loop

   .. code-block:: python

      while True:
          text = input("Text to speak: ").strip()
          if text.lower() == 'quit':
              break
          if text:
              print(f"Speaking: {text}")
              tts.say(text)

   The program prompts you for text:

   - Type any sentence and press **Enter** to make the robot speak.
   - Type ``quit`` to exit the loop.
   - Press **Ctrl+C** at any time to interrupt.

#. Contrast with STT

   This lesson is the companion to :ref:`py_stt`. Together, STT (speech
   recognition) and TTS (speech synthesis) form the input and output halves
   of a voice interface for PiCrawler.
