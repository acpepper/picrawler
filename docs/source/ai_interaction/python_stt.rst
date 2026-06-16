.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 愛好者コミュニティへようこそ！ Raspberry Pi、Arduino、ESP32 について、他の愛好者と一緒に深く掘り下げて学びましょう。

    **参加する理由は？**

    - **専門的なサポート**: 購入後の問題や技術的な課題を、コミュニティやチームの助けを借りて解決できます。
    - **学びと共有**: スキルを高めるためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**: 新しい製品発表や先行プレビューに早期アクセスできます。
    - **特別割引**: 最新製品に対する独占的な割引を楽しめます。
    - **祝典プロモーションとプレゼント**: プレゼントキャンペーンや季節ごとのプロモーションに参加できます。

    👉 私たちと一緒に探求し、創造する準備はできましたか？ [|link_sf_facebook|] をクリックして、今すぐ参加しましょう！

.. _py_stt:

15. STT (音声認識)
==============================================

この例では、PiCrawler で STT (音声認識) モジュールを使用する方法を示します。
ロボットは内蔵マイクを通してあなたの声を聞き、リアルタイムでテキストに変換します。

**コードの実行**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 15_stt.py

プログラムを実行すると、言語設定とプロンプトが表示されます。
ロボットが聞き取りを開始します — マイクに向かって話すと、認識された
テキストがターミナルに表示されます。

音声が検出されない場合は、``(no speech detected)`` と表示されます。
**Ctrl+C** で終了します。

**事前準備**

以下が完了していることを確認してください：

* :ref:`install_all_modules` — ``robot-hat``、``vilib``、``picrawler`` モジュールをインストールし、スクリプト ``i2samp.sh`` を実行します。

**コード**

.. note::
    以下のコードを **変更/リセット/コピー/実行/停止** できます。ただし、その前に
    ``picrawler\examples`` のようなソースコードのパスに移動する必要があります。
    コードを変更した後、直接実行して効果を確認できます。

.. raw:: html

    <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    from robot_hat.stt import STT

    # sunfounder_voice_assistant STT モジュールを使用した音声認識デモ
    # Ctrl+C で終了します

    # 言語設定: "en-us", "zh-cn" など
    LANGUAGE = "en-us"

    def main():
        print("=== PiCrawler 音声認識デモ ===")
        print(f"言語: {LANGUAGE}")
        print("Ctrl+C で終了します")
        print()

        stt = STT(language=LANGUAGE)

        try:
            while True:
                print("聞き取り中... (話しかけてください)")
                text = stt.listen()
                if text:
                    print(f">>> {text}")
                else:
                    print("(音声が検出されませんでした)")
        except KeyboardInterrupt:
            print("\n終了中...")

    if __name__ == "__main__":
        main()


**仕組み**

#. STT モジュールのインポート

   .. code-block:: python

      from robot_hat.stt import STT

   ``STT`` クラスは ``robot_hat`` パッケージの一部です。低レベルの
   オーディオキャプチャと音声認識処理をすべて処理します。

#. 言語の設定

   .. code-block:: python

      LANGUAGE = "en-us"

   ``LANGUAGE`` 変数で認識言語を設定します。必要に応じて
   ``"zh-cn"`` (中国語) などの他のサポートコードに変更できます。

#. STT インスタンスの作成

   .. code-block:: python

      stt = STT(language=LANGUAGE)

   選択した言語用に設定された STT オブジェクトを作成します。このオブジェクトは
   マイクと音声認識エンジンを初期化します。

#. 聞き取りループ

   .. code-block:: python

      while True:
          print("聞き取り中... (話しかけてください)")
          text = stt.listen()
          if text:
              print(f">>> {text}")
          else:
              print("(音声が検出されませんでした)")

   プログラムは無限ループを実行し、各反復で：

   - ユーザーに話すよう促します。
   - ``stt.listen()`` を呼び出し、音声が検出されて処理されるまでブロックします。
   - 認識されたテキストを文字列として返すか、何も理解できなかった場合は
     ``None`` / 空文字列を返します。
   - 結果をターミナルに表示します。

#. 正常終了

   .. code-block:: python

      except KeyboardInterrupt:
          print("\n終了中...")

   **Ctrl+C** を押すと ``KeyboardInterrupt`` が発生し、終了メッセージを
   表示してプログラムをクリーンに終了します。
