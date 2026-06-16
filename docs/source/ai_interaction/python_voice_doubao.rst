.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 愛好者コミュニティへようこそ！ Raspberry Pi、Arduino、ESP32 について、他の愛好者と一緒に深く掘り下げて学びましょう。

    **参加する理由は？**

    - **専門的なサポート**: 購入後の問題や技術的な課題を、コミュニティやチームの助けを借りて解決できます。
    - **学びと共有**: スキルを高めるためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**: 新しい製品発表や先行プレビューに早期アクセスできます。
    - **特別割引**: 最新製品に対する独占的な割引を楽しめます。
    - **祝典プロモーションとプレゼント**: プレゼントキャンペーンや季節ごとのプロモーションに参加できます。

    👉 私たちと一緒に探求し、創造する準備はできましたか？ [|link_sf_facebook|] をクリックして、今すぐ参加しましょう！

.. _py_voice_doubao:

19. Doubao との音声チャット
================================

この例では、ByteDance の大規模言語モデル **Doubao (豆包)** を PiCrawler の
AI 頭脳として使用します。ロボットは中国語を話し、ウェイクワード「旺财」に
応答し、マルチモーダルビジョンをサポートします — 目の前にあるものを
見て説明することができます。

.. note::

    `Volcano Engine Ark Console <https://console.volcengine.com/ark/>`_
    から Doubao API キーが必要です。``secret.py`` に ``DOUBAO_API_KEY`` として
    保存してください。

**コードの実行**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 19_voice_active_crawler_doubao.py

実行後、ロボットは STT エンジン、TTS エンジン (中国語音声)、Doubao LLM
クライアント、ウェイクワード検出器を初期化します。中国語であなたを迎えます —
**「旺财」** と言って起こし、会話を始めてください。

**コード**

.. note::
    以下のコードを **変更/リセット/コピー/実行/停止** できます。ただし、その前に
    ``picrawler\examples`` のようなソースコードのパスに移動する必要があります。
    コードを変更した後、直接実行して効果を確認できます。

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

    # ロボットの名前
    NAME = "旺财"

    # 画像認識を有効にする (マルチモーダルモデルが必要)
    WITH_IMAGE = True

    # モデルと言語の設定
    TTS_MODEL = "zh_CN-huayan-x_low"
    STT_LANGUAGE = "cn"

    # キーボード入力を有効にする
    KEYBOARD_ENABLE = True

    # ウェイクワードを有効にする
    WAKE_ENABLE = True
    # ウェイクワード
    WAKE_WORD = ["旺财"]
    # ウェイクワード応答。空文字列にすると無効
    ANSWER_ON_WAKE = "汪汪"

    # 歓迎メッセージ
    WELCOME = f"你好、私は{NAME}、{WAKE_WORD[0]}と呼んで起こしてください"

    # 指示を設定
    INSTRUCTIONS = """
    あなたはSunFounderが開発した Raspberry Pi ベースのクモ型ロボット、Picrawler です。Iron Man の JARVIS のような強力な AI 能力を持っています。人と会話し、文脈に基づいてアクションを実行できます。

    ## ハードウェア特性

    物理的な身体を持ち、以下の特徴があります：
    - 12個のサーボで4本の脚を制御 (各脚3個のサーボ)
    - 視覚用カメラ
    - 7.4V 18650 バッテリーパックで駆動
    - アルミ合金ボディ

    ## 実行可能なアクション：
    ["forward", "backward", "turn left", "turn right", "sit", "stand", "wave", "push up", "dance", "look left", "look right", "look up", "look down"]

    ## 応答要件
    ### 形式
    以下の形式で応答すること：
    RESPONSE_TEXT
    ACTIONS: ACTION1, ACTION2, ...

    ### スタイル
    トーン: 活発、前向き、ユーモラス
    よく使う表現: ジョーク、比喩、遊び心のあるからかい
    回答の長さ: 適度に詳細

    ## その他の要件
    - ジョークを理解し合わせる
    - 数学問題は最終結果を直接回答
    - 自分がクモ型ロボットであることを認識している
    - 常に日本語で返答すること
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

#. 同じパイプライン、異なるバックエンド

   このレッスンでは、:ref:`py_voice_active_gpt` で紹介したものと同じ
   ``VoiceActiveCrawler`` フレームワークを使用します。変更点は LLM
   プロバイダー (GPT の代わりに Doubao) と言語設定のみです。
   3 つのバックエンドの比較表は :ref:`py_voice_active_gpt` を参照してください。

#. Doubao への接続

   .. code-block:: python

      from picrawler.llm import Doubao as LLM
      from secret import DOUBAO_API_KEY as API_KEY

      llm = LLM(
          api_key=API_KEY,
          model="doubao-seed-1-6-250615",
      )

   ``Doubao`` は ByteDance の LLM で、Volcano Engine Ark API を通じて
   アクセスします。``picrawler.llm`` モジュールは OpenAI 互換のラッパーを
   提供しているため、インターフェースは GPT のレッスンと同じです —
   インポートとモデル名だけが異なります。

   モデル ``doubao-seed-1-6-250615`` はテキストと画像入力の両方を
   サポートするフラッグシップのマルチモーダルモデルです。

#. 中国語音声の設定

   .. code-block:: python

      TTS_MODEL = "zh_CN-huayan-x_low"
      STT_LANGUAGE = "cn"

   中国語を話す Doubao モデルに合わせて、TTS エンジンは中国語の女性音声
   (``huayan``) を使用し、STT は中国語の音声認識 (``"cn"``) に設定されています。
   ``"en-us"`` と ``"en_US-ryan-low"`` を使用する英語のレッスンと比較して
   ください。

#. ウェイクワード「旺财」

   .. code-block:: python

      WAKE_WORD = ["旺财"]
      ANSWER_ON_WAKE = "汪汪"

   「旺财」(ワンツァイ) は「繁栄」を意味する伝統的な中国のペットの名前です。
   ロボットはこの名前を聞くと「汪汪」(ワンワン) と応答します —
   忠実なロボットペットの役割を演じています。

#. 中国語のシステムプロンプト

   ``INSTRUCTIONS`` 文字列は完全に中国語で書かれています。英語版と同じ構造 —
   ハードウェアの説明、利用可能なアクション、応答形式、性格 — を定義して
   いますが、追加のルールもあります：

   .. code-block::

      常に中国語で返答すること

   これにより、ロボットは中国語を話す仲間としてのキャラクターを保ちます。

#. Doubao によるビジョン

   .. code-block:: python

      WITH_IMAGE = True

   ほとんどの Ollama モデルとは異なり、Doubao はネイティブにマルチモーダル入力を
   サポートしています。``WITH_IMAGE`` を有効にすると、ロボットは写真を撮影し、
   音声質問と共に Doubao API に送信します。モデルはシーンを説明し、物体を識別し、
   視覚的な質問に答えることができます — すべて中国語で。
