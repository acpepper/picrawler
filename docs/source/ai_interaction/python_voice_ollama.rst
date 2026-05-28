.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_voice_ollama:

20. Local Voice Chat with Ollama
==================================================

This example replaces the cloud-based GPT API with a locally running
**Ollama** LLM. All AI processing stays on your own machine — no internet
required, no API keys to manage. It's a fully offline voice-interactive
robot.

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 20_voice_active_crawler_ollama.py

**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you
    need to go to source code path like ``picrawler\examples``. After modifying
    the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python

   from picrawler.llm import Ollama as LLM

   from voice_active_crawler import VoiceActiveCrawler

   # If Ollama runs on the same Raspberry Pi, use "localhost".
   # If it runs on another computer in your LAN, replace with that computer's IP address.
   llm = LLM(
      ip="localhost",
      model="llama3.2:3b"   # you can replace with any model
   )

   # Robot name
   NAME = "Buddy"

   # Enable image (requires multimodal model)
   WITH_IMAGE = False

   # Set models and languages
   TTS_MODEL = "en_US-ryan-low"
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


**How it works?**

#. What Is Ollama?

   `Ollama <https://ollama.com/>`_ is a tool for running large language models
   locally on your own hardware. Unlike the GPT lesson which calls a cloud API,
   this example runs everything on-device — your conversations never leave the
   Raspberry Pi (or your local network).

   .. code-block::

      # Install Ollama, then pull a model:
      ollama pull llama3.2:3b

#. Local LLM Connection

   .. code-block:: python

      from picrawler.llm import Ollama as LLM

      llm = LLM(
          ip="localhost",
          model="llama3.2:3b"
      )

   The ``Ollama`` class connects to an Ollama server via its OpenAI-compatible
   API. Key differences from the cloud GPT setup:

   - **No API key** — authentication is not needed for a local server.
   - **IP address** — use ``"localhost"`` if Ollama runs on the same Pi, or
     a LAN IP like ``"192.168.1.100"`` if it runs on another computer.
   - **Model** — any model you've pulled in Ollama works (``llama3.2:3b``,
     ``qwen2.5:7b``, ``mistral``, etc.).

#. Disabling Vision

   .. code-block:: python

      WITH_IMAGE = False

   Most Ollama models do not support multimodal (image) input. Setting
   ``WITH_IMAGE`` to ``False`` skips the camera capture step. If you do pull
   a vision-capable model (e.g. ``llava``), you can set this to ``True``.

#. Disabling Think

   .. code-block:: python

      vad = VoiceActiveCrawler(
          ...
          disable_think=True,
      )

   Some Ollama models (especially reasoning models like ``qwen2.5``) emit
   ``<think>`` tags in their output. Setting ``disable_think=True`` tells
   ``VoiceActiveCrawler`` to strip these tags so the robot only speaks the
   final answer.

#. The Same Pipeline, Offline

   The conversation pipeline is identical to :ref:`py_voice_active_gpt`:

   1. Wake word detection triggers a turn.
   2. STT converts your speech to text.
   3. The text is sent to the local Ollama LLM.
   4. The LLM returns a response and optional actions.
   5. TTS speaks the response, and the robot performs actions.

   The critical difference: **step 3 runs on your own hardware**, with no
   cloud dependency, no rate limits, and complete privacy.

#. Hardware Considerations

   Running an LLM locally is resource-intensive. On a Raspberry Pi:

   - **Smaller models** (3B parameters, like ``llama3.2:3b``) run slowly but
     work; expect several seconds of processing per response.
   - **Larger models** (7B+) will be too slow for interactive use on a Pi.
   - For better performance, run Ollama on a separate computer in your LAN
     and point the ``ip`` parameter to it.
