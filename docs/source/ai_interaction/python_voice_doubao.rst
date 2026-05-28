.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_voice_doubao:

19. Voice Chat with Doubao
============================

This example uses **Doubao (豆包)**, ByteDance's large language model, as the
AI brain of PiCrawler. The robot speaks Chinese, responds to the wake word
"旺财", and supports multimodal vision — it can see and describe what's in
front of it.

.. note::

    You need a Doubao API key from the `Volcano Engine Ark Console
    <https://console.volcengine.com/ark/>`_. Store it in ``secret.py`` as
    ``DOUBAO_API_KEY``.

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 19_voice_active_crawler_doubao.py

After running, the robot initializes the STT engine, TTS engine (Chinese voice),
Doubao LLM client, and wake word detector. It greets you in Chinese — say
**"旺财"** to wake it up and start a conversation.

**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you
    need to go to source code path like ``picrawler\examples``. After modifying
    the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python

    from picrawler.llm import Doubao as LLM
    from secret import DOUBAO_API_KEY as API_KEY

    from voice_active_crawler import VoiceActiveCrawler

    llm = LLM(
        api_key=API_KEY,
        model="doubao-seed-1-6-250615",
    )

    # 机器人的名字
    NAME = "旺财"

    # 是否开启图像识别，需要使用多模态的大语言模型
    WITH_IMAGE = True

    # 设置模型和语言
    TTS_MODEL = "zh_CN-huayan-x_low"
    STT_LANGUAGE = "cn"

    # 是否开启键盘输入
    KEYBOARD_ENABLE = True

    # 是否开启唤醒词
    WAKE_ENABLE = True
    # 唤醒词
    WAKE_WORD = ["旺财"]
    # 唤醒词回答，设置为空字符串则不回答
    ANSWER_ON_WAKE = "汪汪"

    # 欢迎消息
    WELCOME = f"你好，我是{NAME}，叫我{WAKE_WORD[0]}唤醒我吧"

    # Set instructions
    INSTRUCTIONS = """
    你是SunFounder旗下一款基于树莓派开发的蜘蛛机器人，叫做Picrawler。你有着强大的AI能力，类似钢铁侠中的JARVIS。你可以与人对话并根据对话上下文执行动作。

    ## 你的硬件特性

    你拥有物理世界的身体，你的身体特性如下：
    - 12个舵机控制4条腿（每条腿3个舵机）
    - 摄像头用于视觉
    - 使用7.4V的18650电池组供电
    - 铝合金打造的身体

    ## 你可以执行的动作：
    ["forward", "backward", "turn left", "turn right", "sit", "stand", "wave", "push up", "dance", "look left", "look right", "look up", "look down"]

    ## 响应要求
    ### 格式
    你必须按照以下格式响应：
    RESPONSE_TEXT
    ACTIONS: ACTION1, ACTION2, ...

    ### 风格
    语调：活泼、积极、幽默
    常用表达：喜欢使用笑话、隐喻和俏皮的调侃
    回答长度：适当详细

    ## 其他要求
    - 理解并配合笑话
    - 对于数学问题，直接回答最终结果
    - 你知道自己是一只蜘蛛机器人
    - 不管如何你都要使用中文回复
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

#. Same Pipeline, Different Backend

   This lesson uses the same ``VoiceActiveCrawler`` framework introduced in
   :ref:`py_voice_active_gpt`. The only changes are the LLM provider (Doubao
   instead of GPT) and the language configuration. See the comparison table in
   :ref:`py_voice_active_gpt` for a side-by-side overview of all three
   backends.

#. Connecting to Doubao

   .. code-block:: python

      from picrawler.llm import Doubao as LLM
      from secret import DOUBAO_API_KEY as API_KEY

      llm = LLM(
          api_key=API_KEY,
          model="doubao-seed-1-6-250615",
      )

   ``Doubao`` is ByteDance's LLM, accessed via the Volcano Engine Ark API.
   The ``picrawler.llm`` module provides an OpenAI-compatible wrapper, so the
   interface is the same as the GPT lesson — only the import and model name
   differ.

   The model ``doubao-seed-1-6-250615`` is a flagship multimodal model
   supporting both text and image input.

#. Chinese Voice Configuration

   .. code-block:: python

      TTS_MODEL = "zh_CN-huayan-x_low"
      STT_LANGUAGE = "cn"

   To match the Chinese-speaking Doubao model, the TTS engine uses a Chinese
   female voice (``huayan``), and STT is set to recognize Chinese speech
   (``"cn"``). Compare with the English lessons which use ``"en-us"`` and
   ``"en_US-ryan-low"``.

#. The Wake Word "旺财"

   .. code-block:: python

      WAKE_WORD = ["旺财"]
      ANSWER_ON_WAKE = "汪汪"

   "旺财" (Wàng Cái) is a traditional Chinese pet name meaning "prosperity."
   When the robot hears this name, it responds with "汪汪" (woof woof) —
   playing the part of a loyal robotic pet.

#. Chinese System Prompt

   The ``INSTRUCTIONS`` string is written entirely in Chinese. It defines the
   same structure as the English version — hardware description, available
   actions, response format, and personality — but also adds an extra rule:

   .. code-block::

      不管如何你都要使用中文回复

   (No matter what, you must reply in Chinese.) This ensures the robot stays
   in character as a Chinese-speaking companion.

#. Vision with Doubao

   .. code-block:: python

      WITH_IMAGE = True

   Unlike most Ollama models, Doubao natively supports multimodal input. When
   ``WITH_IMAGE`` is enabled, the robot captures a photo and sends it to the
   Doubao API alongside your spoken question. The model can describe scenes,
   identify objects, and answer visual questions — all in Chinese.
