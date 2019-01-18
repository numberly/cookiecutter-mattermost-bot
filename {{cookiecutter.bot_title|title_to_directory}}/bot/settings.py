import os

USERNAME = os.environ.get('USER_NAME', '{{cookiecutter.bot_user_name}}')

ICON_URL = os.environ.get('ICON_URL', '{{cookiecutter.bot_icon_url}}')

# the Mattermost token or tokens generated when you created your slash webhook
MATTERMOST_BOT_TOKEN = os.environ.get('MATTERMOST_BOT_TOKEN',
                                      '{{cookiecutter.mattermost_token}}')
