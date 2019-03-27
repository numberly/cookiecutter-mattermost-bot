import os

from marshmallow import Schema
from marshmallow.fields import String
from marshmallow.validate import Equal, Length
from sanic import Sanic, response
from sanic.exceptions import abort

app = Sanic(__name__)

# the Mattermost token or tokens generated when you created your slash webhook
MATTERMOST_BOT_TOKEN = os.environ.get('MATTERMOST_BOT_TOKEN')


class BotSchema(Schema):
    text = String(validate=Length(min=3), required=True)
    token = String(validate=Equal(MATTERMOST_BOT_TOKEN), required=True)
    user_name = String(validate=Length(min=2), required=True)


@app.route('/', methods=['GET'])
async def get(request):
    return response.text('Hello there! You might want to POST on this URL.')


@app.route('/', methods=['POST'])
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
