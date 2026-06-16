#!/usr/bin/env python3
"""
PiCrawler CLI — control the quadruped robot from the command line.

Usage:
  pc.py move <action> [--steps N] [--speed N]
  pc.py pose <name> [--speed N]
  pc.py sensor distance
  pc.py sound play <file> [--volume N]
  pc.py sound volume <0-100>
  pc.py sound music <file> [--volume N]
  pc.py sound stop

Examples:
  pc.py move forward --steps 3 --speed 60
  pc.py pose stand --speed 40
  pc.py sensor distance
  pc.py sound play ~/picrawler/examples/sounds/talk1.wav --volume 80
"""

import argparse
from time import sleep


def cmd_move(args):
    from picrawler import Picrawler
    crawler = Picrawler()
    try:
        crawler.do_step('stand', 40)
        sleep(1.0)
        crawler.do_action(args.action, args.steps, args.speed)
    finally:
        crawler.do_step('sit', 40)
        sleep(1.0)


def cmd_pose(args):
    from picrawler import Picrawler
    crawler = Picrawler()
    try:
        crawler.do_step(args.name, args.speed)
        sleep(1.0)
    finally:
        pass  # don't auto-sit — caller might chain poses


def cmd_sensor(args):
    from robot_hat import Pin, Ultrasonic
    sonar = Ultrasonic(Pin("D2"), Pin("D3"))
    d = sonar.read()
    print(f"{d:.1f}" if d else "None")


def cmd_sound(args):
    from robot_hat import Music
    music = Music()
    if args.sound_cmd == "play":
        music.sound_play(args.file, volume=args.volume)
    elif args.sound_cmd == "volume":
        music.music_set_volume(args.volume)
    elif args.sound_cmd == "music":
        music.music_set_volume(args.volume or 20)
        music.music_play(args.file)
    elif args.sound_cmd == "stop":
        music.music_stop()


def main():
    parser = argparse.ArgumentParser(description="PiCrawler Robot Controller")
    sub = parser.add_subparsers(dest="command")
    sub.required = True

    # move
    move_p = sub.add_parser("move", help="Move the robot")
    move_p.add_argument("action", choices=[
        "forward", "backward",
        "turn left", "turn right",
        "turn left angle", "turn right angle",
    ])
    move_p.add_argument("--steps", type=int, default=1, help="Step count")
    move_p.add_argument("--speed", type=int, default=60, help="Speed 0-100")
    move_p.set_defaults(func=cmd_move)

    # pose
    pose_p = sub.add_parser("pose", help="Set robot pose")
    pose_p.add_argument("name", choices=["stand", "sit"])
    pose_p.add_argument("--speed", type=int, default=40, help="Speed 0-100")
    pose_p.set_defaults(func=cmd_pose)

    # sensor
    sensor_p = sub.add_parser("sensor", help="Read sensors")
    sensor_p.add_argument("type", choices=["distance"])
    sensor_p.set_defaults(func=cmd_sensor)

    # sound
    sound_p = sub.add_parser("sound", help="Sound control")
    sound_p.add_argument("sound_cmd", choices=["play", "volume", "music", "stop"])
    sound_p.add_argument("file", nargs="?", help="Sound file path")
    sound_p.add_argument("--volume", type=int, default=None, help="Volume 0-100")
    sound_p.set_defaults(func=cmd_sound)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
