.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 愛好者コミュニティへようこそ！ Raspberry Pi、Arduino、ESP32 について、他の愛好者と一緒に深く掘り下げて学びましょう。

    **参加する理由は？**

    - **専門的なサポート**: 購入後の問題や技術的な課題を、コミュニティやチームの助けを借りて解決できます。
    - **学びと共有**: スキルを高めるためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**: 新しい製品発表や先行プレビューに早期アクセスできます。
    - **特別割引**: 最新製品に対する独占的な割引を楽しめます。
    - **祝典プロモーションとプレゼント**: プレゼントキャンペーンや季節ごとのプロモーションに参加できます。

    👉 私たちと一緒に探求し、創造する準備はできましたか？ [|link_sf_facebook|] をクリックして、今すぐ参加しましょう！

.. _py_online_llm:

17. オンライン LLM への接続
================================

このレッスンでは、PiCrawler (または Raspberry Pi) をさまざまな
**オンライン大規模言語モデル (LLM)** に接続する方法を学びます。
各プロバイダーは API キーを必要とし、選択可能な異なるモデルを提供しています。

以下をカバーします：

* API キーを安全に作成・保存する方法。
* ニーズに合ったモデルの選び方。
* サンプルコードを実行してモデルと対話する方法。

各プロバイダーについて順を追って説明します。

----

事前準備
----------------

以下が完了していることを確認してください：

* :ref:`install_all_modules` — ``robot-hat``、``vilib``、``picrawler`` モジュールをインストールし、スクリプト ``i2samp.sh`` を実行します。


OpenAI
----------

OpenAI は **GPT-4o** や **GPT-4.1** などの強力なモデルを提供しており、
テキストとビジョンの両方のタスクに使用できます。

設定方法は次のとおりです：

**API キーの取得と保存**

#. |link_openai_platform| にアクセスしてログインします。**API keys** ページで **Create new secret key** をクリックします。

   .. image:: img/llm_openai_create.png

#. 詳細 (Owner, Name, Project, 権限) を入力し、**Create secret key** をクリックします。

   .. image:: img/llm_openai_create_confirm.png

#. キーが作成されたらすぐにコピーしてください — 再度表示することはできません。紛失した場合は新しいキーを生成する必要があります。

   .. image:: img/llm_openai_copy.png

#. プロジェクトフォルダ (例: ``/picrawler/examples``) に ``secret.py`` というファイルを作成します：

   .. code-block:: bash

       cd ~/picrawler/examples
       sudo nano secret.py

#. 以下のようにキーをファイルに貼り付けます：

   .. code-block:: python

       # secret.py
       # ここにシークレットを保存します。このファイルを Git にコミットしないでください。
       OPENAI_API_KEY = "sk-xxx"

**課金の有効化とモデルの確認**

#. キーを使用する前に、OpenAI アカウントの **Billing** ページに移動し、支払い情報を追加して少額のクレジットをチャージしてください。

   .. image:: img/llm_openai_billing.png

#. 次に **Limits** ページに移動し、アカウントで利用可能なモデルを確認し、コードで使用する正確なモデル ID をコピーします。

   .. image:: img/llm_openai_models.png

**サンプルコードでテスト**

#. サンプルコードを開きます：

   .. code-block:: bash

       cd ~/picrawler/examples
       sudo nano 18.online_llm_test.py

#. 内容を以下のコードに置き換え、``model="xxx"`` を使用したいモデル (例: ``gpt-4o``) に更新します：

   .. code-block:: python

       from picrawler.llm import OpenAI
       from secret import OPENAI_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = OpenAI(
           api_key=OPENAI_API_KEY,
           model="gpt-4o",
       )

   保存して終了します (``Ctrl+X``、``Y``、``Enter``)。

#. 最後に、テストを実行します：

   .. code-block:: bash

       sudo python3 18.online_llm_test.py


----

Gemini
------------------

Gemini は Google の AI モデルファミリーです。高速で汎用的なタスクに最適です。

**API キーの取得と保存**

#. |link_google_ai| にログインし、API Keys ページに移動します。

   .. image:: img/llm_gemini_get.png

#. 右上の **Create API key** ボタンをクリックします。

   .. image:: img/llm_gemini_create.png

#. 既存のプロジェクトまたは新しいプロジェクト用のキーを作成できます。

   .. image:: img/llm_gemini_choose.png

#. 生成された API キーをコピーします。

   .. image:: img/llm_gemini_copy.png

#. プロジェクトフォルダで：

   .. code-block:: bash

       cd ~/picrawler/examples
       sudo nano secret.py

#. キーを貼り付けます：

   .. code-block:: python

        # secret.py
        # ここにシークレットを保存します。このファイルを Git にコミットしないでください。
       GEMINI_API_KEY = "AIxxx"

**利用可能なモデルの確認**

公式の |link_gemini_model| ページにアクセスしてください。ここでモデルのリスト、正確な API ID、各モデルが最適化されているユースケースを確認できます。

   .. image:: img/llm_gemini_model.png

**サンプルコードでテスト**

#. テストファイルを開きます：

   .. code-block:: bash

       cd ~/picrawler/examples
       sudo nano 18.online_llm_test.py

#. 内容を以下のコードに置き換え、``model="xxx"`` を使用したいモデル (例: ``gemini-2.5-flash``) に更新します：

   .. code-block:: python

       from picrawler.llm import Gemini
       from secret import GEMINI_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = Gemini(
           api_key=GEMINI_API_KEY,
           model="gemini-2.5-flash",
       )

#. 保存して実行します：

   .. code-block:: bash

       sudo python3 18.online_llm_test.py

----

Qwen
------------------

Qwen は、Alibaba Cloud が提供する大規模言語モデルとマルチモーダルモデルの
ファミリーです。これらのモデルはテキスト生成、推論、マルチモーダル理解
(画像分析など) をサポートしています。

**API キーの取得**

Qwen モデルを呼び出すには、**API キー** が必要です。
ほとんどの海外ユーザーは **DashScope International (Model Studio)** コンソールを
使用してください。中国本土のユーザーは **Bailian (百炼)** コンソールを代わりに
使用できます。

* **海外ユーザー向け**

  #. **Alibaba Cloud** の公式 |link_qwen_inter| ページにアクセスします。
  #. サインインするか、**Alibaba Cloud** アカウントを作成します。
  #. **Model Studio** に移動します (シンガポールまたは北京リージョンを選択)。

      * ページ上部に「Activate Now」プロンプトが表示された場合、クリックして Model Studio を有効化し、無料クォータを受け取ります (シンガポールのみ)。
      * 有効化は無料です — 無料クォータを使い切った後にのみ課金されます。
      * 有効化プロンプトが表示されない場合、サービスは既に有効です。

  #. **Key Management** ページに移動します。**API Key** タブで **Create API Key** をクリックします。
  #. 作成後、API キーをコピーして安全に保管してください。

    .. image:: img/llm_qwen_api_key.png
        :width: 800

  .. note::
     香港、マカオ、台湾のユーザーも **International (Model Studio)** オプションを選択してください。

* **中国本土ユーザー向け**

  中国本土にいる場合は、代わりに **Alibaba Cloud Bailian (百炼)** コンソールを使用できます：

  #. |link_aliyun| (百炼コンソール) にログインし、アカウント認証を完了します。
  #. **Create API Key** を選択します。モデルサービスが有効化されていないというプロンプトが表示された場合、**Activate** をクリックし、規約に同意して無料クォータを受け取ります。有効化後、**Create API Key** ボタンが有効になります。

     .. image:: img/llm_qwen_aliyun_create.png

  #. 再度 **Create API Key** をクリックし、アカウントを確認して **Confirm** をクリックします。

     .. image:: img/llm_qwen_aliyun_confirm.png

  #. 作成されたら、API キーをコピーします。

     .. image:: img/llm_qwen_aliyun_copy.png

**API キーの保存**

#. プロジェクトフォルダで：

   .. code-block:: bash

       cd ~/picrawler/examples
       sudo nano secret.py

#. 以下のようにキーを貼り付けます：

   .. code-block:: python

        # secret.py
        # ここにシークレットを保存します。このファイルを Git にコミットしないでください。

        QWEN_API_KEY = "sk-xxx"

**サンプルコードでテスト**

#. テストファイルを開きます：

   .. code-block:: bash

       cd ~/picrawler/examples
       sudo nano 18.online_llm_test.py

#. 内容を以下のコードに置き換え、``model="xxx"`` を使用したいモデル (例: ``qwen-plus``) に更新します：

   .. code-block:: python

      from picrawler.llm import Qwen
      from secret import QWEN_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = Qwen(
          api_key=QWEN_API_KEY,
          model="qwen-plus",
      )


#. 以下で実行します：

   .. code-block:: bash

       sudo python3 18.online_llm_test.py

Grok (xAI)
------------------
Grok は xAI の会話型 AI で、Elon Musk のチームによって開発されました。
xAI API を通じて接続できます。

**API キーの取得と保存**

#. |link_grok_ai| でアカウントを作成します。最初にアカウントにクレジットを追加してください — そうしないと API は動作しません。

#. API Keys ページに移動し、**Create API key** をクリックします。

   .. image:: img/llm_grok_create.png

#. キーの名前を入力し、**Create API key** をクリックします。

   .. image:: img/llm_grok_name.png

#. 生成されたキーをコピーして安全に保管します。

   .. image:: img/llm_grok_copy.png

#. プロジェクトフォルダで：

   .. code-block:: bash

       cd ~/picrawler/examples
       sudo nano secret.py

#. 以下のようにキーを貼り付けます：

   .. code-block:: python

        # secret.py
        # ここにシークレットを保存します。このファイルを Git にコミットしないでください。

        GROK_API_KEY = "xai-xxx"

**利用可能なモデルの確認**

xAI コンソールの Models ページに移動します。ここでチームが利用できるすべての
モデルとその正確な API ID を確認できます — コード内でこれらの ID を使用します。

   .. image:: img/llm_grok_model.png

**サンプルコードでテスト**

#. テストファイルを開きます：

   .. code-block:: bash

       cd ~/picrawler/examples
       sudo nano 18.online_llm_test.py

#. 内容を以下のコードに置き換え、``model="xxx"`` を使用したいモデル (例: ``grok-4-latest``) に更新します：

   .. code-block:: python

       from picrawler.llm import Grok
       from secret import GROK_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = Grok(
           api_key=GROK_API_KEY,
           model="grok-4-latest",
       )

#. 以下で実行します：

   .. code-block:: bash

       sudo python3 18.online_llm_test.py

----

DeepSeek
------------------

DeepSeek は、手頃な価格で高性能なモデルを提供する中国の LLM プロバイダーです。

**API キーの取得と保存**

#. |link_deepseek| にログインします。

#. 右上のメニューから **API Keys → Create API Key** を選択します。

   .. image:: img/llm_deepseek_create.png

#. 名前を入力し、**Create** をクリックしてキーをコピーします。

   .. image:: img/llm_deepseek_copy.png

#. プロジェクトフォルダで：

   .. code-block:: bash

       cd ~/picrawler/examples
       sudo nano secret.py

#. キーを追加します：

   .. code-block:: python

       # secret.py
       DEEPSEEK_API_KEY = "sk-xxx"

**課金の有効化**

最初にアカウントにチャージする必要があります。少額 (例: ¥10 RMB) から始めてください。

   .. image:: img/llm_deepseek_chognzhi.png

**利用可能なモデル**

執筆時点 (2025-09-12) で、DeepSeek は以下を提供しています：

* ``deepseek-chat``
* ``deepseek-reasoner``

**サンプルコードでテスト**

#. テストファイルを開きます：

   .. code-block:: bash

       cd ~/picrawler/examples
       sudo nano 18.online_llm_test.py

#. 内容を以下のコードに置き換え、``model="xxx"`` を使用したいモデル (例: ``deepseek-chat``) に更新します：

   .. code-block:: python

       from picrawler.llm import Deepseek
       from secret import DEEPSEEK_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = Deepseek(
           api_key=DEEPSEEK_API_KEY,
           model="deepseek-chat",
           max_messages=20,
       )

#. 実行：

   .. code-block:: bash

       sudo python3 18.online_llm_test.py

----

Doubao
------------------
Doubao は ByteDance の AI モデルプラットフォーム (Volcengine Ark) です。

**API キーの取得と保存**

#. |link_doubao| にログインします。

#. 左メニューで **API Key Management → Create API Key** に移動します。

   .. image:: img/llm_doubao_create.png

#. 名前を選択し、**Create** をクリックします。

   .. image:: img/llm_doubao_name.png

#. **Show API Key** アイコンをクリックしてコピーします。

   .. image:: img/llm_doubao_copy.png

#. プロジェクトフォルダで：

   .. code-block:: bash

       cd ~/picrawler/examples
       sudo nano secret.py

#. キーを追加します：

   .. code-block:: python

       # secret.py
       DOUBAO_API_KEY = "xxx"

**モデルの選択**

#. モデルマーケットプレイスに移動し、モデルを選択します。

   .. image:: img/llm_doubao_model_select.png

#. 例: **Doubao-seed-1.6** を選択し、**API 接入** をクリックします。

   .. image:: img/llm_doubao_model.png

#. API キーを選択し、**Use API** をクリックします。

   .. image:: img/llm_doubao_use_api.png

#. **Enable Model** をクリックします。

   .. image:: img/llm_doubao_kaitong.png

#. モデル ID にカーソルを合わせてコピーします。

   .. image:: img/llm_doubao_copy_id.png

**サンプルコードでテスト**

#. テストファイルを開きます：

   .. code-block:: bash

       cd ~/picrawler/examples
       sudo nano 18.online_llm_test.py

#. 内容を以下のコードに置き換え、``model="xxx"`` を使用したいモデル (例: ``doubao-seed-1-6-250615``) に更新します：

   .. code-block:: python

       from picrawler.llm import Doubao
       from secret import DOUBAO_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = Doubao(
           api_key=DOUBAO_API_KEY,
           model="doubao-seed-1-6-250615",
       )

#. 以下で実行します：

   .. code-block:: bash

       sudo python3 18.online_llm_test.py


一般
--------------

このプロジェクトは、統一されたインターフェースを通じて複数の LLM プラットフォームへの
接続をサポートしています。以下のプロバイダーにビルトイン対応しています：

* **OpenAI** (ChatGPT / GPT-4o, GPT-4, GPT-3.5)
* **Gemini** (Google AI Studio / Vertex AI)
* **Grok** (xAI)
* **DeepSeek**
* **Qwen (通义千问)**
* **Doubao (豆包)**

さらに、**OpenAI API 形式と互換性のある他のあらゆる LLM サービス**に接続できます。
これらのプラットフォームでは、**API キー**と正しい **base_url** を手動で取得する
必要があります。

**API キーの取得と保存**

#. 使用したいプラットフォームから **API キー** を取得します。(詳細は各プラットフォームの公式コンソールを参照してください。)

#. プロジェクトフォルダに新しいファイルを作成します：

   .. code-block:: bash

      cd ~/picrawler/examples
      nano secret.py

#. ``secret.py`` にキーを追加します：

   .. code-block:: python

      # secret.py
      API_KEY = "your_api_key_here"

.. warning::

   API キーは非公開にしてください。``secret.py`` を公開リポジトリにアップロードしないでください。

**サンプルコードでテスト**

#. テストファイルを開きます：

   .. code-block:: bash

      cd ~/picrawler/examples
      sudo nano 18.online_llm_test.py

#. Python ファイルの内容を以下の例に置き換え、プラットフォームの正しい ``base_url`` と ``model`` を入力してください：

   .. note::

      ``base_url`` について:
      **OpenAI API 形式**およびそれと**互換性のある** API をサポートしています。
      各プロバイダーには独自の ``base_url`` があります。ドキュメントを確認してください。

   .. code-block:: python

      from picrawler.llm import LLM
      from secret import API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = LLM(
          base_url="https://api.example.com/v1",  # プロバイダーの base_url を入力
          api_key=API_KEY,
          model="your-model-name-here",           # プロバイダーからモデルを選択
      )


#. プログラムを実行します：

   .. code-block:: bash

      python3 18.online_llm_test.py


