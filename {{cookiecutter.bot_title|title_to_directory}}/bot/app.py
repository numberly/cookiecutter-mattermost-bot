import logging

from sanic import Sanic
from bot.views.bot import bot

logging.basicConfig(
    level=logging.INFO, format='[%(asctime)s] [%(levelname)s] %(message)s')

app = Sanic(__name__)
app.blueprint(bot)
