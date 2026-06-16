.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 愛好者コミュニティへようこそ！ Raspberry Pi、Arduino、ESP32 について、他の愛好者と一緒に深く掘り下げて学びましょう。

    **参加する理由は？**

    - **専門的なサポート**: 購入後の問題や技術的な課題を、コミュニティやチームの助けを借りて解決できます。
    - **学びと共有**: スキルを高めるためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**: 新しい製品発表や先行プレビューに早期アクセスできます。
    - **特別割引**: 最新製品に対する独占的な割引を楽しめます。
    - **祝典プロモーションとプレゼント**: プレゼントキャンペーンや季節ごとのプロモーションに参加できます。

    👉 私たちと一緒に探求し、創造する準備はできましたか？ [|link_sf_facebook|] をクリックして、今すぐ参加しましょう！

.. _py_tts:

16. TTS (音声合成)
==============================================

この例では、TTS (音声合成) モジュールを使って PiCrawler を話させる方法を示します。
2 つのエンジンをサポートしています：**Piper** (高品質なニューラル TTS) と
**Espeak** (軽量な従来型 TTS) です。任意のテキストを入力すると、ロボットが
それを読み上げます。

**コードの実行**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 16_tts.py

プログラムを実行すると、エンジンの種類とモデルが表示されます。任意の
文章を入力して **Enter** を押すと — ロボットがそれを話します。
``quit`` と入力して終了するか、**Ctrl+C** を押します。

**コード**

.. note::
    以下のコードを **変更/リセット/コピー/実行/停止** できます。ただし、その前に
    ``picrawler\examples`` のようなソースコードのパスに移動する必要があります。
    コードを変更した後、直接実行して効果を確認できます。

.. raw:: html

    <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    from robot_hat.tts import Piper, Espeak

    # robot_hat TTS モジュールを使用した音声合成デモ
    # Ctrl+C で終了します

    # USE_PIPER=True で高品質ニューラル TTS (Piper)、False で Espeak
    USE_PIPER = True

    # Piper モデル: "en_US-ryan-low" (英語), "zh_CN-huayan-x_low" (中国語)
    TTS_MODEL = "en_US-ryan-low"

    def main():
        print("=== PiCrawler 音声合成デモ ===")

        if USE_PIPER:
            print(f"エンジン: Piper ({TTS_MODEL})")
            tts = Piper(model=TTS_MODEL)
        else:
            print("エンジン: Espeak")
            tts = Espeak()

        print("話すテキストを入力してください。'quit' で終了します")
        print()

        try:
            while True:
                text = input("話すテキスト: ").strip()
                if text.lower() == 'quit':
                    break
                if text:
                    print(f"再生中: {text}")
                    tts.say(text)
        except KeyboardInterrupt:
            print("\n終了中...")

    if __name__ == "__main__":
        main()


**仕組み**

#. 2 つの TTS エンジンが利用可能

   .. code-block:: python

      from robot_hat.tts import Piper, Espeak

   ``robot_hat`` パッケージは 2 つの TTS エンジンを提供します：

   - **Piper**: ニューラルネットワークベースのエンジンで、自然で高品質な
     音声を生成します。音声モデルファイルが必要です。
   - **Espeak**: 軽量でルールベースのエンジンで、最小限のリソースで動作します。

#. エンジンとモデルの選択

   .. code-block:: python

      USE_PIPER = True
      TTS_MODEL = "en_US-ryan-low"

   ``USE_PIPER`` を ``True`` にすると Piper、``False`` にすると Espeak を
   使用します。Piper を使用する場合、``TTS_MODEL`` で音声を選択します。
   一般的なモデルは以下の通りです：

   - ``"en_US-ryan-low"`` — アメリカ英語の男性音声
   - ``"zh_CN-huayan-x_low"`` — 中国語の女性音声

#. TTS インスタンスの作成

   .. code-block:: python

      if USE_PIPER:
          tts = Piper(model=TTS_MODEL)
      else:
          tts = Espeak()

   ``USE_PIPER`` フラグに基づいて、適切なエンジンがインスタンス化されます。
   両方のエンジンは同じ ``say()`` インターフェースを共有しているため、
   エンジンを切り替えても他のコードを変更する必要はありません。

#. 入力ループ

   .. code-block:: python

      while True:
          text = input("話すテキスト: ").strip()
          if text.lower() == 'quit':
              break
          if text:
              print(f"再生中: {text}")
              tts.say(text)

   プログラムはテキストの入力を求めます：

   - 任意の文章を入力して **Enter** を押すと、ロボットが話します。
   - ``quit`` と入力してループを終了します。
   - いつでも **Ctrl+C** で中断できます。

#. STT との対比

   このレッスンは :ref:`py_stt` の対になるものです。STT (音声認識) と
   TTS (音声合成) が組み合わさって、PiCrawler の音声インターフェースの
   入力と出力の両方を形成します。
