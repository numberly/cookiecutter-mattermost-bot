#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

from bot.app import app
from bot.settings import MATTERMOST_BOT_TOKEN

if __name__ == "__main__":

    if not MATTERMOST_BOT_TOKEN:
        print("MATTERMOST_BOT_TOKEN must be set. "
              "Please see README.rst for instructions")
        sys.exit()

    port = os.environ.get('PORT', 5000)
    host = os.environ.get('HOST', '0.0.0.0')
    app.run(host=str(host), port=int(port), auto_reload=True)
