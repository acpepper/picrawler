# Picrawler

Picrawler Python library and examples for Raspberry Pi.

Quick Links:

- [Picrawler](#picrawler)
  - [Docs](#docs)
  - [Installation](#installation)
    - [install tool](#install-tool)
    - [robot-hat library](#robot-hat-library)
    - [vilib library](#vilib-library)
    - [picrawler library](#picrawler-library)
  - [About SunFounder](#about-sunfounder)
  - [Contact us](#contact-us)

----------------------------------------------

## Docs

- <https://docs.sunfounder.com/projects/pi-crawler/en/latest/>

----------------------------------------------

## Installation

- <https://docs.sunfounder.com/projects/pi-crawler/en/latest/python/python_start/install_all_modules.html>

### install tool

```bash
sudo apt install git python3-pip python3-setuptools python3-smbus
```

### robot-hat library

```bash
cd ~/
git clone -b 2.5.x --depth=1 https://github.com/sunfounder/robot-hat.git
cd robot-hat
sudo python3 install.py
```

### vilib library

```bash
cd ~/
git clone --depth=1 https://github.com/sunfounder/vilib.git
cd vilib
sudo python3 install.py
```

### picrawler library

```bash
cd ~/
git clone --depth=1 https://github.com/sunfounder/picrawler.git
sudo pip3 install ~/picrawler --break-system-packages
```

----------------------------------------------

## Examples

Run examples with `sudo` (required for GPIO/servo access):

```bash
sudo python3 ~/picrawler/examples/1_move.py
```

| # | Example | Description |
|---|---------|-------------|
| 0 | `0_calibration.py` | Servo calibration helper |
| 1 | `1_move.py` | Basic movement control |
| 2 | `2_keyboard_control.py` | W/A/S/D keyboard control |
| 3 | `3_sound_effect.py` | Play sound effects |
| 4 | `4_avoid.py` | Obstacle avoidance with ultrasonic |
| 5 | `5_display.py` | Camera / computer vision display |
| 6 | `6_record_video.py` | Record video from camera |
| 7 | `7_bull_fight.py` | Bull fight interactive game |
| 8 | `8_treasure_hunt.py` | Treasure hunt game |
| 9 | `9_preset_actions.py` | Pose demonstration (wave, nod, etc.) |
| 10 | `10_do_single_leg.py` | Adjust single leg posture |
| 11 | `11_record_new_step.py` | Record custom steps via keyboard |
| 12 | `12_twist.py` | Twist / body rotation |
| 13 | `13_emotional_robot.py` | Emotional expression robot |
| 14 | `14_do_step.py` | Custom step coordinate control |
| 15 | `15_servo_zeroing.py` | Servo zeroing utility |
| 16 | `16_stt.py` | Speech-to-text demo |
| 17 | `17_tts.py` | Text-to-speech demo |
| 18 | `18_voice_active_crawler_gpt.py` | Voice AI with GPT-4o |
| 19 | `19_voice_active_crawler_ollama.py` | Voice AI with Ollama (local) |
| 20 | `20_voice_active_crawler_doubao.py` | Voice AI with Doubao (Chinese) |

----------------------------------------------

## About SunFounder

SunFounder is a technology company focused on Raspberry Pi and Arduino open source community development. Committed to the promotion of open source culture, we strives to bring the fun of electronics making to people all around the world and enable everyone to be a maker. Our products include learning kits, development boards, robots, sensor modules and development tools. In addition to high quality products, SunFounder also offers video tutorials to help you make your own project. If you have interest in open source or making something cool, welcome to join us!

----------------------------------------------

## Contact us

website:
    www.sunfounder.com

E-mail:
    service@sunfounder.com, support@sunfounder.com
