.. _picrawler_skill:

.. start_using_picrawler

21. OpenClaw で PiCrawler を操作する
========================================


**OpenClaw とは？**

ChatGPT のアップグレード版と考えてください。従来のチャットボットは話すこと (テキスト生成) しかできませんが、OpenClaw はアクションを起こせます。あなたの自然言語の指示を理解し、コマンドの実行、ファイルの管理、さまざまなツールの呼び出しなど、コンピュータ上で実際に操作を実行できます。

以下は素晴らしい応用シナリオです：

* **個人オールラウンドアシスタント:** スケジュール管理、リマインダー設定、タスク追跡を任せられます。チャットアプリ (Telegram、WhatsApp など) で伝えるだけで、記憶して実行します。
* **自動化「接着剤」:** さまざまなサービスをつなぐバインダーとして機能します。例えば、ウェブサイトの価格変動を監視させることができます。値下げが検出されると、自動的に n8n 自動化ワークフローを起動してメール通知を送信します。
* **専任開発アシスタント:** サーバー管理、スクリプト実行、ログ確認を手伝わせられます。「システム負荷を確認して」と言うだけで、サーバーに SSH 接続し、コマンドを実行して結果を返します。
* **ハードウェア「プレイメイト」:** これは非常に興味深いユースケースです。Raspberry Pi に接続されたハードウェアを OpenClaw に制御させることができます。例えば、ある開発者は機械式アーム付きのロボット掃除機の制御に使用したり、レーシングシミュレータのデータを分析して LED スクリーンに表示させたりしました。Raspberry Pi の公式チームも、会話だけでコードを一行も書かずに結婚式用の自動フォトブースを構築しました！


.. important::

   Raspberry Pi Zero 2W は RAM が 512MB しかなく、OpenClaw は最低 1GB を必要とします。そのため、正常に動作しません。Raspberry Pi 4/5 以上を推奨します。

OpenClaw クイックスタート
------------------------------

できるだけ早く OpenClaw のパワーを体験したい場合は、この方法を使用してください。自動的にインストールされ、インタラクティブなセットアップウィザードが起動します。

1.  Raspberry Pi のターミナルを開き、以下のコマンドを直接実行します。このコマンドは公式ウェブサイトからインストールスクリプトをダウンロードして実行します：

    .. code-block:: bash

       curl -fsSL https://openclaw.ai/install.sh | bash

    .. note:: 新しいバージョンが急速に更新されるため、インストール手順が若干異なる場合があります。

2.  スクリプトが自動的に OpenClaw をダウンロードしてインストールします。

    .. image:: /img/openclaw/install_open_claw.png


3.  次に、OpenClaw を信頼するかどうかを確認するセキュリティプロンプトが表示されます。安全で信頼できることを確認したら、矢印キーで「Yes」に移動し、Enter を押します。

    .. image:: /img/openclaw/security_open_claw.png


4.  Quick Start を選択し、Enter を押します。

    .. image:: /img/openclaw/quickstart_open_claw.png

5.  モデルを選択し、Enter を押します。ここでは例として OpenAI を使用します。

    .. image:: /img/openclaw/model_provider_open_claw.png

6.  OpenAI API Key を選択します。

    .. image:: /img/openclaw/api_key_open_claw.png

7.  今すぐ API キーを貼り付けます。

    .. image:: /img/openclaw/paste_api_key_open_claw.png

8.  |link_openai_platform| にアクセスしてログインします。**API keys** ページで **Create new secret key** をクリックします。

    .. image:: /img/openclaw/llm_openai_create.png

9.  詳細 (Owner, Name, Project, 権限) を入力し、**Create secret key** をクリックします。

    .. image:: /img/openclaw/llm_openai_create_confirm.png

10. キーが作成されたらすぐにコピーしてください — 再度表示することはできません。紛失した場合は新しいキーを生成する必要があります。

    .. image:: /img/openclaw/llm_openai_copy.png

11. OpenClaw の設定にキーを貼り付けます。

    .. image:: /img/openclaw/paste_api_key_enter_open_claw.png

12. 使用するモデルを選択します。この例では **Keep current** を使用します。

    .. image:: /img/openclaw/model_config_open_claw.png

13. 次はチャンネル選択です。チャンネルとは、Telegram、WhatsApp、Discord など OpenClaw がサポートする通信サービスを指します。下矢印キーで「Skip for now」オプションを選択し、Enter を押します。

    .. image:: /img/openclaw/channel_open_claw.png

14. 次に、すぐにスキルを設定するよう促されます。「Yes」を選択して Enter を押します。

    .. image:: /img/openclaw/config_skill_open_claw.png

15. 必要なスキルをインストールします。以下の例では「Skip for now」オプションを選択し（スペースキーで選択）、Enter を押します。

    .. image:: /img/openclaw/install_skill_open_claw.png


16. 次は Hooks です。「command-logger」と「session-memory」をチェックします。

    .. image:: /img/openclaw/hooks2_open_claw.png


17. インストールが完了しました。「Hatch in TUI」を選択して Enter を押すと OpenClaw を起動できます。

   .. image:: /img/openclaw/hatch_open_claw.png


.. note::

   以下のコマンドを入力して OpenClaw を起動できます：

    .. code-block:: bash

       openclaw tui

   ctrl+c を 2 回押して TUI インターフェースを終了できます。

------------------------------------------------------------------------

OpenClaw で PiCrawler を操作する
----------------------------------------------

**PiCrawler スキルとは？**

PiCrawler スキルは OpenClaw の拡張機能で、自然言語を通じて SunFounder PiCrawler ロボットスパイダーを制御できるようにします。Python スクリプトを書いたり座標値を覚えたりする代わりに、「立って」「前に 3 歩進んで」「前方に障害物があるか確認して」のように PiCrawler にやってほしいことを OpenClaw に伝えるだけで、OpenClaw が適切な Python コードを自動的に実行します。

PiCrawler スキルでできること：

* **基本動作:** 前進、後退、左折/右折、小角度旋回
* **ポーズ:** 立つ、座る
* **表現力豊かなアクション:** 前脚を振る、ダンス、腕立て伏せ、さまざまな方向を見る
* **センサー:** 超音波距離センサーで障害物を検出
* **サウンド:** ロボットのスピーカーで効果音や音楽を再生
* **カメラビジョン:** 写真撮影、顔検出、色追跡、QR コードやジェスチャーの認識

----------------------------------------------------------------

前提条件
------------------------------

OpenClaw で PiCrawler スキルを使用する前に、以下を確認してください：

1. **PiCrawler** が適切に組み立てられ、Raspberry Pi に接続されていること
2. **OpenClaw** がインストールされ、実行中であること
3. 以下の Python ライブラリがインストールされていること：

   - ``picrawler``
   - ``robot_hat``
   - ``vilib``

以下のコマンドでインストールを確認できます：

.. code-block:: bash

   python3 -c "import picrawler"

このコマンドがエラーなしで実行されれば、準備完了です。

----------------------------------------------------------------

PiCrawler スキルのインストール
------------------------------

以下の手順に従って、OpenClaw 用の PiCrawler スキルをインストールします：

1. **PiCrawler スキルファイルをコピー** して OpenClaw のスキルディレクトリに配置します：

   .. code-block:: bash

      cp -r ~/picrawler/picrawler-control ~/.openclaw/workspace/skills/

2. スキルファイルをチェックして **インストールを確認** します：

   .. code-block:: bash

      ls ~/.openclaw/workspace/skills/picrawler-control/

   出力には ``SKILL.md``、``install.sh``、``scripts/``、``references/`` が表示されるはずです。

このスキルの ``SKILL.md`` ファイルには、OpenClaw が必要とするすべての指示 — 安全ルール、各機能のコードテンプレート、自然言語リクエストから Python コードへのマッピング — が含まれています。OpenClaw はこのファイルを読み取り、PiCrawler 上で実行するコードを決定するために使用します。

----------------------------------------------------------------

CLI からの PiCrawler スキルのテスト
----------------------------------------------

OpenClaw でスキルを使用する前に、付属の CLI ツールを使用してターミナルから直接基本機能をテストすることをお勧めします。

**超音波距離の確認:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picrawler-control/scripts/pc.py sensor distance

**PiCrawler を座らせる:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picrawler-control/scripts/pc.py pose sit --speed 40

**PiCrawler を立たせる:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picrawler-control/scripts/pc.py pose stand --speed 40

**前進:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picrawler-control/scripts/pc.py move forward --steps 2 --speed 60

**左折:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picrawler-control/scripts/pc.py move "turn left" --steps 1 --speed 60

**効果音の再生:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picrawler-control/scripts/pc.py sound play ~/picrawler/examples/sounds/talk1.wav --volume 80

----------------------------------------------------------------

OpenClaw で PiCrawler スキルを使用する
----------------------------------------------------

PiCrawler スキルがコマンドラインから動作することを確認したら、OpenClaw 内で使用を開始できます。

1. **OpenClaw TUI を起動**:

   .. code-block:: bash

      openclaw tui

2. **自然言語コマンドを送信** して PiCrawler を制御します。以下は例です：

   * 「立って」
   * 「座って」
   * 「前に 3 歩進んで」
   * 「左に曲がって」
   * 「ダンスをして」
   * 「腕立て伏せをして」
   * 「前脚を振って」
   * 「左を見て」
   * 「前に何があるか確認して」
   * 「写真を撮って」
   * 「顔を検出して / こっちを見て」
   * 「赤い色を探して」

3. **OpenClaw が自動的に** あなたのリクエストを適切な Python コードに変換し、PiCrawler 上で実行します。移動コマンドの場合、スキルは常にロボットが最初に立ち上がり、アクション完了後に座ることを保証します。

----------------------------------------------------------------

利用可能なアクションとコマンド
-------------------------------------------

PiCrawler スキルがサポートする機能の完全なリストは以下の通りです：

移動 (``pc.py move``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - アクション
     - 説明
   * - ``forward``
     - 前進
   * - ``backward``
     - 後退
   * - ``turn left``
     - その場で左に旋回
   * - ``turn right``
     - その場で右に旋回
   * - ``turn left angle``
     - 小角度の左旋回
   * - ``turn right angle``
     - 小角度の右旋回

ポーズ (``pc.py pose``)
^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - ポーズ
     - 説明
   * - ``stand``
     - 座った状態から立ち上がる
   * - ``sit``
     - 立った状態から座る

追加アクション (自然言語 / exec 経由)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - アクション
     - 説明
   * - ``dance``
     - ダンスモーションを実行
   * - ``push_up``
     - 腕立て伏せモーション
   * - ``wave``
     - 前脚を振る
   * - ``look_left``
     - 体を左に向ける
   * - ``look_right``
     - 体を右に向ける
   * - ``look_up``
     - 体を上に傾ける
   * - ``look_down``
     - 体を下に傾ける

センサー
^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - コマンド
     - 説明
   * - ``sensor distance``
     - 超音波距離センサーを読み取る (cm を返す)

サウンド (``pc.py sound``)
^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - コマンド
     - 説明
   * - ``sound play <file>``
     - 効果音ファイルを再生
   * - ``sound music <file>``
     - BGM を再生
   * - ``sound volume <0-100>``
     - スピーカー音量を設定
   * - ``sound stop``
     - 再生を停止

カメラ & ビジョン (自然言語 / exec 経由)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - 機能
     - 説明
   * - 写真撮影
     - 写真を ``~/Pictures/`` に保存
   * - 顔検出
     - 人の顔を検出し位置を報告
   * - 色検出
     - 色 (赤、青、緑など) で物体を特定
   * - ジェスチャー認識
     - グー/チョキ/パーのジェスチャーを認識
   * - 交通標識検出
     - 停止/左/右/前進の標識を認識
   * - QR コードスキャン
     - QR コードのデータと位置を読み取る

----------------------------------------------------------------

トラブルシューティング
------------------------------

OpenClaw の問題
^^^^^^^^^^^^^^^^^^^^^^^^

Q. インストール中に ``Error: systemctl is-enabled unavailable: Command failed: systemctl --user is-enabled openclaw-gateway.service`` というエラーが表示されます。どうすればいいですか？

   今は無視して構いませんが、次の手順で問題が発生する可能性があります。その際は一つずつ参照してください。


Q. ``openclaw tui`` を実行すると ``-bash: openclaw: command not found`` というエラーが表示されます。どうすればいいですか？

   以下のコマンドを実行してください：

   .. code-block:: bash

      echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.bashrc
      source ~/.bashrc

   これで ``openclaw tui`` で TUI インターフェースを起動できるはずです。



Q. ``openclaw tui`` で ``not connected to gateway — message not sent`` または ``gateway disconnected: closed`` というメッセージが表示されます。

   これは OpenClaw Gateway サービスが起動していないためです。別のターミナルを開き、以下のコマンドを実行して OpenClaw Gateway を起動してください：

   .. code-block:: bash

      openclaw gateway

   その後 ``openclaw tui`` を再起動すれば、直接使用できます。


Q. OpenClaw Gateway サービスをバックグラウンドで実行 / 起動時に自動起動するように設定したいのですが、どうすればいいですか？

   通常、OpenClaw Gateway サービスは起動時に自動的に開始されるはずです。開始されない場合は、以下のコマンドで手動で起動できます。

   1. ``~/.config/systemd/user`` ディレクトリを作成します：

   .. code-block:: bash

      mkdir -p ~/.config/systemd/user


   2. ``openclaw-gateway.service`` ファイルを作成します：

   .. code-block:: bash

      cat > ~/.config/systemd/user/openclaw-gateway.service << EOF
      [Unit]
      Description=OpenClaw Gateway
      After=network.target

      [Service]
      Type=simple
      ExecStart=$HOME/.npm-global/bin/openclaw gateway run
      Restart=on-failure
      RestartSec=10
      Environment="PATH=$HOME/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin"
      Environment="NODE_ENV=production"

      [Install]
      WantedBy=default.target
      EOF


   3. systemd 設定をリロードします：

   .. code-block:: bash

      systemctl --user daemon-reload

   4. サービスを起動します：

   .. code-block:: bash

      systemctl --user start openclaw-gateway

   この時点で ``openclaw tui`` を再起動すれば、直接使用できます。

   5. 起動時に自動起動するように有効化します：

   .. code-block:: bash

      systemctl --user enable openclaw-gateway


Q. OpenClaw がシステムを操作できません。どうすればいいですか？

   新しくインストールした OpenClaw は、デフォルトでは Raspberry Pi システムを操作する権限がない場合があり、チャットしかできません。手動で権限を設定する必要があります。

   1.  OpenClaw 設定ファイルを開きます：

      .. code-block:: bash

         nano ~/.openclaw/openclaw.json

   2.  ``tools`` オプションを見つけ、以下のように ``profile`` と ``exec`` を変更します。

      .. code-block:: json

        "tools": {
            "profile": "coding",
            "exec": {
                "secrity": "full"
            }
        },

   3.  保存して終了します。

   4.  ターミナルで以下のコマンドを入力して OpenClaw Gateway を再起動します：

      .. code-block:: bash

         openclaw gateway restart

   これで OpenClaw は読み取りと書き込みの権限を持ち、Raspberry Pi システムを操作できるようになります。

PiCrawler の問題
^^^^^^^^^^^^^^^^^^^^^^^^


Q. PiCrawler がコマンドに応答しません。どうすればいいですか？

   まず、PiCrawler が適切に接続され電源が入っていることを確認してください。次に基本機能をテストします：

   .. code-block:: bash

      python3 ~/.openclaw/workspace/skills/picrawler-control/scripts/pc.py pose sit --speed 40

   これが失敗する場合は、必要な Python ライブラリがインストールされていることを確認してください：

   .. code-block:: bash

      python3 -c "import picrawler; import robot_hat; import vilib"

Q. ``import picrawler`` テストが失敗します。

   これは PiCrawler Python ライブラリが正しくインストールされていないことを意味します。PiCrawler 公式インストールガイドを参照して必要なライブラリをインストールしてください。付属のインストールスクリプトを実行することもできます：

   .. code-block:: bash

      bash ~/.openclaw/workspace/skills/picrawler-control/install.sh

Q. OpenClaw が PiCrawler スキルを認識しません。

   TUI で *「スキルを再同期してください」* と言って OpenClaw にスキルの同期を促すか、OpenClaw ゲートウェイを再起動します：

   .. code-block:: bash

      openclaw gateway restart

Q. PiCrawler の動きが不安定またはぎこちなく感じます。

   これは通常、速度が高すぎるか、前のアクションの完了を待たずに実行したことが原因です。スキルは安全ルール (移動前に立つ、移動後に座る) を強制し、推奨速度範囲を提案します。速度パラメータを下げる (例: ``--speed 40`` を使用) か、連続するコマンド間に短い遅延を追加してみてください。

----------------------------------------------------------------

.. end_using_picrawler
