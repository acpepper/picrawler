.. _picrawler_skill:

.. start_using_picrawler

21. Using OpenClaw to Control PiCrawler
========================================


**What is OpenClaw?**

Think of it as an upgraded version of ChatGPT. While traditional chatbots can only talk (generate text), OpenClaw can take action. It understands your natural language instructions and can actually perform operations on your computer, such as running commands, managing files, and calling various tools.

Here are some fantastic application scenarios:

* **Personal All-around Assistant:** Let it help you manage your schedule, set reminders, and track tasks. You just need to tell it in a chat app (like Telegram, WhatsApp), and it will remember and execute.
* **Automation "Glue":** It can act as a binder for your various services. For example, you can have it monitor a website for price changes. Once a price drop is detected, it can automatically trigger an n8n automation workflow to send you an email notification.
* **Dedicated Development Assistant:** Have it help you manage servers, run scripts, and check logs. You can simply say, "Check the system load for me," and it can SSH into your server, execute the command, and return the results.
* **Hardware "Playmate":** This is a very interesting use case. You can have OpenClaw control hardware connected to a Raspberry Pi. For example, a developer used it to control a robotic vacuum cleaner with a mechanical arm, or even had it help analyze racing simulator data and display it on an LED screen. The official Raspberry Pi team even used it to build an automatic photo booth for a wedding, just through conversation, without writing a single line of code!


.. important::

   The Raspberry Pi Zero 2W has only 512MB of RAM, while OpenClaw requires a minimum of 1GB. Therefore, it cannot run properly. A Raspberry Pi 4/5 or higher is recommended.

Quick Start OpenClaw
------------------------------

If you want to experience the power of OpenClaw as quickly as possible, use this method. It will automatically install and launch an interactive setup wizard.

1.  Open the terminal on your Raspberry Pi and run the following command directly. This command downloads the installation script from the official website and executes it:

    .. code-block:: bash

       curl -fsSL https://openclaw.ai/install.sh | bash

    .. note:: Because new versions are updated rapidly, it's normal if your installation steps differ slightly.

2.  The script will automatically download and install OpenClaw.

    .. image:: /img/openclaw/install_open_claw.png


3.  You will then see a security prompt asking if you trust OpenClaw. Once you are sure it is safe and reliable, use the arrow keys to navigate to "Yes" and press Enter.

    .. image:: /img/openclaw/security_open_claw.png


4.  Select Quick Start, and then press Enter.

    .. image:: /img/openclaw/quickstart_open_claw.png

5.  Select your Model, and then press Enter. Here we use OpenAI as an example.

    .. image:: /img/openclaw/model_provider_open_claw.png

6.  Select OpenAI API Key.

    .. image:: /img/openclaw/api_key_open_claw.png

7.  Paste API key now.

    .. image:: /img/openclaw/paste_api_key_open_claw.png

.. |link_openai_platform| raw:: html

    <a href="https://platform.openai.com/settings/organization/api-keys" target="_blank">OpenAI Platform</a>

8.  Go to |link_openai_platform| and log in. On the **API keys** page, click **Create new secret key**.

    .. image:: /img/openclaw/llm_openai_create.png

9.  Fill in the details (Owner, Name, Project, and permissions if needed), then click **Create secret key**.

    .. image:: /img/openclaw/llm_openai_create_confirm.png

10. Once the key is created, copy it right away — you won't be able to see it again. If you lose it, you'll need to generate a new one.

    .. image:: /img/openclaw/llm_openai_copy.png

11. Paste the key into the OpenClaw configuration.

    .. image:: /img/openclaw/paste_api_key_enter_open_claw.png

12. Select the Model you want to use. In this example, we will use **Keep current**.

    .. image:: /img/openclaw/model_config_open_claw.png

13. Next is the channel selection. Channels refer to the communication services supported by OpenClaw, such as Telegram, WhatsApp, Discord, and more. Use the down arrow key to select the "Skip for now" option, then press Enter.

    .. image:: /img/openclaw/channel_open_claw.png

14. Next, you will be prompted to configure skills immediately. Select "Yes" and press Enter.

    .. image:: /img/openclaw/config_skill_open_claw.png

15. Install the skills you need. In the following example, we select the "Skip for now" option (press the spacebar to select), then press Enter.

    .. image:: /img/openclaw/install_skill_open_claw.png


16. Next are Hooks; we will check "command-logger" and "session-memory".

    .. image:: /img/openclaw/hooks2_open_claw.png


17. The installation is now complete. You can start OpenClaw by Selecting "Hatch in TUI" and pressing Enter.

   .. image:: /img/openclaw/hatch_open_claw.png


.. note::

   You can start OpenClaw by entering the following command:

    .. code-block:: bash

       openclaw tui

   And You can press ctrl+c twice to exit the tui interface.

------------------------------------------------------------------------

Making OpenClaw Operate the PiCrawler
----------------------------------------------

**What is PiCrawler Skill?**

PiCrawler Skill is an extension for OpenClaw that allows you to control your SunFounder PiCrawler robot spider through natural language. Instead of writing Python scripts or remembering coordinate values, you can simply tell OpenClaw what you want PiCrawler to do — like "stand up", "walk forward three steps", or "check if there's an obstacle ahead" — and OpenClaw will execute the appropriate Python code automatically.

Here are some things you can do with PiCrawler Skill:

* **Basic Movements:** Walk forward, backward, turn left/right, make small-angle turns
* **Poses:** Stand up, sit down
* **Expressive Actions:** Wave a front leg, dance, do push-ups, look in different directions
* **Sensors:** Read the ultrasonic distance sensor to detect obstacles
* **Sound:** Play sound effects and music through the robot's speaker
* **Camera Vision:** Take photos, detect faces, track colors, recognize QR codes and gestures

----------------------------------------------------------------

Prerequisites
------------------------------

Before you can use PiCrawler Skill with OpenClaw, make sure you have:

1. **PiCrawler** properly assembled and connected to your Raspberry Pi
2. **OpenClaw** installed and running
3. The following Python libraries installed:

   - ``picrawler``
   - ``robot_hat``
   - ``vilib``

You can verify the installation by running:

.. code-block:: bash

   python3 -c "import picrawler"

If this command runs without errors, you're ready to proceed.

----------------------------------------------------------------

Installing PiCrawler Skill
------------------------------

Follow these steps to install the PiCrawler Skill for OpenClaw:

1. **Copy the PiCrawler skill files** to the OpenClaw skills directory:

   .. code-block:: bash

      cp -r ~/picrawler/picrawler-control ~/.openclaw/workspace/skills/

2. **Verify the installation** by checking the skill files:

   .. code-block:: bash

      ls ~/.openclaw/workspace/skills/picrawler-control/

   You should see ``SKILL.md``, ``install.sh``, ``scripts/``, and ``references/`` in the output.

The skill's ``SKILL.md`` file contains all the instructions OpenClaw needs — safety rules, code templates for each capability, and a mapping from natural language requests to Python code. OpenClaw reads this file and uses it to decide what code to execute on your PiCrawler.

----------------------------------------------------------------

Testing PiCrawler Skill from the CLI
----------------------------------------------

Before using the skill with OpenClaw, you may want to test basic functionality directly from the terminal using the included CLI tool.

**Check ultrasonic distance:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picrawler-control/scripts/pc.py sensor distance

**Make PiCrawler sit:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picrawler-control/scripts/pc.py pose sit --speed 40

**Make PiCrawler stand:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picrawler-control/scripts/pc.py pose stand --speed 40

**Walk forward:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picrawler-control/scripts/pc.py move forward --steps 2 --speed 60

**Turn left:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picrawler-control/scripts/pc.py move "turn left" --steps 1 --speed 60

**Play a sound effect:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picrawler-control/scripts/pc.py sound play /home/pi/picrawler/examples/sounds/talk1.wav --volume 80

**Run servo calibration:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picrawler-control/scripts/pc.py calibrate

----------------------------------------------------------------

Using PiCrawler Skill in OpenClaw
----------------------------------------------------

Once you've verified that PiCrawler Skill works from the command line, you can start using it within OpenClaw.

1. **Launch OpenClaw TUI**:

   .. code-block:: bash

      openclaw tui

2. **Send natural language commands** to control PiCrawler. Here are some examples:

   * "Stand up"
   * "Sit down"
   * "Walk forward three steps"
   * "Turn left"
   * "Do a dance"
   * "Do some push-ups"
   * "Wave your front leg"
   * "Look to the left"
   * "Check if there's something ahead"
   * "Take a photo"
   * "Detect faces / look at me"
   * "Find the color red"

3. **OpenClaw will automatically** translate your request into the appropriate Python code and execute it on PiCrawler. For movement commands, the skill always ensures the robot stands first and sits down after completing the action.

----------------------------------------------------------------

Available Actions and Commands
-------------------------------------------

Here is the complete list of capabilities supported by PiCrawler Skill:

Movements (``pc.py move``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Action
     - Description
   * - ``forward``
     - Walk forward
   * - ``backward``
     - Walk backward
   * - ``turn left``
     - Pivot left in place
   * - ``turn right``
     - Pivot right in place
   * - ``turn left angle``
     - Small-angle turn left
   * - ``turn right angle``
     - Small-angle turn right

Poses (``pc.py pose``)
^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Pose
     - Description
   * - ``stand``
     - Stand up from sitting position
   * - ``sit``
     - Sit down from standing position

Additional Actions (via natural language / exec)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Action
     - Description
   * - ``dance``
     - Perform a dancing motion
   * - ``push_up``
     - Do push-up motions
   * - ``wave``
     - Wave a front leg
   * - ``look_left``
     - Turn body to look left
   * - ``look_right``
     - Turn body to look right
   * - ``look_up``
     - Tilt body to look up
   * - ``look_down``
     - Tilt body to look down

Sensors
^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Command
     - Description
   * - ``sensor distance``
     - Read ultrasonic distance sensor (returns cm)

Sound (``pc.py sound``)
^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Command
     - Description
   * - ``sound play <file>``
     - Play a sound effect file
   * - ``sound music <file>``
     - Play background music
   * - ``sound volume <0-100>``
     - Set speaker volume
   * - ``sound stop``
     - Stop playback

Camera & Vision (via natural language / exec)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Capability
     - Description
   * - Take photo
     - Capture and save a photo to ``~/Pictures/``
   * - Face detection
     - Detect human faces and report position
   * - Color detection
     - Locate objects by color (red, blue, green, etc.)
   * - Gesture recognition
     - Recognize rock/paper/scissor gestures
   * - Traffic sign detection
     - Recognize stop/left/right/forward signs
   * - QR code scanning
     - Read QR code data and position

----------------------------------------------------------------

Troubleshooting
------------------------------

OpenClaw Issues
^^^^^^^^^^^^^^^^^^^^^^^^

Q. During installation, I get the error ``Error: systemctl is-enabled unavailable: Command failed: systemctl --user is-enabled openclaw-gateway.service``. What should I do?

   You can ignore this for now, but you might encounter issues in the next steps. Please refer to them one by one at that time.


Q. When I run ``openclaw tui``, I get the error ``-bash: openclaw: command not found``. What should I do?

   Execute the following command:

   .. code-block:: bash

      echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.bashrc
      source ~/.bashrc

   You should now be able to start the tui interface with ``openclaw tui``.



Q. In ``openclaw tui``, I encounter ``not connected to gateway — message not sent`` or the message ``gateway disconnected: closed``.

   This is because your OpenClaw Gateway service is not started. Open another terminal and execute the following command to start the OpenClaw Gateway:

   .. code-block:: bash

      openclaw gateway

   Then restart ``openclaw tui``, and you can use it directly.


Q. I want to set the OpenClaw Gateway service to run in the background / start automatically on boot. How do I do that?

   Normally, your OpenClaw Gateway service should start automatically on boot. If it doesn't, you can manually start it with the following command.

   1. Create the ``~/.config/systemd/user`` directory:

   .. code-block:: bash

      mkdir -p ~/.config/systemd/user


   2. Create the ``openclaw-gateway.service`` file:

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


   3. Then reload the systemd configuration:

   .. code-block:: bash

      systemctl --user daemon-reload

   4. Start the service:

   .. code-block:: bash

      systemctl --user start openclaw-gateway

   At this point, restart ``openclaw tui``, and you can use it directly.

   5. Enable it to start on boot:

   .. code-block:: bash

      systemctl --user enable openclaw-gateway


Q. My OpenClaw can not operate the system, what should I do?

   A newly installed OpenClaw may not have permission to operate your Raspberry Pi system by default; it can only chat. We need to manually configure the permissions.

   1.  Open the OpenClaw configuration file:

      .. code-block:: bash

         nano ~/.openclaw/openclaw.json

   2.  Find the ``tools`` option and change the ``profile`` and ``exec`` as shown.

      .. code-block:: json

        "tools": {
            "profile": "coding",
            "exec": {
                "secrity": "full"
            }
        },

   3.  Save and exit.

   4.  Enter the following command in the terminal to restart the OpenClaw Gateway:

      .. code-block:: bash

         openclaw gateway restart

   Now, OpenClaw should have read and write permissions and be able to operate your Raspberry Pi system.

PiCrawler Issues
^^^^^^^^^^^^^^^^^^^^^^^^


Q. PiCrawler doesn't respond to commands. What should I do?

   First, verify that PiCrawler is properly connected and powered on. Then test basic functionality:

   .. code-block:: bash

      python3 ~/.openclaw/workspace/skills/picrawler-control/scripts/pc.py pose sit --speed 40

   If this fails, ensure the required Python libraries are installed:

   .. code-block:: bash

      python3 -c "import picrawler; import robot_hat; import vilib"

Q. The ``import picrawler`` test fails.

   This means the PiCrawler Python library is not properly installed. Please refer to the PiCrawler official installation guide to install the necessary libraries. You can also run the included install script:

   .. code-block:: bash

      bash ~/.openclaw/workspace/skills/picrawler-control/install.sh

Q. OpenClaw doesn't recognize the PiCrawler skill.

   Remind OpenClaw to sync the skills by saying in the TUI: *"Please rsync my skills"* or restart OpenClaw gateway:

   .. code-block:: bash

      openclaw gateway restart

Q. PiCrawler movements seem unstable or jerky.

   This is usually caused by executing actions at too high a speed or without allowing the previous action to complete. The skill enforces safety rules (stand before move, sit after move) and recommends speed ranges. Try reducing the speed parameter (e.g., use ``--speed 40``), or add short delays between consecutive commands.

----------------------------------------------------------------

.. end_using_picrawler
