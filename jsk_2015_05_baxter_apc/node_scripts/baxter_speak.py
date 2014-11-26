#!/usr/bin/python
#-*- coding:utf-8 -*-
import os
import sys
import argparse

import roslib; roslib.load_manifest('jsk_2014_picking_challenge')
import rospy

from sound_play.msg import *

def send_audio(speech, lang='en'):
    speech.replace(' ', '+')
    pub = rospy.Publisher('robotsound', SoundRequest, queue_size=100)
    print('http://translate.google.com/translate_tts?tl='+lang+'&q='+speech)
    req = SoundRequest(sound=SoundRequest.PLAY_FILE, command=SoundRequest.PLAY_ONCE, arg='http://translate.google.com/translate_tts?tl='+lang+'&q='+speech)
    print(req)
    rospy.init_node('robotspeaker', anonymous=True)
    pub.publish(req)

def main():
    """Baxter can speak."""
    arg_fmt = argparse.RawTextHelpFormatter
    parser = argparse.ArgumentParser(formatter_class=arg_fmt,
                                     description=main.__doc__)
    required = parser.add_argument_group('required arguments')
    required.add_argument(
        '-s', '--speak', required=True,
        help='What you want Baxter to speak.'
    )
    parser.add_argument(
        '-l', '--lang', type=str, default='en',
        help = 'select language'
    )
    args = parser.parse_args(rospy.myargv()[1:])

    print(args.speak)
    send_audio(args.speak, lang=args.lang)

    return 0

if __name__ == '__main__':
    sys.exit(main())
