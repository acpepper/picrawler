.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 愛好者コミュニティへようこそ！ Raspberry Pi、Arduino、ESP32 について、他の愛好者と一緒に深く掘り下げて学びましょう。

    **参加する理由は？**

    - **専門的なサポート**: 購入後の問題や技術的な課題を、コミュニティやチームの助けを借りて解決できます。
    - **学びと共有**: スキルを高めるためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**: 新しい製品発表や先行プレビューに早期アクセスできます。
    - **特別割引**: 最新製品に対する独占的な割引を楽しめます。
    - **祝典プロモーションとプレゼント**: プレゼントキャンペーンや季節ごとのプロモーションに参加できます。

    👉 私たちと一緒に探求し、創造する準備はできましたか？ [|link_sf_facebook|] をクリックして、今すぐ参加しましょう！

.. _py_voice_active_gpt:

18. GPT との音声チャット
================================

この例では、:ref:`py_stt`、:ref:`py_tts`、および GPT 搭載 LLM を組み合わせて、
完全な音声対話型ロボットを作成します。PiCrawler はウェイクワードを聞き取り、
あなたの音声を理解し、AI が生成した会話で応答し、文脈に基づいて物理的な
アクションを実行します。

.. note::

    このプロジェクトは **VoiceActiveCrawler** クラスに依存しています。
    ``voice_active_crawler.py`` ファイルが examples ディレクトリに存在することを
    確認してください。また、``OPENAI_API_KEY`` を含む ``secret.py`` ファイルを
    作成してください。まだ API キーを取得していない場合は、
    :ref:`py_online_llm` (OpenAI セクション) で手順を確認してください。

**コードの実行**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 18_voice_active_crawler_gpt.py

実行後、ロボットは以下を初期化します：

- 音声認識用の STT エンジン
- 音声応答用の TTS エンジン (Piper)
- AI 会話用の LLM クライアント (GPT-4o-mini)
- ウェイクワード検出器

ロボットは歓迎メッセージであなたを迎えます。ウェイクワード (例: "Hey Buddy")
を言って会話を開始します。**Ctrl+C** で終了します。

**コード**

.. note::
    以下のコードを **変更/リセット/コピー/実行/停止** できます。ただし、その前に
    ``picrawler\examples`` のようなソースコードのパスに移動する必要があります。
    コードを変更した後、直接実行して効果を確認できます。

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

    # ロボットの名前
    NAME = "Buddy"

    # 画像認識を有効にする (マルチモーダルモデルが必要)
    WITH_IMAGE = True

    # モデルと言語の設定
    TTS_MODEL = "en_US-ryan-low"
    STT_LANGUAGE = "en-us"

    # キーボード入力を有効にする
    KEYBOARD_ENABLE = True

    # ウェイクワードを有効にする
    WAKE_ENABLE = True
    WAKE_WORD = ["hey buddy"]
    # ウェイクワードの応答を設定。空文字列にすると無効
    ANSWER_ON_WAKE = "Hi there"

    # 歓迎メッセージ
    WELCOME = f"Hi, I'm {NAME}. Wake me up with: " + ", ".join(WAKE_WORD)

    # 指示を設定
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


**仕組み**

#. VoiceActiveCrawler とは？

   ``VoiceActiveCrawler`` は、4 つのサブシステムを 1 つの音声対話パイプラインに
   統合する高レベルクラスです：

   - **STT** — 音声認識 (あなたの声を聞き取る)
   - **LLM** — AI 会話 (GPT があなたの発言を処理)
   - **TTS** — 音声合成 (AI の応答を話す)
   - **Actions** — 物理的な動き (ロボットがコマンドに基づいて動作)

#. ウェイクワードをトリガーとして使用

   .. code-block:: python

      WAKE_ENABLE = True
      WAKE_WORD = ["hey buddy"]

   有効にすると、ロボットは継続的にウェイクワードを聞き取ります。
   それを検出した後にのみ、ロボットは会話ターンを開始します。
   これにより、背景ノイズへの応答を防ぎます。

   .. code-block:: python

      ANSWER_ON_WAKE = "Hi there"

   ウェイクワードが認識されると、ロボットはコマンドを聞く前に
   オプションであなたに挨拶できます。空文字列に設定すると無効になります。

#. LLM の接続

   .. code-block:: python

      from picrawler.llm import OpenAI as LLM
      from secret import OPENAI_API_KEY as API_KEY

      llm = LLM(
          api_key=API_KEY,
          model="gpt-4o-mini",
      )

   ``picrawler.llm`` モジュールは OpenAI 互換のクライアントを提供します。
   API キーはバージョン管理外の別ファイル ``secret.py`` に保存してください。
   OpenAI API キーの作成と課金の有効化については :ref:`py_online_llm` を
   参照してください。

   ``gpt-4o-mini`` が推奨です：高速で手頃な価格であり、マルチモーダル入力
   (テキスト + 画像) をサポートしています。

#. マルチモーダルモデルによるビジョン

   .. code-block:: python

      WITH_IMAGE = True

   有効にすると、ロボットはカメラから写真を撮影し、あなたの音声質問と
   一緒に送信します。LLM はロボットが見ているものを「見る」ことができ —
   *「前に何色の物がある？」* のような対話が可能になります。

#. 指示によるロボットの性格設定

   .. code-block:: python

      INSTRUCTIONS = """
      You are a Raspberry Pi-based robotic spider...
      ## Actions You Can Perform:
      ["forward", "backward", "turn left", ...]
      ...
      """

   ``INSTRUCTIONS`` 文字列は LLM に送信される **システムプロンプト** です。
   以下を定義します：

   - ロボットのアイデンティティと性格 (ユーモラスで活発)
   - 利用可能な物理アクションのリスト
   - 必要な応答形式：最初にテキスト、次に ``ACTIONS:`` 行

   ``VoiceActiveCrawler`` は LLM の応答から ``ACTIONS:`` 行を解析し、
   それらのアクションをロボット上で実行します。

#. キーボードフォールバック

   .. code-block:: python

      KEYBOARD_ENABLE = True

   有効にすると、音声の代わりにキーボードでメッセージを入力することもできます。
   騒がしい環境やテスト中に便利です。

#. パイプライン概要

   完全な会話ループは次のように動作します：

   1. ロボットがウェイクワード (またはキーボード入力) を待ちます。
   2. トリガーされると、STT を通じてあなたの音声を録音します。
   3. 認識されたテキストが、オプションでカメラ画像と共に LLM に送信されます。
   4. LLM がテキスト応答とオプションのアクションリストを返します。
   5. ロボットが TTS で応答を話し、アクションを実行します。
   6. ループは次のウェイクワードの待機に戻ります。

#. 3 つの LLM バックエンド

   同じ ``VoiceActiveCrawler`` パイプラインが異なる LLM バックエンドで
   動作します。以下のレッスンで 2 つの代替案を示します：

   .. list-table::
      :header-rows: 1

      * - 機能
        - GPT (18)
        - Doubao (19)
        - Ollama (20)
      * - 実行場所
        - クラウド
        - クラウド
        - ローカル
      * - API キー
        - 必要
        - 必要
        - 不要
      * - 言語
        - 英語
        - 中国語
        - 英語
      * - ビジョン
        - 対応
        - 対応
        - 稀

   - :ref:`py_voice_doubao` — 同じクラウドアプローチを、ByteDance の Doubao
     モデルで中国語向けに適応。
   - :ref:`py_voice_ollama` — 完全に自分のハードウェア上で動作し、
     インターネットや API キーは不要。
