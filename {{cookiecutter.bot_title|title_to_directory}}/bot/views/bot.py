from asyncio import sleep

from marshmallow import Schema
from marshmallow.fields import String
from marshmallow.validate import Equal, Length
from sanic import Blueprint, response
from sanic.exceptions import abort

from bot.settings import MATTERMOST_BOT_TOKEN


bot = Blueprint("bot", url_prefix="/bot")


class BotSchema(Schema):
    text = String(validate=Length(min=3), required=True)
    token = String(validate=Equal(MATTERMOST_BOT_TOKEN), required=True)
    user_name = String(validate=Length(min=2), required=True)


@bot.route('/', methods=['GET'])
async def get(request):
    return response.text('Hello there! You might want to POST on this URL.')


@bot.route('/', methods=['POST'])
async def post(request):
    """
    Mattermost new post event handler
    """
    schema = BotSchema().load(request.form)
    if schema.errors:
        abort(400, schema.errors)

    message = "Retour du bot: {} from @{}".format(schema.data['text'],
                                                  schema.data['user_name'])
    return response.json({"text": message})
