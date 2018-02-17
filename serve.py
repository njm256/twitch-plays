#!/usr/bin/env python

from sys import exit
from config.config import config
import lib.bot as bot

# Twitch Plays
# Inpsired by http://twitch.tv/twitchplayspokemon
# Originally written by Aidan Thomson - <aidraj0 at gmail dot com>
# Shamelessly coopted for hackathon project

try:
    bot.Bot().run()
except KeyboardInterrupt:
    exit()
