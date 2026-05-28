.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_stt:

15. STT (Speech-to-Text)
==============================================

This example demonstrates how to use the STT (Speech-to-Text) module on
PiCrawler. The robot listens to your voice through the onboard microphone
and converts it into text in real time.

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picrawler/examples
    sudo python3 15_stt.py

After running the program, you will see the language setting and a prompt.
The robot starts listening — speak into the microphone and the recognized
text will be printed to the terminal.

If no speech is detected, ``(no speech detected)`` is shown. Press **Ctrl+C**
to exit.

**Before You Start**

Make sure you’ve completed:

* :ref:`install_all_modules` — Install ``robot-hat``, ``vilib``, ``picrawler`` modules, then run the script ``i2samp.sh``.

**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you
    need to go to source code path like ``picrawler\examples``. After modifying
    the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    from robot_hat.stt import STT

    # Speech recognition demo using sunfounder_voice_assistant STT module
    # Press Ctrl+C to exit

    # Configure language: "en-us", "zh-cn", etc.
    LANGUAGE = "en-us"

    def main():
        print("=== PiCrawler Speech-to-Text Demo ===")
        print(f"Language: {LANGUAGE}")
        print("Press Ctrl+C to exit")
        print()

        stt = STT(language=LANGUAGE)

        try:
            while True:
                print("Listening... (speak now)")
                text = stt.listen()
                if text:
                    print(f">>> {text}")
                else:
                    print("(no speech detected)")
        except KeyboardInterrupt:
            print("\nExiting...")

    if __name__ == "__main__":
        main()


**How it works?**

#. Importing the STT Module

   .. code-block:: python

      from robot_hat.stt import STT

   The ``STT`` class is part of the ``robot_hat`` package. It handles all the
   low-level audio capture and speech recognition processing.

#. Setting the Language

   .. code-block:: python

      LANGUAGE = "en-us"

   The ``LANGUAGE`` variable configures the recognition language. You can
   change it to other supported codes such as ``"zh-cn"`` (Chinese) depending
   on your needs.

#. Creating the STT Instance

   .. code-block:: python

      stt = STT(language=LANGUAGE)

   This creates an STT object configured for the chosen language. The object
   initializes the microphone and the speech recognition engine.

#. The Listening Loop

   .. code-block:: python

      while True:
          print("Listening... (speak now)")
          text = stt.listen()
          if text:
              print(f">>> {text}")
          else:
              print("(no speech detected)")

   The program runs an infinite loop where each iteration:

   - Prompts the user to speak.
   - Calls ``stt.listen()`` which blocks until speech is detected and processed.
   - Returns the recognized text as a string, or ``None`` / empty if nothing
     was understood.
   - Prints the result to the terminal.

#. Graceful Exit

   .. code-block:: python

      except KeyboardInterrupt:
          print("\nExiting...")

   Pressing **Ctrl+C** raises a ``KeyboardInterrupt``, which is caught to print
   an exit message and terminate the program cleanly.
