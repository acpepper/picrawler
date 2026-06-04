.. note::

    こんにちは！SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Raspberry Pi、Arduino、ESP32について、他の愛好者と共にさらに深く学びましょう。

    **参加する理由**

    - **専門家のサポート**: 購入後の問題や技術的な課題を、コミュニティやチームのサポートで解決できます。
    - **学びと共有**: ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **特別なプレビュー**: 新製品の発表や先行公開に早期アクセスできます。
    - **特別割引**: 新しい製品に対する限定割引をお楽しみください。
    - **祝祭プロモーションとプレゼント**: プレゼントや祝祭プロモーションに参加できます。

    👉 私たちと一緒に探求し、創造する準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_action_gallery:

14. アクションギャラリー
===========================

この例では、PiCrawler のさまざまなプリプログラム済みアクション（手を振る、
握手、ファイティング、うなずき、腕立て伏せなど）をトリガーできる対話型
メニューを提供します。

**コードを実行する**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 14_action_gallery.py

実行後、利用可能なアクションの番号付きリストが端末に表示されます。実行したい
アクションの番号を入力して **Enter** を押します。再度 **Enter** を押すと直前の
アクションを繰り返します。**Ctrl+C** で安全に終了し、ロボットは座った姿勢に
戻ります。

**コード**

.. note::
    以下のコードは **変更/リセット/コピー/実行/停止** できます。ただし、まずソースコードのパス（例: ``picrawler\examples`` ）に移動する必要があります。コードを修正した後、直接実行して効果を確認できます。

.. raw:: html

    <run></run>

.. code-block:: python

    from time import sleep

    BODY_LENGTH = 77
    BODY_WIDTH = 77
    BODY_DIAGONAL = 108.9
    DELTA = 45


    def sit(spider):
        spider.do_action('sit', speed=40)


    def stand(spider):
        spider.do_action('stand', speed=40)


    def look_up(spider):
        coords = [
            # stand
            [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
            [[45, 45, -76], [45, 0, -76], [45, 0, -38], [45, 45, -30]],
        ]

        for coord in coords:
            spider.do_step(coord, 60)


    def look_down(spider):
        coords = [
            # stand
            [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
            [[45, 45, -28], [45, 0, -40], [45, 0, -68], [45, 45, -76]],
        ]
        for coord in coords:
            spider.do_step(coord, 60)


    def dance(spider):
        spider.do_action('dance', speed=60)


    def wave_hand(spider):
        coords = [
            # stand
            [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
            # wave hand
            [[45, 45, -70], [60, 0, 120], [45, 0, -60], [45, 45, -30]],
            [[45, 45, -70], [-20, 60, 120], [45, 0, -60], [45, 45, -30]],
            [[45, 45, -70], [60, 0, 120], [45, 0, -60], [45, 45, -30]],
            [[45, 45, -70], [-20, 60, 120], [45, 0, -60], [45, 45, -30]],
            # return to stand
            [[45, 45, -50], [45, 0, -30], [45, 0, -50], [45, 45, -50]],
            [[45, 45, -50], [45, 0, -40], [45, 0, -50], [45, 45, -50]],
            [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
        ]

        for coord in coords:
            spider.do_step(coord, 58)


    def shake_hand(spider):
        coords = [
            # stand
            [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
            # shake hand
            [[45, 45, -65], [5, 280, 80], [45, 0, -60], [45, 45, -40]],
            [[45, 45, -65], [5, 280, 100], [45, 0, -60], [45, 45, -40]],
            [[45, 45, -65], [5, 280, -10], [45, 0, -60], [45, 45, -40]],
            [[45, 45, -65], [5, 280, 100], [45, 0, -60], [45, 45, -40]],
            [[45, 45, -65], [5, 280, -10], [45, 0, -60], [45, 45, -40]],
            [[45, 45, -65], [5, 280, 100], [45, 0, -60], [45, 45, -40]],
            [[45, 45, -65], [5, 280, -10], [45, 0, -60], [45, 45, -40]],
            [[45, 45, -65], [5, 100, 10], [45, 0, -60], [45, 45, -40]],
            [[45, 45, -65], [5, 100, 10], [45, 0, -60], [45, 45, -40]],
            # return to stand
            [[45, 45, -50], [45, 0, -30], [45, 0, -50], [45, 45, -50]],
            [[45, 45, -50], [45, 0, -40], [45, 0, -50], [45, 45, -50]],
            [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
        ]

        for coord in coords:
            spider.do_step(coord, 52)


    def fighting(spider):
        ready = [
            # stand
            [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
            # fighting ready
            [[45, 45, -40], [45, 0, -40], [50, 20, -20], [45, 45, -50]],
            [[45, 45, -40], [45, 0, -40], [40, 20, -45], [45, 45, -50]],
            [[45, 45, -40], [45, 0, -40], [60, 40, -60], [45, 45, -40]],
            #
            [[45, 45, -40], [45, 30, -30], [60, 40, -60], [45, 45, -40]],
            [[45, 45, -30], [45, 30, -30], [60, 40, -60], [60, 40, -60]],
        ]

        twist_butt = [
            # twist butt
            [[55, 7, -30], [19, 48, -30], [77, 12, -60], [36, 63, -60]],
            [[19, 48, -30], [55, 7, -30], [36, 63, -60], [77, 12, -60]],
            #
            [[55, 7, -30], [19, 48, -30], [77, 12, -60], [36, 63, -60]],
            [[19, 48, -30], [55, 7, -30], [36, 63, -60], [77, 12, -60]],
            #
            [[40, 30, -30], [40, 30, -30], [60, 40, -60], [60, 40, -60]],
            # shrink
            [[40, 50, -30], [40, 50, -30], [60, 20, -60], [60, 20, -60]],
        ]

        pounce_bite = [
            [[40, 40, -60], [20, 60, 110], [60, 60, -60], [60, 60, -60]],
            [[40, 40, -40], [20, 30, -40], [60, 60, -60], [60, 60, -60]],
            [[20, 60, 110], [20, 30, -60], [60, 60, -60], [60, 60, -60]],
            [[20, 30, -40], [20, 30, -40], [60, 60, -60], [60, 60, -60]],
        ]

        return_stand = [
            [[45, 45, -50], [45, 0, -30], [45, 0, -50], [45, 45, -50]],
            [[45, 45, -50], [45, 0, -40], [45, 0, -50], [45, 45, -50]],
            [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
        ]

        for coord in ready:
            spider.do_step(coord, 50)
        for coord in twist_butt:
            spider.do_step(coord, 52)
        sleep(0.2)
        for coord in pounce_bite:
            spider.do_step(coord, 40)
            sleep(0.1)
        sleep(1)
        for coord in return_stand:
            spider.do_step(coord, 52)


    def excited(spider):
        coords = [
            # stand
            [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
            #
            [[45, 45, -30], [45, 0, -30], [45, 0, -30], [45, 45, -30]],
            [[45, 45, -80], [45, 0, -80], [45, 0, -80], [45, 45, -80]],
            [[45, 45, -30], [45, 0, -30], [45, 0, -30], [45, 45, -30]],
            [[45, 45, -80], [45, 0, -80], [45, 0, -80], [45, 45, -80]],
            [[45, 45, -30], [45, 0, -30], [45, 0, -30], [45, 45, -30]],
            [[45, 45, -80], [45, 0, -80], [45, 0, -80], [45, 45, -80]],
            #
            [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
        ]
        for coord in coords:
            spider.do_step(coord, 40)
            sleep(0.08)


    def play_dead(spider):
        sit = [
            # stand
            [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
            #
            [[45, 45, -10], [45, 0, -10], [45, 0, -10], [45, 45, -10]],
        ]

        play_dead = [
            [[45, 45, 100], [45, 45, 100], [45, 45, 100], [45, 45, 100]],
            #
            [[45, 35, 60], [35, 45, 80], [35, 45, 80], [45, 35, 60]],
            [[35, 45, 80], [45, 35, 60], [45, 35, 60], [35, 45, 80]],
            [[45, 35, 60], [35, 45, 80], [35, 45, 80], [45, 35, 60]],
            [[35, 45, 80], [45, 35, 60], [45, 35, 60], [35, 45, 80]],
            [[45, 35, 60], [35, 45, 80], [35, 45, 80], [45, 35, 60]],
            [[35, 45, 80], [45, 35, 60], [45, 35, 60], [35, 45, 80]],
            [[45, 35, 60], [35, 45, 80], [35, 45, 80], [45, 35, 60]],
            [[35, 45, 80], [45, 35, 60], [45, 35, 60], [35, 45, 80]],
            [[45, 35, 60], [35, 45, 80], [35, 45, 80], [45, 35, 60]],
            [[35, 45, 80], [45, 35, 60], [45, 35, 60], [35, 45, 80]],
            #
            [[45, 45, 100], [45, 45, 100], [45, 45, 100], [45, 45, 100]],
        ]

        return_stand = [
            [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
        ]

        for coord in sit:
            spider.do_step(coord, 60)
        for coord in play_dead:
            spider.do_step(coord, 55)
        for coord in return_stand:
            spider.do_step(coord, 60)


    def nod(spider):
        stand = [
            # stand
            [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
        ]

        nod = [
            [[45, 45, -80], [45, 0, -50], [45, 0, -20], [45, 45, -30]],
            [[45, 45, -20], [45, 0, -36], [45, 20, -52], [40, 20, -80]],
            [[45, 45, -80], [45, 0, -50], [45, 0, -20], [45, 45, -30]],
            [[45, 45, -20], [45, 0, -36], [45, 20, -52], [40, 20, -80]],
            [[45, 45, -80], [45, 0, -50], [45, 0, -20], [45, 45, -30]],
        ]

        return_stand = [
            [[45, 45, -80], [45, 0, -50], [45, 0, -40], [45, 45, -40]],
            [[45, 45, -60], [45, 0, -50], [45, 0, -40], [45, 45, -40]],
            [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
        ]

        for coord in stand:
            spider.do_step(coord, 60)
        for coord in nod:
            spider.do_step(coord, 45)
        sleep(.2)
        for coord in return_stand:
            spider.do_step(coord, 50)
        sleep(1)


    def shake_head(spider):
        ready = [
            # stand
            [[45, 45, -50], [45, 0, -50], [45, 20, -50], [45, 45, -50]],
            [[45, 45, -50], [45, 20, -30], [45, 20, -50], [45, 45, -50]],
            [[45, 45, -50], [45, 45, -50], [45, 20, -50], [45, 45, -50]],
        ]

        twist_butt = [
            # twist butt
            [[55, 7, -50], [19, 48, -50], [77, 12, -50], [36, 63, -50]],
            [[19, 48, -50], [55, 7, -50], [36, 63, -50], [77, 12, -50]],
            #
            [[51, 15, -50], [27, 43, -50], [72, 22, -50], [45, 56, -50]],
            [[27, 43, -50], [51, 15, -50], [45, 56, -50], [72, 22, -50]],
            #
            [[45, 45, -50], [45, 45, -50], [45, 45, -50], [45, 45, -50]],
        ]

        return_stand = [
            [[45, 45, -50], [45, 20, -30], [45, 0, -50], [45, 45, -50]],
            [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
        ]

        for coord in ready:
            spider.do_step(coord, 50)
        for coord in twist_butt:
            spider.do_step(coord, 58)
        sleep(.5)
        for coord in return_stand:
            spider.do_step(coord, 52)


    def look_left(spider):
        stand = [
            [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
        ]

        look_left = [
            [[45, 0, -50], [45, 45, -50], [45, 45, -50], [45, 0, -50]],
            [[0, 45, -50], [45, 45, -50], [45, 45, -50], [45, 0, -50]],
            [[0, 45, -50], [45, 45, -35], [45, 45, -50], [45, 0, -50]],
            [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
        ]

        for coord in stand:
            spider.do_step(coord, 50)
        for coord in look_left:
            spider.do_step(coord, 50)


    def look_right(spider):
        stand = [
            [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
        ]

        look_right = [
            [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
            [[45, 45, -50], [0, 45, -50], [45, 0, -50], [45, 45, -50]],
            [[45, 45, -35], [0, 45, -50], [45, 0, -50], [45, 45, -50]],
            [[45, 0, -50], [45, 45, -50], [45, 45, -50], [45, 0, -50]],
        ]

        for coord in stand:
            spider.do_step(coord, 50)
        for coord in look_right:
            spider.do_step(coord, 50)


    def warm_up(spider):
        stand = [
            [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
            [[45, 45, -50], [45, 45, -50], [45, 45, -50], [45, 45, -50]],
        ]

        left_right = [
            [[45, 37, -85], [45, 37, -14], [45, 37, -14], [45, 37, -85]],
            [[45, 45, -50], [45, 45, -50], [45, 45, -50], [45, 45, -50]],
            [[45, 37, -85], [45, 37, -14], [45, 37, -14], [45, 37, -85]],
            [[45, 45, -50], [45, 45, -50], [45, 45, -50], [45, 45, -50]],
            #
            [[45, 37, -14], [45, 37, -85], [45, 37, -85], [45, 37, -14]],
            [[45, 45, -50], [45, 45, -50], [45, 45, -50], [45, 45, -50]],
            [[45, 37, -14], [45, 37, -85], [45, 37, -85], [45, 37, -14]],
            [[45, 45, -50], [45, 45, -50], [45, 45, -50], [45, 45, -50]],
        ]

        clockwise = []
        clockwise.append(spider.move_list.move_body_absolute(0, 25, 10))
        clockwise.append(spider.move_list.move_body_absolute(12.5, 21.65, 10))
        clockwise.append(spider.move_list.move_body_absolute(21.65, 12.5, 10))
        clockwise.append(spider.move_list.move_body_absolute(25, 0, 10))
        clockwise.append(spider.move_list.move_body_absolute(21.65, -12.5, 10))
        clockwise.append(spider.move_list.move_body_absolute(12.5, -21.65, 10))
        clockwise.append(spider.move_list.move_body_absolute(0, -25, 10))
        clockwise.append(spider.move_list.move_body_absolute(-12.5, -21.65, 10))
        clockwise.append(spider.move_list.move_body_absolute(-21.65, -12.5, 10))
        clockwise.append(spider.move_list.move_body_absolute(-25, 0, 10))
        clockwise.append(spider.move_list.move_body_absolute(-21.65, 12.5, 10))
        clockwise.append(spider.move_list.move_body_absolute(-12.5, 21.65, 10))
        clockwise.append(spider.move_list.move_body_absolute(0, 25, 10))

        anticlockwise = []
        anticlockwise.append(spider.move_list.move_body_absolute(0, 25, 10))
        anticlockwise.append(spider.move_list.move_body_absolute(-12.5, 21.65, 10))
        anticlockwise.append(spider.move_list.move_body_absolute(-21.65, 12.5, 10))
        anticlockwise.append(spider.move_list.move_body_absolute(-25, 0, 10))
        anticlockwise.append(spider.move_list.move_body_absolute(-21.65, -12.5, 10))
        anticlockwise.append(spider.move_list.move_body_absolute(-12.5, -21.65, 10))
        anticlockwise.append(spider.move_list.move_body_absolute(0, -25, 10))
        anticlockwise.append(spider.move_list.move_body_absolute(12.5, -21.65, 10))
        anticlockwise.append(spider.move_list.move_body_absolute(21.65, -12.5, 10))
        anticlockwise.append(spider.move_list.move_body_absolute(25, 0, 10))
        anticlockwise.append(spider.move_list.move_body_absolute(21.65, 12.5, 10))
        anticlockwise.append(spider.move_list.move_body_absolute(12.5, 21.65, 10))
        anticlockwise.append(spider.move_list.move_body_absolute(0, 25, 10))

        return_stand = [
            [[45, 45, -50], [45, 45, -40], [45, 0, -50], [45, 45, -50]],
            [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
        ]

        for coord in stand:
            spider.do_step(coord, 50)
        sleep(0.5)
        for coord in left_right:
            spider.do_step(coord, 48)
        sleep(.3)
        for coord in clockwise:
            spider.do_step(coord, 58)
        sleep(.3)
        for coord in anticlockwise:
            spider.do_step(coord, 58)
        sleep(.3)
        for coord in return_stand:
            spider.do_step(coord, 50)


    def push_up(spider):
        ready = [
            # stand
            [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
            #
            [[60, 10, -60], [60, 0, -60], [20, 60, 10], [10, 65, -40]],
            [[70, 0, -76], [70, 0, -76], [0, 130, -40], [0, 130, -40]],
        ]

        push_up = [
            [[70, 0, -40], [70, 0, -40], [0, 130, -40], [0, 130, -40]],
            [[70, 0, -76], [70, 0, -76], [0, 130, -40], [0, 130, -40]],
            [[70, 0, -40], [70, 0, -40], [0, 130, -40], [0, 130, -40]],
            [[70, 0, -76], [70, 0, -76], [0, 130, -40], [0, 130, -40]],
            [[70, 0, -40], [70, 0, -40], [0, 130, -40], [0, 130, -40]],
            [[70, 0, -76], [70, 0, -76], [0, 130, -40], [0, 130, -40]],
        ]

        for coord in ready:
            spider.do_step(coord,70)
        for coord in push_up:
            spider.do_step(coord, 35)
            sleep(0.1)


    actions_dict = {
        "sit": sit,
        "stand": stand,
        "wave_hand": wave_hand,
        "shake_hand": shake_hand,
        "fighting": fighting,
        "excited": excited,
        "play_dead": play_dead,
        "nod": nod,
        "shake_head": shake_head,
        "look_left": look_left,
        "look_right": look_right,
        "look_up": look_up,
        "look_down": look_down,
        "warm_up": warm_up,
        "push_up": push_up,
    }


    sounds_dict = {

    }

    if __name__ == "__main__":
        from picrawler import Picrawler

        my_spider = Picrawler()

        actions = list(actions_dict.keys())
        for i, key in enumerate(actions):
            print(f'{i} {key}')

        last_key = None

        try:
            while True:
                key = input()

                if key == '':
                    print(actions[last_key])
                    actions_dict[actions[last_key]](my_spider)
                else:
                    key = int(key)
                    if key > (len(actions) - 1):
                        print("無効なキー")
                    else:
                        last_key = key
                        print(actions[key])
                        actions_dict[actions[key]](my_spider)

        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f'Error:\n {e}')
        finally:
            my_spider.do_action("sit", speed=40)
            sleep(.1)


**仕組み**

#. プログラム開始時に利用可能なアクションの辞書を構築し、番号付きメニューを
   表示します。

   .. code-block:: python

      actions_dict = {"sit": sit, "stand": stand, ...}
      for i, key in enumerate(actions): print(f'{i} {key}')

#. 対話型メニューループ — 番号を入力してアクション選択・実行、**Enter** で
   直前のアクションを繰り返し、**Ctrl+C** で終了。

#. 座標ステップとは？ — 各ポーズは ``[[x, y, z], ...]`` 形式の 4 脚座標
   リストで定義。右前脚(0)、左前脚(1)、左後脚(2)、右後脚(3)。X=前後、
   Y=左右、Z=上下（より負で高い）。

#. ポーズシーケンスの再生 — ``do_step()`` がサーボを現在のポーズから目標
   ポーズへ滑らかに補間。速度パラメータは 40（遅い）〜 80（速い）。

#. 組み込み vs カスタムアクション — ``do_action()`` は組み込みアクションを
   使用、``do_step()`` で手動ポーズ構築。

#. 遅延の追加 — ``sleep()`` で動作フェーズ間に一時停止を挿入。各フェーズが
   視覚的に完了してから次に進みます。

#. ``move_body_absolute()`` による円運動 — サイン/コサイン値で円上の点を
   ステップ実行し、円形のボディスウェイを実行。

#. 安全な終了 — ``finally`` ブロックでプログラムの終了方法に関わらずロボット
   が安全な座位に戻ります。
