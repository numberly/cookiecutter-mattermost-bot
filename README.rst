cookiecutter-mattermost-bot
===========================

🍪 Bootstrap Kubernetes-ready asynchronous Python 3.7 Mattermost bots.

Usage
-----

Install Cookiecutter:

.. code-block:: bash

   $ pip install --user cookiecutter

Generate a new bot:

.. code-block:: bash

   $ cookiecutter https://github.com/numberly/cookiecutter-mattermost-bot

To create the project, you will need:

- a hostname for the bot, that your Kubernetes setup can control,
- the URL on which the bot's Docker image will be hosted.

Once all questions have been answered, check the ``README.rst`` file of your newly generated application to learn how to run it.

License
-------

MIT
