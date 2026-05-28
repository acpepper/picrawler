.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_voice_active_gpt:

18. Voice Chat with GPT
============================

This example combines :ref:`py_stt`, :ref:`py_tts`, and a GPT-powered LLM to
create a fully voice-interactive robot. PiCrawler listens for a wake word,
understands your speech, responds with AI-generated conversation, and performs
physical actions based on the context.

.. note::

    The project depends on the **VoiceActiveCrawler** class. Make sure the file
    ``voice_active_crawler.py`` is present in the examples directory. Also
    create a ``secret.py`` file with your ``OPENAI_API_KEY``. If you haven't
    obtained an API key yet, see :ref:`py_online_llm` (OpenAI section) for
    step-by-step instructions.

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 18_voice_active_crawler_gpt.py

After running, the robot initializes:

- The STT engine for speech recognition
- The TTS engine (Piper) for spoken responses
- The LLM client (GPT-4o-mini) for AI conversation
- The wake word detector

The robot greets you with a welcome message. Say the wake word (e.g. "Hey Buddy")
to start a conversation. Press **Ctrl+C** to exit.

**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you
    need to go to source code path like ``picrawler\examples``. After modifying
    the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler.llm import OpenAI as LLM
    from secret import OPENAI_API_KEY as API_KEY

    from voice_active_crawler import VoiceActiveCrawler

    llm = LLM(
        api_key=API_KEY,
        model="gpt-4o-mini",
    )

    # Robot name
    NAME = "Buddy"

    # Enable image (requires multimodal model)
    WITH_IMAGE = True

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
    )

    if __name__ == '__main__':
        vad.run()


**How it works?**

#. What Is VoiceActiveCrawler?

   ``VoiceActiveCrawler`` is a high-level class that wires together four
   subsystems into a single voice-interactive pipeline:

   - **STT** — speech recognition (listens to your voice)
   - **LLM** — AI conversation (GPT processes what you said)
   - **TTS** — speech synthesis (speaks the AI response)
   - **Actions** — physical movement (the robot acts on commands)

#. Using wake-word as trigger

   .. code-block:: python

      WAKE_ENABLE = True
      WAKE_WORD = ["hey buddy"]

   When enabled, the robot continuously listens for the wake word. Only after
   detecting it will the robot begin a conversation turn. This avoids
   responding to background noise.

   .. code-block:: python

      ANSWER_ON_WAKE = "Hi there"

   When the wake word is recognized, the robot can optionally greet you before
   listening for a command. Set to an empty string to disable the greeting.

#. Connecting the LLM

   .. code-block:: python

      from picrawler.llm import OpenAI as LLM
      from secret import OPENAI_API_KEY as API_KEY

      llm = LLM(
          api_key=API_KEY,
          model="gpt-4o-mini",
      )

   The ``picrawler.llm`` module provides an OpenAI-compatible client.
   Store your API key in a separate ``secret.py`` file to keep it out of
   version control. See :ref:`py_online_llm` for how to create an OpenAI API
   key and enable billing.

   ``gpt-4o-mini`` is recommended: it is fast, affordable, and supports
   multimodal input (text + images).

#. Vision with Multimodal Models

   .. code-block:: python

      WITH_IMAGE = True

   When enabled, the robot captures a photo from its camera and sends it
   along with your spoken question. The LLM can then "see" what the robot
   sees — allowing interactions like *"What color is the object in front
   of you?"*

#. Setting the Robot's Personality with Instructions

   .. code-block:: python

      INSTRUCTIONS = """
      You are a Raspberry Pi-based robotic spider...
      ## Actions You Can Perform:
      ["forward", "backward", "turn left", ...]
      ...
      """

   The ``INSTRUCTIONS`` string is the **system prompt** sent to the LLM. It
   defines:

   - The robot's identity and personality (humorous, lively)
   - The list of available physical actions
   - The required response format: text first, then an ``ACTIONS:`` line

   The ``VoiceActiveCrawler`` parses the ``ACTIONS:`` line from the LLM's
   response and executes those actions on the robot.

#. Keyboard Fallback

   .. code-block:: python

      KEYBOARD_ENABLE = True

   When enabled, you can also type messages via keyboard instead of speaking.
   This is useful in noisy environments or during testing.

#. Pipeline Overview

   The complete conversation loop works like this:

   1. Robot listens for the wake word (or keyboard input).
   2. Once triggered, it records your speech via STT.
   3. The recognized text is sent to the LLM, optionally with a camera image.
   4. The LLM returns a text response and an optional action list.
   5. The robot speaks the response via TTS and performs the actions.
   6. The loop returns to listening for the next wake word.

#. Three LLM Backends

   The same ``VoiceActiveCrawler`` pipeline works with different LLM backends.
   The following lessons show two alternatives:

   .. list-table::
      :header-rows: 1

      * - Feature
        - GPT (18)
        - Doubao (19)
        - Ollama (20)
      * - Runs on
        - Cloud
        - Cloud
        - Local
      * - API key
        - Required
        - Required
        - None
      * - Language
        - English
        - Chinese
        - English
      * - Vision
        - Yes
        - Yes
        - Rarely

   - :ref:`py_voice_doubao` — Same cloud approach, adapted for Chinese with
     ByteDance's Doubao model.
   - :ref:`py_voice_ollama` — Runs entirely on your own hardware, no internet
     or API key needed.
