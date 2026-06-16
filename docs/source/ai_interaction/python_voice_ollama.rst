.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 愛好者コミュニティへようこそ！ Raspberry Pi、Arduino、ESP32 について、他の愛好者と一緒に深く掘り下げて学びましょう。

    **参加する理由は？**

    - **専門的なサポート**: 購入後の問題や技術的な課題を、コミュニティやチームの助けを借りて解決できます。
    - **学びと共有**: スキルを高めるためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**: 新しい製品発表や先行プレビューに早期アクセスできます。
    - **特別割引**: 最新製品に対する独占的な割引を楽しめます。
    - **祝典プロモーションとプレゼント**: プレゼントキャンペーンや季節ごとのプロモーションに参加できます。

    👉 私たちと一緒に探求し、創造する準備はできましたか？ [|link_sf_facebook|] をクリックして、今すぐ参加しましょう！

.. _py_voice_ollama:

20. Ollama によるローカル音声チャット
======================================================

この例では、クラウドベースの GPT API をローカルで実行される **Ollama** LLM に
置き換えます。すべての AI 処理は自分のマシン上で行われます — インターネット
不要、API キーの管理も不要です。完全にオフラインの音声対話型ロボットです。

**コードの実行**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 20_voice_active_crawler_ollama.py

**コード**

.. note::
    以下のコードを **変更/リセット/コピー/実行/停止** できます。ただし、その前に
    ``picrawler\examples`` のようなソースコードのパスに移動する必要があります。
    コードを変更した後、直接実行して効果を確認できます。

.. raw:: html

    <run></run>

.. code-block:: python

   from picrawler.llm import Ollama as LLM

   from voice_active_crawler import VoiceActiveCrawler

   # Ollama が同じ Raspberry Pi 上で動作する場合は "localhost" を使用。
   # LAN 内の別のコンピュータで動作する場合は、そのコンピュータの IP アドレスに置き換えてください。
   llm = LLM(
      ip="localhost",
      model="llama3.2:3b"   # 任意のモデルに置き換え可能
   )

   # ロボットの名前
   NAME = "Buddy"

   # 画像認識を有効にする (マルチモーダルモデルが必要)
   WITH_IMAGE = False

   # モデルと言語の設定
   TTS_MODEL = "en_US-ryan-low"
   STT_LANGUAGE = "en-us"

   # キーボード入力を有効にする
   KEYBOARD_ENABLE = True

   # ウェイクワードを有効にする
   WAKE_ENABLE = True
   WAKE_WORD = ["hey buddy"]
   # ウェイクワード応答。空文字列にすると無効
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
      disable_think=True,
   )

   if __name__ == '__main__':
      vad.run()


**仕組み**

#. Ollama とは？

   `Ollama <https://ollama.com/>`_ は、大規模言語モデルを自分のハードウェア上で
   ローカルに実行するためのツールです。クラウド API を呼び出す GPT レッスンとは
   異なり、この例ではすべてをデバイス上で実行します — 会話は Raspberry Pi
   (またはローカルネットワーク) から出ることはありません。

   .. code-block::

      # Ollama をインストールし、モデルをプル：
      ollama pull llama3.2:3b

#. ローカル LLM 接続

   .. code-block:: python

      from picrawler.llm import Ollama as LLM

      llm = LLM(
          ip="localhost",
          model="llama3.2:3b"
      )

   ``Ollama`` クラスは OpenAI 互換 API を通じて Ollama サーバーに接続します。
   クラウド GPT セットアップとの主な違い：

   - **API キー不要** — ローカルサーバーには認証は必要ありません。
   - **IP アドレス** — Ollama が同じ Pi 上で動作する場合は ``"localhost"``、
     別のコンピュータで動作する場合は ``"192.168.1.100"`` のような LAN IP を
     使用します。
   - **モデル** — Ollama でプルした任意のモデルが動作します (``llama3.2:3b``、
     ``qwen2.5:7b``、``mistral`` など)。

#. ビジョンの無効化

   .. code-block:: python

      WITH_IMAGE = False

   ほとんどの Ollama モデルはマルチモーダル (画像) 入力をサポートしていません。
   ``WITH_IMAGE`` を ``False`` に設定すると、カメラキャプチャ手順をスキップ
   します。視覚対応モデル (例: ``llava``) をプルした場合は、``True`` に
   設定できます。

#. Think の無効化

   .. code-block:: python

      vad = VoiceActiveCrawler(
          ...
          disable_think=True,
      )

   一部の Ollama モデル (特に ``qwen2.5`` のような推論モデル) は出力に
   ``<think>`` タグを出力します。``disable_think=True`` を設定すると、
   ``VoiceActiveCrawler`` がこれらのタグを除去し、ロボットが最終回答だけを
   話すようにします。

#. 同じパイプライン、オフライン

   会話パイプラインは :ref:`py_voice_active_gpt` と同一です：

   1. ウェイクワード検出がターンを開始します。
   2. STT があなたの音声をテキストに変換します。
   3. テキストがローカルの Ollama LLM に送信されます。
   4. LLM が応答とオプションのアクションを返します。
   5. TTS が応答を話し、ロボットがアクションを実行します。

   決定的な違い：**ステップ 3 が自分のハードウェア上で実行され**、
   クラウド依存、レート制限がなく、完全なプライバシーが保たれます。

#. ハードウェアの考慮事項

   LLM をローカルで実行するのはリソース集約的です。Raspberry Pi では：

   - **小さいモデル** (3B パラメータ、``llama3.2:3b`` など) は遅いですが
     動作します。応答ごとに数秒の処理時間を想定してください。
   - **大きいモデル** (7B+) は Pi での対話的な使用には遅すぎます。
   - より良いパフォーマンスを得るには、LAN 内の別のコンピュータで Ollama を
     実行し、``ip`` パラメータをそのコンピュータに向けます。
